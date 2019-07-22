#This script gets the traces converted through traceExpoter and arranges the nodes timestep wise and exports data into a text file

from xml.dom import minidom
import math
import fileinput

def main():	  
	#index_X = 0
	#index_Y = 0
	#time = ''
	#t  = ''
	prev_time = ''
	r = 800
	#prev_line = ''

	infile = open('Mobility-NV50.txt', 'r')
	outfile = open('Mobility-502.txt', 'w+')
	for line in infile:
		if '$ns_ at' in line:
			seprate = line.split(' at')
			s1 = seprate [1]
			s2 = s1.split('"$node_')
			t = s2[0]
			#time = str('Timestep: '+ t)
			if t != prev_time and 'switch OFF"' not in line and 'switch ON"' not in line:
				#print ('Time:' +t)
				#outfile.write(line)
				#line.split(' at')[0]	
				outfile.write('Timestep:'+t+'\n')
			#prev_time= t
			elif '$ns_ at' in line and 'switch OFF"' not in line and 'switch ON"' not in line:
					seprate2 = line.split(' setdest')
					s3 = seprate2[0]
					s_x_y = seprate2[1]
					nx = s_x_y[0:8]
					ny = s_x_y[9:16]
					print (nx)
					print (ny)
					print (s_x_y)
					s4 = line.split('"$')
					s5 = s4[1]
					nn= s5.split(' setdest')
					nns = nn[0]
					nns=str(nns)
					outfile.write(nns+': ('+nx+', '+ ny+')\n')
			prev_time= t
"""

			for line in infile:
				if '$ns_ at' in line:
					if 'switch OFF"' not in line and 'switch ON"' not in line:
						seprate2 = line.split(' setdest')
						s3 = seprate2[0]
				#	print (s3)		
						outfile.write(s3)
			prev_time= t"""
						#index_X = index_X+1
				#prev_time= t
		#prev_line = line


if __name__ == "__main__":
    main()
