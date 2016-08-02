"""Usage:      character_freq.py TEXT...

Arguments:
    TEXT  Message to be printed

Options:
    -h, --help       Show this message.
"""


import docopt
import logging
import string


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
        self.result_dict = {}
        self.alphabet_dict = {}

    def char_freq(self, input_string):
        """
        Function to calculate frequency of every character
        """
        try:
            # Set the frequency for each character in input_string
            for character in input_string:
                if character in self.alphabet_dict:
                    self.alphabet_dict[character] = \
                            self.alphabet_dict.get(character) + 1
                else:
                    self.alphabet_dict[character] = 1
            return self.alphabet_dict
        except TypeError:
            logger.error('Wrong input...\n')
            raise Exception('Input not in Expected Format.')


if __name__ == '__main__':

    try:
        arguments = docopt.docopt(__doc__)

        logger.info('Started Program Execution...')

        # Access any string(even if separated by space)
        input_string = ' '.join(arguments['TEXT'])

        char_freq_obj = CharFreq()
        result_dict = char_freq_obj.char_freq(input_string)
        logger.info('Character Frequency:\n{}'.format(result_dict))

    except docopt.DocoptExit as e:
        logger.exception(e)
