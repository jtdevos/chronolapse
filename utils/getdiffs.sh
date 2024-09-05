#!/bin/bash

# Define the directory to get files from
directory=$1
if [ ! -d  "$directory" ] 
then
    echo directory does not exist && return 1
fi

# Populate the list of files by using ls in the specified directory
files=($(ls -d "$directory"/*))

# Get the length of the file list
length=${#files[@]}

# Iterate over the list, but stop before the last file to avoid out-of-bound error
for ((i=0; i<$length-1; i++)); do
  file1="${files[$i]}"
  file2="${files[$i+1]}"
  
  # Call the script with the nth and n+1th file as arguments
#   ./your_script.sh "$file1" "$file2"
    python main.py "$file1" "$file2"
done
