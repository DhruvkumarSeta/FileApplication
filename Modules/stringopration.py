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
            line=line.replace(drive,"<d>:")
            logger.info("drive letter found and replaced")
        except Exception as e:
            logger.exception(e)
            logger.info("drive letter not found")
        try:
            usernamepart = userregxc1.search(line).group()
            user=userregxc2.search(usernamepart[5:]).group()
            line=line.replace(user,"<u>")
            logger.info("Username found and replaced")
        except Exception as e:
            logger.exception(e)
            logger.info("Username not found")
        newline.append(line)
    return "\r".join(newline)