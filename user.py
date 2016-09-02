import logging
import MySQLdb
import sys


USER_TABLE = "User"
PASSWORD = "zillow"


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


class UserInvalidException(Exception):
    msg = "Specified user is not valid in our Company."


class User(object):
    """
    For storing user data
    """
    def __init__(self, id, name, extension):
        self.employee_id = id
        self.employee_name = name
        self.employee_extension = extension


class UserManager(object):
    """
    For performing all user related activities
    """
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.get_cursor()

    def get_user_by_id(self, employee_id):
        sql_query = "SELECT * FROM " + USER_TABLE + \
                    " WHERE UserID = " + str(employee_id)
        self.cursor.execute(sql_query)
        employee_data = self.cursor.fetchone()
        if employee_data is not None:
            self.user_obj = User(employee_id, employee_data["UserName"],
                                 employee_data["Extension"])
            return self.user_obj
        else:
            raise UserInvalidException()

    def add_user(self, employee_name, employee_extension):
        try:
            sql_query = "INSERT INTO " + USER_TABLE + \
                        "(UserName, Extension) " + \
                        "VALUES('" + \
                        employee_name + "', " + \
                        str(employee_extension) + ")"
            self.cursor.execute(sql_query)
            self.connection.connector.commit()
            self.cursor.execute("SELECT UserID FROM " + USER_TABLE +
                                " WHERE UserName = '" + employee_name +
                                "' AND Extension = " + str(employee_extension))
            row = self.cursor.fetchone()
            logger.info("Your Employee-ID is: {}".format(row["UserID"]))
        except MySQLdb.Error, e:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)

    def remove_user(self, employee_id):
        try:
            sql_query = "SELECT * FROM " + USER_TABLE + \
                        " WHERE UserID = " + str(employee_id)
            self.cursor.execute(sql_query)
            employee_data = self.cursor.fetchone()
            if employee_data is not None:
                sql_query = "DELETE FROM " + USER_TABLE + \
                            " WHERE UserID = " + str(employee_id)
                self.cursor.execute(sql_query)
                logger.info("Removing user account with ID " + str(employee_id) +
                            " from the db.")
                self.connection.connector.commit()
            else:
                raise UserInvalidException()
            
        except MySQLdb.Error, e:
            logger.error("Caught MYSQL exception :%s" % (e))
            self.connection.connector.rollback()
            sys.exit(0)


class Authentication(object):
    """
    Authenticating the validity of a user.
    """
    def __init__(self, cursor=None):
        self.cursor = cursor

    def is_user_valid(self, user):
        """
        Return validation of user
        """
        logger.info("Authenticating user-ID " + str(user.employee_id))
        sql_query = "SELECT * FROM " + USER_TABLE + \
                    " WHERE UserID = " + str(user.employee_id) + \
                    " AND UserName = '" + user.employee_name + \
                    "' AND Extension = " + str(user.employee_extension)
        self.cursor.execute(sql_query)
        employee_row = self.cursor.fetchone()
        return bool(employee_row)
        if employee_row is not None:
            return True
        else:
            return False

    def _is_valid_password(self, passwd):
        if passwd == PASSWORD:
            return True
        else:
            logger.info("Sorry, Wrong password...!")
            return False
