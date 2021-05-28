import time
from datetime import datetime
from Modules import logmodule as lm
logger=lm.getlogger()

def getepoch():
    return int(time.time())

def getformattedtime(epoch,formatstring):
    return time.strftime(formatstring,time.gmtime(epoch))

def stringtoepoch(timestring,timestringformat):
    utc_time = datetime.strptime(timestring, timestringformat)
    return int((utc_time - datetime(1970, 1, 1)).total_seconds())
