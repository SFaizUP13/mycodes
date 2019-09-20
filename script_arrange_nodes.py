#This script gets the traces converted through traceExpoter and arranges the nodes timestep wise and exports data into a text file

from xml.dom import minidom
import math
import fileinput

def main():	  
	prev_time = ''
	r = 800
	#prev_line = ''

	infile = open('mobility-spacing.txt', 'r')
	outfile = open('arrangedMobility.txt', 'w+')
	for line in infile:
		if '$ns_ at' in line:
			seprate = line.split(' at')
			s1 = seprate [1]
			s2 = s1.split('"$node_')
			t = s2[0]
			if t != prev_time:	
				outfile.write('Timestep:'+t+'\n')
			#prev_time= t
			if '$ns_ at' in line:
				seprate2 = line.split('setdest')
				s3 = seprate2[0]
				print (s3) # test print -------
				s_x_y = seprate2[1]
				nx = s_x_y[0:8]
				ny = s_x_y[8:16]
				print (nx)
				print (ny)
				print (s_x_y)  #test print -----------
				s4 = line.split('"$')
				s5 = s4[1]
				nn= s5.split('setdest')
				nns = nn[0]
				nns=str(nns)
				print (nns)
				outfile.write(nns+': ('+nx+' ,'+ny+')\n')
			prev_time= t


if __name__ == "__main__":
    main()
