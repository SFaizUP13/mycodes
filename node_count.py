#This script counts the number of nodes in each timestep

from xml.dom import minidom
import math
import fileinput

def main():

	prev_line = ''
	count = 0
	cnt = ''
	infile = open('arrangedMobility.txt', 'r') 
	outfile = open('node_count.txt', 'w+')
	for line in infile:		                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
		if 'Timestep:' in line:
			outfile.write(cnt+'\n')
			if line != prev_line:
				outfile.write(line)
				print (line)
			count = 0
	 	if 'node_' in line:
	 		count += 1
	 		cnt = str (count)
	 		#outfile.write(cnt+'\n')
		prev_line= line
	outfile.write(cnt+'\n')	


if __name__ == "__main__":
    main()
