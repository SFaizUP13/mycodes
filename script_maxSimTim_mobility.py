# This script traces the last time step of each node in SUMO traces and resets the nodes at 0.0 cordinats
# also writes the node number and its (last)Timestep in another file to be used for/to compare in NS3 traces
# This is the final version of this script todate 19/10/19   
from xml.dom import minidom
import math
import fileinput

def main():	  
	nod_index = 0
	line_num = []
	prev_line = ''
	out = ''
	k = 0
	array = [0]*50 #Value to be set equal to the number of nodes
	line_index =0
	j = 0
	with open ('NV50_600s.txt', 'r+') as infile:
		with open ('NV50_MaxTmobility_out.txt', 'w+') as outfile:
			with open ('NV50_mobility_time_out.txt', 'w+') as outtimefile:
				lines = infile.readlines()
				for itr in range(0, len(lines)):
					line = lines[itr]
					if ' setdest' in line: 
						splitline = line.split(') setdest')
						part1 = splitline[0]
						splitpart1 = part1.split (' ')
						tim = splitpart1[2]
						node = splitpart1[3]
				 		splitNode= node.split('$node_(')
				 		nNode = splitNode[1]
				 		nn= str(nNode)
				 		s = int(nn)					
				 		array[s] = k
				 	k = k+1
				for i in range(len(array)):
				 	print (str(array[i]))
				 	array.sort()
				for itr2 in range(0, len(lines)):
					line2 = lines[itr2]
					printline = array[j]
					if itr2 == printline: 
						splitline2 = line2.split(') setdest')
						part2 = splitline2[0]
						splitpart2 = part2.split (' ')
						tim2 = splitpart2[2]
						node2 = splitpart2[3]
				 	 	splitNode2= node2.split('$node_(')
				 	 	nNode2 = splitNode2[1]
				 	 	nod_numb= str(nNode2)
				 		print (itr2)
				 		#nxtline = itr2+1
				 		splitline3 = line2.split('est ')
				 		inserlinep1= splitline3[0]
				 		outfile.write(inserlinep1+'est 0000.00 0000.00 1000000000.0"'+'\n')
				 		outtimefile.write(tim2+' >>> '+ nNode2+'\n')
				 		j += 1
				 		#prev_line = line2
				 	else:
				 		outfile.write(line2)

					

		
if __name__ == "__main__":
    main()