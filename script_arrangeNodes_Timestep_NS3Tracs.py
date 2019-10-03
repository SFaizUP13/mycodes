# This script gets input from output file of the comare_transmit_receive files and arranges the 
# nodes timestep wise according to its range(transmit/receive data)

from xml.dom import minidom
import math
import fileinput

def main():

	prv_time= ''
	sm_tdnode=''
	prnt_rcvnod =''
	with open ('test_pyout.txt', 'w+') as output:
		with open('compare_out1.txt', 'r+') as infile:
			lines = infile.readlines()
			for itr1 in range(0, len(lines)):
				prv_line = lines[itr1-1]
				prv_split = prv_line.split(' /')
				prv_time= prv_split[0]
				prv_rcvnode = prv_split[1]
				prv_tdnode = prv_split[2]
				line = lines[itr1]
				split1 = line.split(' /')
				time = split1[0]
				rcvnode = split1[1]
				tdnode = split1[2]
				if time != prv_time:
					output.write('Timestep:'+time+'\n')
				if tdnode != sm_tdnode:
					output.write(tdnode)
				sm_tdnode=tdnode
				for itr2 in range(0, len(lines)):
					ndline= lines[itr2]
					nd_split= ndline.split(' /')
					time2 = nd_split[0]
					rcvnode2= nd_split[1]
					tdnode2 = nd_split[2]
					if time2 == time:
						if tdnode2 == tdnode and rcvnode!= prnt_rcvnod:
							output.write('Inrange: '+rcvnode+'\n')
							prnt_rcvnod=rcvnode




if __name__ == "__main__":
    main()