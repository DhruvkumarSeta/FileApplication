import time
from Modules import timeformat as tf, zipmodule as zm, osoprations as osop,logmodule as lm
from Constant import ZipperApp as zac
logger = lm.getlogger()


while(True):
    textfilename=osop.fileexists(zac.textfilepath)
    if not (textfilename=="Only 1 .txt allowed" or textfilename=="no .txt found we'll keep checking"):
        logger.info(textfilename+" found")
        epochtimestamp=tf.getepoch()
        zipname=tf.getformattedtime(epochtimestamp,zac.timestringformat)
        if (zm.createzip(epochtimestamp,zipname,zac.textfilepath,textfilename,osop.dircreateexists(zac.zipdestinationfolder))):
            logger.info(zipname + " created")
            osop.delfile(zac.textfilepath + textfilename)
        else:
            logger.critical("zip creation failed")
    else:
        logger.info(textfilename)
        time.sleep(30)
