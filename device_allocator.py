"""
Usage:
device_allocator.py --list=TEXT[all|available]
device_allocator.py request --device="TEXT" --userID=TEXT
                                 --time=TEXT --notify=[Y|N]
device_allocator.py release --deviceID=TEXT --userID=TEXT
device_allocator.py adduser --pwd=TEXT --name=TEXT --ext=TEXT
device_allocator.py deluser --pwd=TEXT --userID=TEXT
device_allocator.py deviceadd --pwd=TEXT --model="TEXT" --type=TEXT
                                   --OSVersion=TEXT --screensize=TEXT
                                   --resolution=TEXT [--manufacturer=TEXT]
device_allocator.py deldevice --pwd=TEXT --deviceID=TEXT

Options:
        -h, --help          Show this message.
        list                Choice to list devices (all / available)
        device              Device model to be accessed
        deviceID            ID of device
        userID              UserID of employee
        time                Required Time for use
        notify              Set Notification or not
        pwd                 Password
        name                Name of User
        ext                 Extension no. of user
        model               Model of the device
        type                Type of the device(Phone/Tablet/Phablet)
        OSVersion           OS Version of the Device
        screensize          Screen Size of the device(in inches)
        resolution          Resolution of the device (ht x wt)
        manufacturer        Manufacturer of the device
"""


import docopt
import logging
import sys

from connection import Connection
from device_manager import DeviceManager, DeviceNotAvailableException
from notification import NotificationManager
from user import Authentication, UserManager, UserInvalidException


# Setting up logger
logging.basicConfig(filename='device_allocator.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s '
                           '[%(name)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s '
                              '[%(name)s] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


if __name__ == '__main__':

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        connection = Connection()
        cursor = connection.get_cursor()

        user_manager = UserManager(connection)
        device_manager = DeviceManager(connection)
        authentication = Authentication()

        if arguments['request'] is True:

            device_model = str(arguments['--device'])
            employee_id = int(arguments['--userID'])
            time_for_use = int(arguments['--time'])

            try:
                user = user_manager.get_user_by_id(employee_id)
            except UserInvalidException, e:
                logger.warn(e.msg)
                sys.exit(0)

            try:
                allocated = device_manager.request_device(user, device_model,
                                                          time_for_use)
            except DeviceNotAvailableException, e:
                logger.warn(e.msg)
                sys.exit(0)

            if not allocated:
                notification_choice = str(arguments['--notify'])
                if notification_choice in ['Y', 'y']:
                    notification = NotificationManager(connection)
                    notificationID = notification.set_notification(
                                        user.employee_id, device_model)
                    logger.info("Your notification-ID is: " +
                                str(notificationID))
                elif notification_choice not in ['N', 'n']:
                    logger.error("Enter proper choice...")
                    sys.exit(0)

        elif arguments['release'] is True:
            device_id = int(arguments['--deviceID'])
            employee_id = int(arguments['--userID'])
            device_manager.release_device(employee_id, device_id)

        elif str(arguments['--list']) == 'all':
            device_manager.list_all_devices()

        elif str(arguments['--list']) == 'available':
            device_manager.list_available_devices()

        elif arguments['adduser'] is True:
            if authentication._is_valid_password(str(arguments['--pwd'])):
                user_manager.add_user(str(arguments['--name']),
                                      int(arguments['--ext']))

        elif arguments['deluser'] is True:
            if authentication._is_valid_password(str(arguments['--pwd'])):
                user_manager.remove_user(int(arguments['--userID']))

        elif arguments['deviceadd'] is True:
            if authentication._is_valid_password(str(arguments['--pwd'])):
                device_manager.add_device(str(arguments['--model']),
                                          str(arguments['--type']),
                                          str(arguments['--manufacturer']),
                                          str(arguments['--OSVersion']),
                                          str(arguments['--screensize']),
                                          str(arguments['--resolution']))

        elif arguments['deldevice'] is True:
            if authentication._is_valid_password(str(arguments['--pwd'])):
                device_manager.remove_device(int(arguments['--deviceID']))

        else:
            logger.info("Sorry, Wrong choice...!")
            sys.exit(0)

    except docopt.DocoptExit as e:
        logger.error(e.message)
    except (ValueError, NameError, SyntaxError):
        logger.error('Wrong input...Not a valid Integer Number...\n')
    except (DeviceNotAvailableException, UserInvalidException) as e:
        logger.warn(e.msg)