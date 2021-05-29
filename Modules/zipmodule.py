import pyzipper
from Modules import logmodule as lm
logger=lm.getlogger()

def createzip(zippassword,zipfilename,filepath,filename,destination):
    try:
        with pyzipper.AESZipFile(destination+"/"+zipfilename+".zip", 'w', compression=pyzipper.ZIP_LZMA) as zf:
            zf.setpassword(bytes(str(zippassword),'utf-8'))
            zf.setencryption(pyzipper.WZ_AES, nbits=128)
            zf.write(filepath+filename, arcname=filename, compresslevel=9)
        return True
    except Exception as e:
        logger.exception(e)
    return False

def extractzip(zippassword,zipfilename):
    try:
        with pyzipper.AESZipFile(zipfilename) as zf:
            return (zf.read(zf.filelist[0].filename,bytes(str(zippassword),'utf-8')),zf.filelist[0].filename,True)
    except Exception:
        logger.exception(Exception)
        logger.info(zipfilename+" extract failed")
        return ("","file extract failed",False)


