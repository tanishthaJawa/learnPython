import logging

# logger = logging.getLogger(__name__)
#
# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')
#
# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
#
# formatter = logging.Formatter('%(names -%(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
#
# logger.addHandler(stream_h)
# logger.addHandler(file_h)
#
# logger.warning('This is a warning')
# logger.error('This is an error')

# logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
