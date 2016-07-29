"""Usage:      overlap.py --list1=LIST --list2=LIST

Arguements:
        --list1=LIST    List of elements
        --list2=LIST    List of elements

Options:
        -h, --help      Show the help message
"""


import re
import docopt
import logging


"""
To compare between two lists and return True even if
one element is same in both the lists.
"""


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
            for word_list2 in list2:
                if word_list1 == word_list2:
                    return True
        return False
    except TypeError:
        logger.error('Wrong input...\n')
        raise Exception('Input not in Expected Format.')


if __name__ == '__main__':

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        first_input_string = str(arguments['--list1'])
        # Splitting the contents by seperator into list
        input_list1 = filter(None, re.split("[\[\], ;']+", first_input_string))

        second_input_string = str(arguments['--list2'])
        # Splitting the contents by seperator into list
        input_list2 = filter(None, re.split("[\[\], ;']+", second_input_string))

        result = overlapping(input_list1, input_list2)
        logger.info("Overlapping Exists: {}\n".format(result))

    except docopt.DocoptExit as e:
        logger.error(e.message)
