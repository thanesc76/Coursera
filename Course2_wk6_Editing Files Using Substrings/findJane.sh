#!/bin/bash
> oldFiles.txt  # create file
files=$(grep ' jane ' ../data/list.txt | cut -d' ' -f3)
for name in $files; do
  # echo "..$name"
  #if test -e "..$name";
  #  then echo $name >> oldFiles.txt;
  #  else echo "$name does not exist."; 
  #fi
  if test -e "..$name"; then echo $name >> oldFiles.txt; fi
  #if test -e "..$name"; then echo "..$name" >> oldFiles.txt; fi
done