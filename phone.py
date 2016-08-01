"""Usage:      phone.py PHONE_NO...

Arguments:
    PHONE_NO       Specify the Phone number.

Options:
    -h, --help     Show this message.
"""


import docopt
import logging
import re
import sys


"""
Code for regex to parse the possible formats of phone number.
"""


# Setting up logger
logging.basicConfig(filename='phone.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s : '
                              '%(asctime)s:\t %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


class Phone(object):
    """
    Class to validate and parse phone number.
    """
    def __init__(self):
        self.result_dict = {}

    def parse_phone_number(self, phone_no):
        """
        Validate and parse the phone number.
        """
        pattern = r'^((emergency )?1\-)?\(?(?P<area_code>\d{3})\)?[\s.-]'\
                  r'(?P<trunk>\d{3})[\s.-](?P<phone_number>\d{4})[\s]?'\
                  r'((\-|x|( ext\. )|#)(?P<extension>\d{4}))?$'
        compiled_pattern = re.compile(pattern)
        re_match = re.match(compiled_pattern, phone_no)
        if re_match:
            self.result_dict['area_code'] = re_match.group('area_code')
            self.result_dict['trunk'] = re_match.group('trunk')
            self.result_dict['phone_number'] = re_match.group('phone_number')
            if re_match.group('extension') is not None:
                self.result_dict['extension'] = re_match.group('extension')
            return self.result_dict
        else:
            raise Exception("Invalid phone number format")


if __name__ == '__main__':

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        phone_no = ' '.join(arguments['PHONE_NO'])

        phone_obj = Phone()

        try:
            result_dict = phone_obj.parse_phone_number(phone_no)
            logger.info('{}\n'.format(result_dict))
        except Exception:
            logger.error('Invalid phone number format\n')

    except docopt.DocoptExit as e:
        logger.exception(e.message)
