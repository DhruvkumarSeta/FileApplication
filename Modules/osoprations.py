
from os import path,listdir
import os
import shutil
from Modules import logmodule as lm
logger=lm.getlogger()


def fileexists(filepath):
    filelist=listdir(filepath)
    txt_files=[]
    for file in filelist:
        if file.endswith(".txt"):
            txt_files.append(file)
        else:
            continue
    if (len(txt_files) == 1):
        return txt_files[0]
    elif len(txt_files)>1:
        return "Only 1 .txt allowed"
    else:
        return "no .txt found we'll keep checking"

def dircreateexists(dirpath):
    if not path.exists(dirpath):
        logger.info("Creating directory")
        try:
            os.mkdir(dirpath)
        except Exception:
            logger.exception(Exception)
            logger.critical("Not bale to create"+ dirpath)
    else:
        for files in os.listdir(dirpath):
            opath = os.path.join(dirpath, files)
            try:
                shutil.rmtree(opath)
                logger.info("deleting "+opath)
            except OSError:
                logger.exception(OSError)
                os.remove(opath)
    return dirpath

def getzipfilename(zipfilepath):
    zipfilelist=listdir(zipfilepath)
    zipfiles=[]
    for file in zipfilelist:
        if file.endswith(".zip"):
            zipfiles.append(file)
        else:
            continue
    if len(zipfiles)==1:
        return zipfiles[0]
    elif len(zipfiles)==0:
        return "no zipfile found"
    else:
        return "More than 1 zipfiles found"

def delfile(file):
    try:
        os.remove(file)
        logger.info(file+" deleted")
    except Exception:
        logger.exception(Exception)
        logger.critical("Not able to delete "+file)

def writenewfile(filepath,data):
    try:
        with open(filepath,'w') as fp:
            fp.write(data)
        return True
    except Exception:
        logger.exception(Exception)
        logger.critical("writing failed at "+filepath)
        return False

