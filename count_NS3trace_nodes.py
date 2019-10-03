from xml.dom import minidom
import math
import fileinput

def main():

	prev_line = ''
	count = 0
	cnt = ''
	with open('test_pyout.txt', 'r') as infile: 
		with open('node_count_NS3.txt', 'w+') as outfile:
			lines = infile.readlines()
			for itr in range(0, len(lines)):
				line = lines[itr]		      
				if 'Timestep:' in line and 'Node' not in line:
					print (line)
					outfile.write(line)
				if 'Node' in line and 'Inrange' not in line:
					outfile.write(line)
					outfile.write(cnt+'\n')
					print (line)
					count = 0
		 		if 'Inrange' in line and 'Timestep' not in line:
		 			count += 1
		 			cnt = str (count)
 					#outfile.write(cnt+'\n')		 	


if __name__ == "__main__":
    main()