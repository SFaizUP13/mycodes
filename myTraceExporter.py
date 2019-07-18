#This script gets the traces convert through traceExpoter and adds our required perameters in it and exports data into a text file

from xml.dom import minidom
import math
import fileinput
#xmldoc = minidom.parse("Trace.xml")


# if '$node_(0)' in open('MobilityFile.txt').read():
#     print("true")	
# else:
# 	print("no match")
def main():	  
	index_X = 0
	index_Y = 0
	index_Z = 0
	filedata =0
	prev_line = ''

	infile = open('Mobility-NV100.txt', 'r')
	outfile = open('mobility-v100.txt', 'w+')
	for line in infile:
		if '$node_('+str(index_X)+') set X_' in line:
			#line = line.replace('$node_('+str(index)+')', 'a')
			newx = '$node_('+str(index_X)+') set X_ 0000.00'
			switchoff = '$ns_ at 0.0 "$node_('+str(index_X) +') switch OFF" ;# set_X,Y,Z'	
			index_X = index_X+1
			outfile.write(switchoff+'\n')
			outfile.write(newx)
			outfile.write('\n')
		elif '$node_('+str(index_Y)+') set Y_' in line:
			#line = line.replace('$node_('+str(index)+')', 'a')
			newx = '$node_('+str(index_Y)+') set Y_ 0000.00'
			index_Y = index_Y+1					
			outfile.write(newx)
			outfile.write('\n')
		elif '0.00"' in line and 'set Z_ 0' in prev_line:
			line = line.replace('0.00"', '1000000000.0" ;# init_node')
			outfile.write(line)			
			outfile.write(line.split(' "')[0] + str(1) + ' "$node_('+str(index_Y-1)+') switch ON" ;# inside'+'\n')
		else:
			outfile.write(line)
		prev_line = line
		
if __name__ == "__main__":
    main()


#1000000000.000000" ;# init_node
#$ns_ at 0.01 "$node_(0) switch ON" ;# inside

