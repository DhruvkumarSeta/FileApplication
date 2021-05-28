import time

from Modules import stringopration as strop, zipmodule as zm, osoprations as osop,logmodule as lm
from Constant import ZipperApp as zac
logger=lm.getlogger()


while(True):
    zipfilename=osop.getzipfilename(zac.zipdestinationfolder)
    if not(zipfilename=="no zipfile found" or zipfilename=="More than 1 zipfiles found"):
        rawfiledata,textfilename=zm.extractzip(strop.getpassword(zipfilename,zac.timestringformat),zac.zipdestinationfolder+"/"+zipfilename)
        pipfilterddata=strop.pipfilter(rawfiledata.decode())
        osop.writenewfile(zac.zipdestinationfolder+"/"+zac.prefix+textfilename,pipfilterddata)
        osop.delfile(zac.zipdestinationfolder+"/"+zipfilename)
    else:
        logger.info(zipfilename)
        time.sleep(30)



