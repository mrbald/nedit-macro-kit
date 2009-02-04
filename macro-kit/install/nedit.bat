@setlocal enableextensions & C:\python25\python.exe -x "%~f0" %* & goto :EOF

########################################################
# drag and drop file to edit then with NEdit on windows/cygwin
########################################################

# change that to something which can call nedit with file argument:
startNedit = "neditAux.bat"

import sys
sys.path+=[r"C:\frankhelpers"]
from common import *

def unixStyle(windowsPath):
	res = re.subn(r"\\","/",os.path.abspath(windowsPath))[0]
	return "/cygdrive/%s"%(res[0].lower())+res[2:]
files = map(lambda x: unixStyle(x), sys.argv[1:])

neditbat = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"neditAux.bat")
cmd=[neditbat]+files
subprocess.call(cmd)
