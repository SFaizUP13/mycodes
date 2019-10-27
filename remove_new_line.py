from xml.dom import minidom
import math
import fileinput

def main():

	with open('NV10_RcvNS3_count.txt', 'r') as infile:
		with open('NV10_RcvNS3_count_removnewLine.txt','w+') as output:
			lines = infile.readlines()
			for itr in range(0, len(lines)):
				line = lines[itr]
				if 'Timestep:' in line:
					output.write(line)	
				if 'sender:' in line and 'Timestep:' not in line:
					line1 = line.replace('\n',',')
					output.write(line1)
				if 'count:' in line:
					output.write(line)
				if 'None' in line and 'Timestep:' not in line:# and 'sender' not in line:
					#line2 = line.replace('\n',',')
					output.write(line)




if __name__ == "__main__":
    main()