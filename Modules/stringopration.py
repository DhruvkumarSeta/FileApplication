from Modules import timeformat as tf,logmodule as lm
import re
from Constant import ZipperApp as zac
logger=lm.getlogger()

def getpassword(filename,timestringfromat):
    return tf.stringtoepoch(filename[0:-4], timestringfromat)

def pipfilter(rawdata):
    driveregxc=re.compile(zac.driveregx)
    userregxc1=re.compile(zac.userregx1, re.IGNORECASE)
    userregxc2=re.compile(zac.userregx2)
    filelines=str(rawdata).split("\r\n")
    newline=[]
    for line in filelines:
        try:
            drive = driveregxc.search(line).group()
            usernamepart = userregxc1.search(line).group()
            user=userregxc2.search(usernamepart[5:]).group()
            newline.append(line.replace(drive, "<d>:").replace(user,"<u>"))
        except Exception as e:
            logger.exception(e)
            newline.append(line)
    return "\r".join(newline)