import os.path
import re

def read_org(file, header = True):
    ans = []
    with open(os.path.expanduser(file), "r") as f:
        for line in f:
            m = re.match("^\| ~.*", line)
            if m:
                tmp = line.split("|")[1:-1]
                ans.append(list(map(str.strip, tmp)))

    return ans                
