"""Usage:      character_freq.py TEXT...

Arguments:
    TEXT  Message to be printed

Options:
    -h, --help       Show this message.
"""


import docopt
import logging


"""
To find the frequency of each character & store it in a dictionary.
"""


# Setting up logger
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(name)s :'
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


class CharFreq(object):
    def __init__(self):
        self.dict = {}

    def char_freq(self, string):
        """
        Function to calculate frequency of every character
        """
        try:
            for x in string:
                cnt = 0
                if x == ' ':
                    continue
                for y in string:
                    if x == y:
                        cnt += 1
                self.dict[x] = cnt  # Store the character & its frequency
            return self.dict
        except TypeError:
            logger.error('Wrong input...\n')
            raise Exception('Input not in Expected Format.')


if __name__ == '__main__':

    try:
        arguments = docopt.docopt(__doc__)

        logger.info('Started Program Execution...')

        string = ' '.join(arguments['TEXT'])

        char_freq_obj = CharFreq()
        result_dict = char_freq_obj.char_freq(string)
        logger.info('Character Frequency:\n{}'.format(result_dict))

    except docopt.DocoptExit as e:
        logger.exception(e)
