"""
Usage:      filter.py --choice=N --max=N TEXT...

Arguments:
        TEXT    The list of strings for filtering.

Options:
        -h, --help      Show help file

        --choice=N      Choice to use built-in functions or not

        --max=N         Maximum length of acceptable string
"""


import docopt
import logging
import re
import sys

"""
To filter words from a list with string-length greater than max_length.
"""


CHOICE_FOR_WITH_BUILT_IN = 1
CHOICE_FOR_WITHOUT_BUILT_IN = 2
VALID_CHOICES = [CHOICE_FOR_WITH_BUILT_IN, CHOICE_FOR_WITHOUT_BUILT_IN]


# Setting up logger
logging.basicConfig(filename='filter.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s : '
                              '%(asctime)s:\t %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


class Filter(object):
    """
    Class to filter list with strings of length greater than max_length.
    """
    def __init__(self):
        self.reslist = []

    def filter_long_words(self, choice, input_list, max_length):
        """
        Method to filter the list with words greater than specified length.
        """
        try:
            if is_valid_choice(choice):

                    if choice == CHOICE_FOR_WITH_BUILT_IN:
                        for x in input_list:
                            if len(x) > max_length:
                                self.reslist.append(x)
                    elif choice == CHOICE_FOR_WITHOUT_BUILT_IN:
                        for x in input_list:
                            cnt = 0
                            for y in x:
                                cnt = cnt + 1
                            if cnt > max_length:
                                self.reslist.append(x)
                    return self.reslist
            else:
                raise Exception('Invalid choice provided')

        except Exception:
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
        # Take max. length for filtering.
        try:
            choice = int(arguments['--choice'])
            max_length = int(arguments['--max'])
        except ValueError:
            logger.error("Wrong input...Not a valid integer number.\n")
            sys.exit(0)

        #  Access elements of list.
        input_string = str(arguments['TEXT'])
        input_list = filter(None, re.split("[\[\], ;']+", input_string))

        filter_obj = Filter()
        try:
            result_list = filter_obj.filter_long_words(choice, input_list, \
                                                   max_length)
            logger.info("\n  Filtered List :- {}\n".format(result_list))
        except Exception:
            logger.error('Invalid choice provided...\n')

    except docopt.DocoptExit as e:
        logger.error(e.message)
