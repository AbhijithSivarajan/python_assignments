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

    def is_user_valid(self, user):
        """
        Return validation of user
        """
        cursor.execute("select * from UserTable")
        employee_rows = cursor.fetchall()
        user_for_verification = [user.employee_id, \
                                 user.employee_name, \
                                 user.employee_extension]
        if user_for_verification in employee_rows:
            return True
        else:
            return False


class Notification(object):
    """
    Contains operations related to setting up & sending notifications
    """

    def set_notification(self, employee_id, device_model):
        """
        Set notification for a particular user for a device.
        """
        pass
        
    def check_notification(self, device_model):
        """
        Check if notification is set for a device.
        """
        # if notification is set:
                # self.send_notification(employee_id, device_model)
        pass

    def send_notification(self, employee_id, device_model):
        """
        Send notification on availability of device.
        """
        pass
        
        
class User(object):
    """
    For performing all user activities
    """    
    def __init__(self):
        employee_id = 0
        employee_name = None
        employee_extension = 0
        
        
class Device(object):
    """
    For performing device specific activities
    """
    def __init__(self):
        device_id = 0
        device_model = None
        '''
        device_type = None
        device_manufacturer = None
        os_version = None
        scree_size = None
        resolution = None
        '''
        # battery_left = 100
        
    def list_all_devices(self):
        """
        Display list of all the devices.
        """
        cursor.execute("select * from DeviceTable")
        rows = cursor.fetchall()
        for row in rows:
            print "{}.  {}    {}\t{}\t{}\t{}".format \
            (row.DeviceID, row.Type, row.Model, row.OS_Version, \
             row.ScreenSize, row.Resolution)
        
    def list_available_devices(self):
        """
        Display list of all the available devices.
        """
        cursor.execute()
        rows = cursor.fetchall()
        for row in rows:
            print "{}.  {}    {}\t{}\t{}\t{}".format \
            (row.DeviceID, row.Type, row.Model, row.OS_Version, \
             row.ScreenSize, row.Resolution)
             
             
class DeviceAllocationManager(object):
    """
    Takes care of all the device allocations and de-allocations
    """
    def __init__(self):
        self.auth = Authentication()
        self.notification = Notification()
    
    def request_device(self, user, device_model):
        """
        If user is valid & device is available, allocate the device.
        """
        if self.auth.is_user_valid(user):
            if self.__is_device_available(device_model):
                self.__allocate_device(user.employee_id, device_model)
            else:
                claimed_list = self.__get_claimed_users(device_model)
                for row in claimed_list:
                    print "{}\t{}\t{}\t{}".format \
                    (row.DeviceID, row.EmployeeID, row.AccessTime, \
                     row.ExpectedReleaseTime)
                     
                notification_choice = input("Do you want to be notified(Y/N): ")
                if notification_choice in ['Y','y']:
                    self.notification.set_notification(device_model)
        else:
            print ("You are not authorized to access the device. " +
                  "Please contact the person-in-charge.")
        
    def release_device(self, employee_id, device_id):
        """
        If user is valid & device is allocated, de-allocate the device.
        """
        if self.auth.is_user_valid(employee_id):
        
            if self.__is_device_allocated(employee_id, device_id):
                self.__de_allocate_device(device_id)
                self.notification.check_notification(device_model)
                
            else:
                print ("Sorry, Finding issues in completing the process. " +
                      "Please, verify the device_id specified or else "
                      "Please contact the person-in-charge.")
                      
        else:
            print ("You are not authorized. " +
                  "Please contact the person-in-charge.")

    def __is_device_available(self, device_model):
        """
        Check if specified device is available or not
        Returns True or False
        """
        pass
        
    def __get_claimed_users(self, device_model):
        """
        Specify the list of users who have the particular device type
        """
        cursor.execute("select * from ClaimedDevice "+
                       "where Model = "+ device_model +" and Status = 1"
                      )
        return cursor.fetchall()
        
        
    def __allocate_device(self, employee_id, device_model):
        """
        Allocate the device, i.e, reduce the quantity of device
        """
        pass
        
    def __is_device_allocated(self, employee_id, device_id):
        """
        Check if the particular device is allocated to user or not
        Returns True or False
        """
        pass
        
    def __de_allocate_device(self, device_id):
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
            
        # cursor = Connection().get_cursor()
        
        device = Device()
        user = User()
        dam = DeviceAllocationManager()
        
        if option == 1:
            device.list_all_devices()
            
        elif option == 2:
            device.list_available_devices()
            
        elif option == 3:
            device_model = raw_input('\nEnter device model: ')
            user.employee_id = input('\nEnter your Employee-ID: ')
            user.employee_name = input('\nEnter your Name: ')
            user.employee_extension = input('\nEnter your Extension: ')
            dam.request_device(user, device_model)
            
        elif option == 4:
            dam.release_device()
            
        elif option == 5:
            sys.exit(0)
            
        else:
            """
            Display proper error message
            """
            sys.exit(0)
