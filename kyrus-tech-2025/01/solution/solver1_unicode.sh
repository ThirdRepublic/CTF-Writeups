#!/bin/bash
# Attempt to fix using awk replacement.  Dealing with encoding properly prior to hashing 
# Not successful... Moving on to write in python3
CURR=""
inputFile="../puzzle.txt"
skip=1
while IFS= read -r line; do
	echo "Processing: $line -------------------------------";
	echo $CURR;
	if (( skip > 0 )); then
		((skip--))
		echo "Skipped first line. no code points for empty string";
		continue
	fi
	for unicode in $(seq 0 114111); do
		#awk -v out=$unicode 'BEGIN { printf "%s%c ", $CURR, out }'
		#awk -v out=$unicode 'BEGIN { printf "%s%c", $CURR, out }' | md5sum | cut -d ' ' -f 1
		# printf "$CURR\\x$(printf %x "$unicode")"	
		#test=$(awk -v out=$unicode 'BEGIN { printf "%s%c", $CURR, out }' | md5sum | cut -d ' ' -f 1)
		test=$(printf "$CURR\\x$(printf %x "$unicode")" | md5sum | cut -d ' ' -f 1)
		if [ $test = $line ]; then
			#CURR+=$(awk -v out=$unicode 'BEGIN { printf "%s%c", $CURR, out }');
			# Not sure why it is not printing ...
			CURR+=$(printf "\\x$(printf %x "$unicode")");
			#awk 'BEGIN { printf "%s ", $CURR }' 
			#printf "$CURR\\x$(printf %x "$unicode")"
			break;
		fi
	done
done < "$inputFile"
echo $CURR;