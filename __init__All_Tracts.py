#  Logger for writing outputs to .log file.
#  .info prints to standard output + .log file
#  .debug prints to only .log file

import logging
import time
import sys

logdatetime = time.strftime("%m%d")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.handlers =[]

fh = logging.FileHandler('./' + logdatetime + '_All_Tracts.log', mode='a')
fh.setLevel(logging.DEBUG)

sh = logging.StreamHandler(stream=sys.stdout)
sh.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)


