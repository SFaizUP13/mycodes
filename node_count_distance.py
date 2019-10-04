from xml.dom import minidom
import math
import fileinput

def main():

	prev_line = ''
	count = 0
	check = 0
	with open('NV50_rangeFile.txt', 'r') as infile: 
		with open('node_count_rangeNV50.txt', 'w+') as outfile:
			lines = infile.readlines()
			for itr in range(0, len(lines)):
				line = lines[itr]		                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
				if 'Timestep:' in line and 'node_' not in line:
					print (line)
					if check ==1:
						outfile.write(str(count)+'\n')
						check = 0
					outfile.write(line)
				if 'node_' in line and 'In-rangenode' not in line:
					if check ==1:
						outfile.write(str(count)+'\n')
						check = 0
					outfile.write(line)
					count = 0		
			 	if 'In-rangenode' in line and 'Timestep' not in line:
			 		count += 1
			 		check = 1
			if check == 1:
				outfile.write(str(count))
				check=0
	 						 	


if __name__ == "__main__":
    main()
