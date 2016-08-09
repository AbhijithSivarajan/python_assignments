"""Usage:      overlap.py --list1=LIST --list2=LIST

Arguements:
        --list1=LIST    List of elements
        --list2=LIST    List of elements

Options:
        -h, --help      Show the help message
"""


import docopt
import logging
import re


"""
To compare between two lists and return True even if
one element is same in both the lists.
"""


arguments = []


# Setting up logger
logging.basicConfig(filename='overlap.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s: '
                              '%(asctime)s:\n %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


def overlapping(list1, list2):
    """
    Function to check presence of any common element.
    """
    try:
        for word_list1 in list1:
            if word_list1 in list2:
                return True
        return False
    except TypeError:
        raise Exception('Input not in Expected Format.')


def access_input(key):
    input_string = str(arguments[key])
    return filter(None, re.split("[\[\], ;']+", input_string))


if __name__ == '__main__':

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        input_list1 = access_input('--list1')
        input_list2 = access_input('--list2')

        result = overlapping(input_list1, input_list2)
        logger.info("Overlapping Exists: {}\n".format(result))

    except docopt.DocoptExit as e:
        logger.error(e.message)
