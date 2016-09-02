import logging
import MySQLdb
import sys

from datetime import datetime, timedelta

from user import Authentication
from notification import NotificationManager

DEVICE_TABLE = "Device"
CLAIMED_DEVICE_TABLE = "ClaimedDevice"


# Setting up logger
logging.basicConfig(filename='DeviceAllocator.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s '
                           '[%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s '
                              '[%(name)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)


class DeviceNotAvailableException(Exception):
    msg = "Specified device is not available in our Company."


class Device(object):
    """
    For performing device specific activities
    """
    def __init__(self):
        self.device_id = None
        self.model = None
        self.type = None
        self.manufacturer = None
        self.os_version = None
        self.scree_size = None
        self.resolution = None
        # self.battery_left = 100


class DeviceManager(object):
    """
    Takes care of all the device allocations and de-allocations
    """
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.get_cursor()
        self.auth = Authentication(self.cursor)
        self.notification = NotificationManager(self.connection)

    def list_all_devices(self):
        """
        Display list of all the devices.
        """
        self.cursor.execute("SELECT * " +
                            "FROM " + DEVICE_TABLE)
        logger.info("ID  Type\tModel\t OS\tScreenSize\tResolution")
        for row in self.cursor.fetchall():
            logger.info("{}.  {}    {}\t {}\t{}\t\t{}".format
                        (row["DeviceID"], row["Type"], row["Model"],
                         row["OS_Version"], row["ScreenSize"],
                         row["Resolution"]))
        return

    def list_available_devices(self):
        """
        Display list of all the available devices.
        """
        self.cursor.execute("SELECT * " +
                            "FROM " + DEVICE_TABLE + " D" +
                            " WHERE D.DeviceID IN " +
                            "(SELECT DeviceID FROM " + DEVICE_TABLE +
                            " WHERE DeviceID NOT IN " +
                            "(SELECT DeviceID" +
                            " FROM " + CLAIMED_DEVICE_TABLE +
                            " WHERE Status = 1) )")
        logger.info("ID  Type\tModel\t OS\tScreenSize\tResolution")
        for row in self.cursor.fetchall():
            logger.info("{}.  {}    {}\t {}\t{}\t\t{}".format
                        (row["DeviceID"], row["Type"], row["Model"],
                         row["OS_Version"], row["ScreenSize"],
                         row["Resolution"]))
        return

    def request_device(self, user, device_model, time_for_use):
        """
        If user is valid & device is available, allocate the device.
        """
        device = None

        if self.auth.is_user_valid(user):

            try:
                device = self._is_device_available(device_model)
                if device is not None:
                    self._allocate_device(user.employee_id, device,
                                          time_for_use)
                    return True
                else:
                    claimed_list = self._get_claimed_users(device_model)
                    logger.info("DeviceID  UserID\tExpectedReleaseTime")
                    for row in claimed_list:
                        logger.info("{}\t  {}\t{}".format
                                    (row["DeviceID"], row["UserID"],
                                     row["ExpectedReleaseTime"]))
                    return False
            except DeviceNotAvailableException, e:
                raise DeviceNotAvailableException()

        else:
            logger.info("You are not authorized to access the device. " +
                        "Please contact the person-in-charge.")
            sys.exit(0)

    def release_device(self, employee_id, device_id):
        """
        If user is valid & device is allocated, de-allocate the device.
        """
        try:
            if self._is_device_allocated(employee_id, device_id):
                self._de_allocate_device(device_id, employee_id)
                device_model = self._get_device_model(device_id)
                self.notification.check_notification(device_model)
                return True
            else:
                logger.info("Sorry, Finding issues in completing the process."
                            " Please, verify the device_id specified or else"
                            " Please contact the person-in-charge.")
        except Exception:
            return False

    def add_device(self, model, type, manufacturer,
                   os_version, scree_size, resolution):
        try:
            if manufacturer is not None:
                sql_query = "INSERT INTO " + DEVICE_TABLE + \
                            "(Model, Type, Manufacturer, OS_Version, " + \
                            "ScreenSize, Resolution)" + \
                            "VALUES ('" + \
                            model + "', '" + type + "', '" + manufacturer + \
                            "', '" + os_version + "', '" + scree_size + \
                            "', '" + resolution + "')"
            else:
                sql_query = "INSERT INTO " + DEVICE_TABLE + \
                            "(Model, Type, OS_Version, " + \
                            "ScreenSize, Resolution)" + \
                            "VALUES ('" + \
                            model + "', '" + type + "', '" + os_version + \
                            "', '" + scree_size + "', '" + resolution + "')"
            self.cursor.execute(sql_query)
            self.connection.connector.commit()
            self.cursor.execute("SELECT DeviceID FROM " + DEVICE_TABLE +
                                " WHERE Model = '" + model +
                                "' ORDER BY DeviceID DESC LIMIT 1")
            row = self.cursor.fetchone()
            logger.info("The Device-ID is: {}".format(row["DeviceID"]))
        except MySQLdb.Error, e:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)

    def remove_device(self, device_id):
        try:
            sql_query = "DELETE FROM " + DEVICE_TABLE + \
                        " WHERE DeviceID = " + str(device_id)
            self.cursor.execute(sql_query)
            logger.info("Removing device with ID " + str(device_id) +
                        " from the db.")
            self.connection.connector.commit()
        except MySQLdb.Error, e:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)

    def _is_device_available(self, device_model):
        """
        Check if specified device is available or not
        """
        logger.info("Checking whether {} is available".format(device_model))

        self.cursor.execute("SELECT DeviceID FROM " + DEVICE_TABLE +
                            " WHERE Model = '" + device_model + "'")
        if self.cursor.fetchone() is not None:
            self.cursor.execute("SELECT * " +
                                "FROM " + DEVICE_TABLE + " D " +
                                "WHERE Model = '" + device_model +
                                "' AND D.DeviceID IN " +
                                "(SELECT DeviceID FROM " + DEVICE_TABLE +
                                " WHERE DeviceID NOT IN " +
                                "(SELECT DeviceID " +
                                "FROM " + CLAIMED_DEVICE_TABLE +
                                " WHERE Status = 1) )")
            device_row = self.cursor.fetchone()
            if device_row is not None:
                device_obj = Device()
                device_obj.device_id = device_row["DeviceID"]
                device_obj.type = device_row["Type"]
                device_obj.model = device_row["Model"]
                device_obj.manufacturer = device_row["Manufacturer"]
                device_obj.os_version = device_row["OS_Version"]
                device_obj.scree_size = device_row["ScreenSize"]
                device_obj.resolution = device_row["Resolution"]
                return device_obj
            return None
        else:
            raise DeviceNotAvailableException()

    def _get_claimed_users(self, device_model):
        """
        Specify the list of users who have the particular device type
        """
        logger.info("Collecting the claimed users\' data")
        self.cursor.execute("SELECT * " +
                            "FROM " + CLAIMED_DEVICE_TABLE +
                            " WHERE DeviceID IN " +
                            " (SELECT DeviceID FROM " + DEVICE_TABLE +
                            " WHERE Model = '" + device_model +
                            "') AND Status = 1")
        return self.cursor.fetchall()

    def _allocate_device(self, employee_id, device, time_for_use):
        """
        Allocate the device, i.e, reduce the quantity of device
        """
        logger.info("Allocating {} with ID {} to employee with ID: {}".format(
                     device.model, device.device_id, employee_id))
        time = datetime.now()
        access_time = "{}:{}:{}".format(time.hour, time.minute, time.second)

        release_time = datetime.now() + timedelta(minutes=time_for_use)
        expected_release = "{}:{}:{}".format(release_time.hour,
                                             release_time.minute,
                                             release_time.second)
        try:
            sql_query = "INSERT INTO " + CLAIMED_DEVICE_TABLE + \
                        "(DeviceID, UserID, AccessTime, " + \
                        "ExpectedReleaseTime, Status)" + \
                        " VALUES (" + \
                        str(device.device_id) + ", " + \
                        str(employee_id) + ", '" + \
                        access_time + "', '" + \
                        expected_release + "', 1)"
            self.cursor.execute(sql_query)
            self.connection.connector.commit()
        except MySQLdb.Error:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
        return

    def _is_device_allocated(self, employee_id, device_id):
        """
        Check if the particular device is allocated to user or not
        Returns True or False
        """
        logger.info("Checking whether device {} is allocated".format(
                     device_id))
        self.cursor.execute("SELECT * FROM " + CLAIMED_DEVICE_TABLE +
                            " WHERE UserID = " + str(employee_id) +
                            " AND DeviceID = " + str(device_id) +
                            " AND Status = 1")
        claim_row = self.cursor.fetchone()
        if claim_row is not None:
            return True
        return False

    def _de_allocate_device(self, device_id, employee_id):
        """
        De-allocate the device, i.e, increase the quantity of device
        """
        logger.info("De-allocating device {} from "
                    "employee with ID: {}".format(device_id, employee_id))
        time = datetime.now()
        actual_release_time = "{}:{}:{}".format(time.hour,
                                                time.minute, time.second)
        try:
            self.cursor.execute("UPDATE " + CLAIMED_DEVICE_TABLE +
                                " SET Status = 0, ActualReleaseTime = '" +
                                actual_release_time +
                                "' WHERE UserID = " + str(employee_id) +
                                " AND DeviceID = " + str(device_id) +
                                " AND Status = 1")
            self.connection.connector.commit()
        except MySQLdb.Error:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
        return

    def _get_device_model(self, device_id):
        """
        Get model of de_allocated device
        """
        self.cursor.execute("SELECT Model FROM " + DEVICE_TABLE +
                            " WHERE DeviceID = " + str(device_id))
        device_row = self.cursor.fetchone()
        if device_row is not None:
            return device_row["Model"]
        return None
