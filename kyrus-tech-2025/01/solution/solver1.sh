#!/bin/bash
# Incremental output
CURR="";
# Given Challenge Problem Input
inputFile="../puzzle.txt";
# Loop through the entire file line by line
while IFS= read -r line; do
	echo "Processing brute: $line";
	# Looping through the extended ASCII character set (0-255)
	for ((idx=0; idx<=255; idx++)); do
		# Check if the md5sum of the current output + the ith character of the ASCII character set matches the current line of the puzzle.txt file 
		if [ $(printf "$CURR\\x$(printf %x "$idx")" | md5sum | cut -d ' ' -f 1) = $line ]; then
			CURR+=$(printf "\\x$(printf %x "$idx")"); # A match was found! Append the correct ASCII character to the current output
			echo "Incremental output after appending($idx): $CURR";
			break; 
		fi
	done
done < "$inputFile"	
echo $CURR;