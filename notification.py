import logging
import MySQLdb
import sys


NOTIFICATION_TABLE = "Notify"


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


class Notification(object):
    """
    For storing notification data
    """
    def __init__(self, notification_id, employee_id, device_model):
        self.notification_id = notification_id
        self.employee_id = employee_id
        self.device_model = device_model


class NotificationManager(object):
    """
    Contains operations related to setting up & sending notifications
    """
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.get_cursor()

    def set_notification(self, employee_id, device_model):
        """
        Set notification for a particular user for a device.
        """
        try:
            sql_query = "INSERT INTO " + NOTIFICATION_TABLE + \
                        "(UserID, DeviceModel)" \
                        "VALUES (" + str(employee_id) + \
                        ", '" + device_model + "')"
            logger.info("Set Notification for DeviceModel:{} for "
                        "Employee-ID:{}".format(device_model, employee_id))
            self.cursor.execute(sql_query)
            self.connection.connector.commit()
            return self.cursor.lastrowid
        except MySQLdb.Error:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)

    def check_notification(self, device_model):
        """
        Check if notification is set for a device.
        """
        logger.info("Checking Notification for {}".format(device_model))
        try:
            sql_query = "SELECT * FROM " + NOTIFICATION_TABLE + \
                        " WHERE DeviceModel = '" + device_model + "'"
            self.cursor.execute(sql_query)

            notification_rows = self.cursor.fetchall()

            self.cursor.execute("DELETE FROM " + NOTIFICATION_TABLE +
                                " WHERE DeviceModel = '" + device_model +
                                "'")
            self.connection.connector.commit()

            for row in notification_rows:
                notify_obj = Notification(row["NotificationID"],
                                          row["UserID"], row["DeviceModel"])
                self.send_notification(notify_obj)
        except MySQLdb.Error:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)

    def send_notification(self, notify_obj):
        """
        Send notification on availability of device.
        """
        logger.info("The notification with Id - " +
                    str(notify_obj.notification_id) +
                    " is now active. " + notify_obj.device_model +
                    " is available.")
