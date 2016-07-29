"""
Usage:      strlength.py --choice=N --list=LIST TEXT...

Arguments:
        TEXT    The string for calculating length.
        LIST    The list for calculating length.

Options:
        -h, --help      Show this message.

        --choice=N       Choice to use built-in functions or not.

        --list=LIST...  The list for calculating length.
"""


import sys
import logging
import docopt
import re


"""
To find length of a string and list using built-in functions and
without using built-in functions.
"""


CHOICE_FOR_WITH_BUILT_IN = 1
CHOICE_FOR_WITHOUT_BUILT_IN = 2
VALID_CHOICES = [CHOICE_FOR_WITH_BUILT_IN, CHOICE_FOR_WITHOUT_BUILT_IN]


# Setting up logger
logging.basicConfig(filename='strlength.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s : '
                              '%(asctime)s:\t %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


class Length(object):
    """
    Class to calcute length of string and list.
    """

    def __init__(self):
        self.result = []

    def built_in(self, input):
        """
        Method to calculate length of string and list using built-in methods.
        """
        try:
            return len(input)
        except TypeError:
            logger.error('Wrong input...Not a valid Integer Number...\n')
            raise Exception('Input not in Expected Format.')

    def without_built_in(self, input):
        """
        Method to calculate length of string, list using user-defined methods.
        """
        input_length = 0
        try:
            for x in input:
                input_length = input_length + 1
            return input_length
        except TypeError:
            logger.error('Wrong input...Not a valid Integer Number...\n')
            raise Exception('Input not in Expected Format.')


def is_valid_choice(choice):
    """
    Check if choice provided is valid or not.
    """
    return (choice in VALID_CHOICES)


if __name__ == '__main__':

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        # Take choice to use Built-In Functions or not.
        try:
            choice = int(arguments['--choice'])
        except ValueError:
            logger.error("Choice not a valid number.\n")
            sys.exit(0)

        # To take string & list.
        string = ' '.join(arguments['TEXT'])
        input_string = str(arguments['--list'])
        input_list = filter(None, re.split("[\[\], ;']+", input_string))

        length_obj = Length()

        if is_valid_choice(choice):

            if choice == CHOICE_FOR_WITH_BUILT_IN:
                list_length = length_obj.built_in(input_list)
                string_length = length_obj.built_in(string)

            elif choice == CHOICE_FOR_WITHOUT_BUILT_IN:
                list_length = length_obj.without_built_in(input_list)
                string_length = length_obj.without_built_in(string)

        else:
            logger.error('Invalid choice provided...\n')
            sys.exit(0)

        logger.info("Length of string is: {}".format(string_length))
        logger.info("Length of list is: {}\n".format(list_length))

    except docopt.DocoptExit as e:
        logger.exception(e.message)
