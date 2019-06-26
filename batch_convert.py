#!/usr/bin/env python3

import os
import glob

path = './'
files = [f for f in glob.glob(path + "**/*.md", recursive=True)]
for f in files:
    cmd = 'markdown2 ' + f + ' > ' + f[0:len(f)-2] + 'html'
    #print(cmd)
    os.system(cmd)
