import logging
import MySQLdb


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


class Connection(object):
    """
    Setting up a connection with the database
    """

    _instance = None

    def __new__(conn, *args, **kwargs):
        """
        Setting the class to be singleton
        """
        if not conn._instance:
            conn._instance = super(Connection, conn).__new__(
                                conn, *args, **kwargs)
        return conn._instance

    def __init__(self):
        """
        Connect to the database
        """
        logger.info("Connecting to Database")
        self.connector = MySQLdb.connect(host="localhost",
                                         user="root",
                                         passwd="emtec*123",
                                         db="trainingdb")

    def get_cursor(self):
        """
        Get a cursor from the connection
        """
        return self.connector.cursor(MySQLdb.cursors.DictCursor)
