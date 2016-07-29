"""
Usage:      encode_decode.py --choice=N <number_of_shifts> TEXT...

Arguments:
        TEXT    The string for encoding / decoding.

Options:
        -h, --help          Show this message.

        --choice=N          Choice to Encode or Decode the string [1 | 2]

        number_of_shifts    The number of shifts by which the string
                            is to be encoded or decoded.
"""


import sys
import logging
import docopt


"""
To encode & decode a string by shifting it with specied no. of places.
"""


TOTAL_ALPHABETS_COUNT = 26
FIRST_SMALL_LETTER_UNICODE = 97
FIRST_CAPITAL_LETTER_UNICODE = 65
FIRST_SMALL_LETTER_LATIN = 'a'
FIRST_CAPITAL_LETTER_LATIN = 'A'


# Setting up logger
logging.basicConfig(filename='encode_decode.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s: '
                              '%(asctime)s:\n %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


class Choice(object):
    """
    Storing the choices for encode and decode
    """
    ENCODE = 1
    DECODE = 2


class Coder(object):
    """
    Encoding & decoding the string by shifting it by 'n' number of places.
    """
    def __init__(self, string_input, number_of_shifts):
        """
        Initialising the instance variables.
        """
        try:
            self.string_input = string_input
            self.number_of_shifts = int(number_of_shifts)
        except Exception:
            logger.error('Wrong input...Not a valid Integer Number...\n')
            raise Exception('Input not in Expected Format.')

    def decode(self):
        """
        Method to decode the string by shifting it to right by n places.
        """
        result_string = ''
        for character in self.string_input:
            if ord(character) >= FIRST_SMALL_LETTER_UNICODE:
                # Characters are shifted by number_of_shifts to the right.
                # By adding the number_of_shifts to the unicode values.
                result_string += chr((((ord(character) -
                                        ord(FIRST_SMALL_LETTER_LATIN)) +
                                       self.number_of_shifts) %
                                      TOTAL_ALPHABETS_COUNT) +
                                     ord(FIRST_SMALL_LETTER_LATIN))

            elif ord(character) >= FIRST_CAPITAL_LETTER_UNICODE:
                result_string += chr((((ord(character) -
                                        ord(FIRST_CAPITAL_LETTER_LATIN)) +
                                       self.number_of_shifts) %
                                      TOTAL_ALPHABETS_COUNT) +
                                     ord(FIRST_CAPITAL_LETTER_LATIN))
            else:
                result_string += character

        return result_string

    def encode(self):
        """
        Method to encode the string by shifting it to left by n places.
        """
        result_string = ''
        for character in self.string_input:
            if ord(character) >= FIRST_SMALL_LETTER_UNICODE:
                # Characters are shifted by number_of_shifts to the left.
                # By subtracting the number_of_shifts from the unicode values.
                result_string += chr((((ord(character) -
                                        ord(FIRST_SMALL_LETTER_LATIN)) -
                                       self.number_of_shifts) %
                                      TOTAL_ALPHABETS_COUNT) +
                                     ord(FIRST_SMALL_LETTER_LATIN))

            elif ord(character) >= FIRST_CAPITAL_LETTER_UNICODE:
                result_string += chr((((ord(character) -
                                        ord(FIRST_CAPITAL_LETTER_LATIN)) -
                                       self.number_of_shifts) %
                                      TOTAL_ALPHABETS_COUNT) +
                                     ord(FIRST_CAPITAL_LETTER_LATIN))
            else:
                result_string += character

        return result_string


def is_valid_choice(choice):
    """
    Check if choice provided is valid or not.
    """
    return (choice in [Choice().ENCODE, Choice().DECODE])


if __name__ == "__main__":

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)
        number_of_shifts = 0

        # Access the choice and number_of_shifts.
        try:
            choice = int(arguments['--choice'])
            number_of_shifts = int(arguments['<number_of_shifts>'])
            number_of_shifts %= TOTAL_ALPHABETS_COUNT
        except ValueError:
            logger.error('Wrong input...Not a valid Integer Number...\n')
            sys.exit(0)

        # Accessing the string.
        string_input = ' '.join(arguments['TEXT'])

        # Create object of class Coder
        coder = Coder(string_input, number_of_shifts)

        # Call respective method based on choice
        if is_valid_choice(choice):
            if choice == Choice().ENCODE:
                result_string = coder.encode()
            elif choice == Choice().DECODE:
                result_string = coder.decode()
        else:
            logger.error('Invalid choice provided...\n')
            sys.exit(0)

        logger.info("Output String: {}\n".format(result_string))

    except docopt.DocoptExit as e:
        logger.exception(e.message)
