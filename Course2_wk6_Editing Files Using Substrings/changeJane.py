#!/usr/bin/env python3
import sys
import subprocess
import os

with open(sys.argv[1]) as file:
  lines = file.readlines()
  for line in lines:  
    # print(line.strip().replace('jane','jdoe')) 
    subprocess.run(['mv',line.strip(),line.strip().replace('jane','jdoe')])
  file.close()
