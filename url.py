"""
Usage:      url.py <url>

Options:
        -h, --help      Show this message.

        url             Specify the url.
"""


import docopt
import logging
import re


"""
This code validates the given url with respected to a specified format.
"""


# Setting up logger
logging.basicConfig(filename='url.log', level=logging.INFO,
                    format='%(levelname)s: %(name)s : '
                           '%(asctime)s:\t %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s: '
                              '%(asctime)s:\n %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)


def is_valid_url(url):
    """
    Validate the url against a provided regular expression.
    """
    pattern = r'^(ftp|https?)://[a-z]+\.emtecinc\.com(:\d{4})?/v\d\.\d' \
        r'/api/[\w/\-\.]*$'
    compiled_pattern = re.compile(pattern)
    return bool(re.match(compiled_pattern, url))


if __name__ == "__main__":

    logger.info('Started Program Execution...')
    logger.addHandler(ch)

    try:
        arguments = docopt.docopt(__doc__)

        # Access the url.
        url = str(arguments['<url>'])

        if is_valid_url(url):
            logger.info("Valid Url\n")
        else:
            logger.info("Invalid Url\n")

    except docopt.DocoptExit as e:
        logger.exception(e.message)
