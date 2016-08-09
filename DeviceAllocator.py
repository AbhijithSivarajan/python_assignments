import pyodbc
import sys


class Connection(object):
"""
Setting up a connection with the database
"""

    def __init__(self):
    """
    Connect to the database
    """
        self.connector = pyodbc.connect()
        
    def get_cursor(self):
    """
    Get a cursor from the connection
    """
        return self.connector.cursor()
        
        
class Authentication(object):
"""
Authenticating the validity of a user.
"""

    def is_user_valid(self):
        """
        Return validation
        """
        pass

        
class Notification(object):
"""
Contains operations related to setting up & sending notifications
"""
    
    def set_notification(self):
        """
        Set notification for a particular user for a device.
        """
        pass
        
    def check_notification(self):
        """
        Check if notification is set for a device.
        """
        pass

    def send_notification(self):
        """
        Send notification on availability of device.
        """
        pass
        
        
class User(object):
"""
For performing all user activities
"""

    employee_id = 0
    
    def __init__(self):
        pass
    
    def request_device(self):
        """
        If user is valid & device is available, allocate the device.
        """
        pass
        
    def release_device(self):
        """
        If user is valid & device is allocated, de-allocate the device.
        """
        pass
        
        
class Device(object):
"""
For performing device specific activities
"""

    device_id = 0
    battery_left = 100
    
    def __init__(self):
        pass
        
    def list_all_devices(self):
        """
        Display list of all the devices.
        """
        pass
        
    def list_available_devices(self):
        """
        Display list of all the available devices.
        """
        pass
             
    def add_device(self):
        """
        Add a new device
        """
        pass
        
    def delete_device(self):
        """
        Delete a device
        """
        pass
             
             
class DeviceAllocationManager(object):
"""
Takes care of all the device allocations and de-allocations
"""

    def is_device_available(self):
        """
        Check if specified device is available or not
        """
        pass
        
    def allocate_device(self):
        """
        Allocate the device, i.e, reduce the quantity of device
        """
        pass
        
    def de_allocate_device(self):
        """
        De-allocate the device, i.e, increase the quantity of device
        """
        pass
        
        
if __name__ == '__main__':

    while True:
        print ("\nMenu\n"
               "1. List All Devices\n"
               "2. List Available devices\n"
               "3. Access a device\n"
               "4. Release a device\n"
               "5. Exit\n")

            option = int(input('Choose your option : '))
            
        cursor = Connection().get_cursor()
        
        device = Device()
        user = User()
        
        if option == 1:
            device.list_all_devices()
            
        elif option == 2:
            device.list_available_devices()
            
        elif option == 3:
            user.access_device()
            
        elif option == 4:
            user.release_device()
            
        elif option == 5:
            sys.exit(0)
            
        else:
            """
            Display proper error message
            """
            sys.exit(0)
