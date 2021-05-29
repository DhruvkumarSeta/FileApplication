# FileApplication

**Problem Statment**
Part -1: Create an application that will monitor a specific folder in a system. Once a new .txt (sample attached) file is created/dropped/copied to the folder, application should take the .txt file and create a password protected zip file using the UTC epoch time stamp for the file. The name of the zip file should be in the format of YYYY_MM_DD_hh_mm_ss_am/pm.zip (e.g. 2020_08_24_7_24_32_pm.zip)  ( ref: https://www.epochconverter.com/) The password is the UTC time epoch format.

 

The application should drop the zip file into a different folder named "todecode". it should create this folder when it is run first time or if the folder is not existing. It should delete any old file (if any exists) in the folder and keep only the new file.

 

Part-2:

Create application that monitors the "todecode" folder for any new zip file. When a new file is published, the application should be able to unzip the new zip file. The application should be able to identify the password using the file name. Extract file, perform PII filtering, put the contents in the new file (PII_filtered_<original_name>.txt) without any PII information in the file path if the text file has any in the file path. if NO PII in the file_path it to display as it is.

e.g.

field name to look for is "file_path" : "C:\Users\john\xyz" should be converted to "<d>:\\Users\<u>\xyz"
  
 **Sample Input File**
  
 "file_path":"c:\Users\ppph.hpp\AppData\Local\Microsoft\OneDrive\19.033.0218.0012\nl\FileSync.LocalizedResources.dll.mui"
"file_path": "d:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\IDE\Extensions\mlgen.exe"
"file_path": "e:\\Users\\tester1\AppData\Local\Microsoft\OneDrive\19.086.0502.0006\ga-IE\FileSync.LocalizedResources.dll"
  
  **Sample Output File**
  
 "file_path":"<d>:\Users\<u>\AppData\Local\Microsoft\OneDrive\19.033.0218.0012\nl\FileSync.LocalizedResources.dll.mui"
"file_path": "d:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\IDE\Extensions\mlgen.exe"
"file_path": "<d>:\\Users\\<u>\AppData\Local\Microsoft\OneDrive\19.086.0502.0006\ga-IE\FileSync.LocalizedResources.dll"
  
**Environment details**
  
  1. Pythoon 3.9
  2. pyzipper(pip install pyzipper)
  
  **Documentation**
  
  1.zipCrator.py
  
    This conatins solution of 1st bullet of problem statement. 
    It monitors D:/code folder by default(can be changed form ZipperApp.py file) which needs to be created manually. 
    It writes output in  D:/toDecode folder by default(can be changed form ZipperApp.py file)
  
  2.zipExtractor
  
    This contains solution of 2nd bullet of problem statement. 
    It Monitors D:/toDecode folder by default(can be changed form ZipperApp.py file).
    It'll delete all the data from D:/decode folder before writing output file.
  
  3. Module Folder
  
    contains all the modules which is used by both application
  
  4. Constant Folder
  
    contain file which is configuration as wwell as constant being used by both application
  
  5. sample log file([logfile.log](https://github.com/DhruvkumarSeta/FileApplication/files/6564441/logfile.log)) atteched which is created at home directory of code.
  

  
  
  
