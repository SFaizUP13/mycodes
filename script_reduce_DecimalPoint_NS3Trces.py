from xml.dom import minidom
import math
import fileinput

def main():

	with open ('split-TDout_rducDecml.txt', 'w+') as output:
		with open('split-TDout_addDecml.txt', 'r') as infile:
			lines = infile.readlines()
			for itr1 in range(0, len(lines)):
				cmpr1 = lines[itr1]
				split1 = cmpr1.split(' ')
				node = split1[1]
				SA = split1[2]
				td_time = split1[0]
				time1= td_time.split('.')
				timeBD = time1[0]
				time11= time1[1]
				time12 = time11[0]
				td_nodes = split1[1]
				td_SA = split1[2]
				print (time12+'\n')
				output.write(timeBD+'.'+time12+' '+node+' '+SA)


if __name__ == "__main__":
    main()