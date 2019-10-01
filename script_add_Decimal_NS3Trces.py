from xml.dom import minidom
import math
import fileinput

def main():

	with open ('split-TDout_addDecml.txt', 'w+') as output:
		with open('split-TDout.txt', 'r') as infile:
			lines = infile.readlines()
			for itr1 in range(0, len(lines)):
				line = lines[itr1]
				if '.' not in line:
					split1= line.split(' /N')
					tm = str (split1[0])
					nd = str (split1[1])
					output.write(tm+'.00 /N'+nd)
					print (tm+'.00 /N'+nd)
				else:
					output.write(line)
					print (line)



if __name__ == "__main__":
    main()