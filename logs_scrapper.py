import re
import sys
from datetime import datetime
import os

if ((len(sys.argv) < 3)):
    print("Usage: python3 log_scrapper.py <absolute path to log file>")
    sys.exit(1)
#try:
#    iw_home = os.environ['IW_HOME']
#except KeyError as e:
#    print('Please source $IW_HOME/bin/env.sh before running this script')
#    sys.exit(-1)
#this script will display the time difference between the lines that took more than the specified threshold


MIN_THRESHOLD = int(sys.argv[2])
regCompile = r"\d\d:\d\d:\d\d"
filePath = sys.argv[1]

lastTime = None
lastLine = ""

with open(filePath, 'r') as f:
    #print("entered")
    for line in f:
        #print(line)
        regexp = re.search(regCompile, line)
        if regexp:
            currentTime = datetime.strptime(re.search(regCompile, line).group(0),"%H:%M:%S")
            #print(currentTime)
            if lastTime != None:
                duration = (currentTime - lastTime).seconds/60.0
                #print(duration)
                if duration >= MIN_THRESHOLD:
                    print(duration)
                    #print (line)
                    print ("#########################################################")
                    print (lastLine)
                    print (line)
            lastTime = currentTime
            lastLine = line
f.closed
