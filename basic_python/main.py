# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Root logger
import logging
import traceback
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
#
# # import intermediate_python.loggingHelper
#
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")
#
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)

try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("The error msg is %s", traceback.format_exc())

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over 2KB, and keep backup logs app.log1, app.log2 etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# rotating handler
timedHandler = TimedRotatingFileHandler('timed_app.log', when='s', interval=5, backupCount=5)
logger.addHandler(timedHandler)

for i in range(6):
    logger.info("Hello World!")
