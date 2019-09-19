from xml.dom import minidom
import math
import fileinput



def main():
	#version-2 -------
	r= 200.00
	infile = open('arranged_nodes.txt', 'r') 
	outfile = open('range_test.txt', 'w+')
	prev_line = ''
	for line in infile:                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
		if 'Timestep' in line and 'node_' not in line:
			outfile.write(line)
		if 'node_' in line:
			sec_nd = line.split(': (')
			sec_nd0 = sec_nd[0]
			sec_nd1 = sec_nd[1]
			sec_xy = sec_nd1.split(',')
			sec_x = sec_xy[0]
			sec_xf = float (sec_x)
			sec_y1 = sec_xy[1]
			sec_y = sec_y1[0:8]
			sec_yf = float (sec_y)
			print('nd0= '+sec_nd0)
			print('nd1= '+sec_nd1)
			#print (sec_xy[2])
			outfile.write(sec_nd0+','+sec_x+sec_y+ '******'+'\n')
			#break
			for line in infile:
				if 'node_' in line:
					sec_ndr = line.split(': (')
					sec_ndr0 = sec_ndr[0]
					sec_ndr1 = sec_ndr[1]
					sec_rxy = sec_ndr1.split(',')
					sec_rx = sec_rxy[0]
					sec_rxf = float (sec_rx)
					sec_ry1 = sec_rxy[1]
					sec_ry = sec_ry1[0:8]
					sec_ryf = float (sec_ry)
					dist = math.sqrt ((sec_rxf - sec_xf) ** 2 + (sec_ryf - sec_yf) ** 2)
					#if r >= dist and sec_ndr0 != sec_nd0:
					outfile.write(sec_ndr0+'tsssss,'+sec_rx+sec_ry+ '\n')
					break
		prev_line = line
	
"""
#version-1-----------
	r= 300
	infile = open('arrangedMobility.txt', 'r') 
	outfile = open('range_test.txt', 'w+')
	prev_line = ''
	for line in infile:                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
		if 'Timestep' in line and 'node_' not in line:
			outfile.write(line)
		if 'node_' in line:
			sec_nd = line.split(': (')
			sec_nd0 = sec_nd[0]
			sec_nd1 = sec_nd[1]
			sec_xy = sec_nd1.split(',')
			sec_x = sec_xy[0]
			sec_xf = float (sec_x)
			sec_y1 = sec_xy[1]
			sec_y = sec_y1[0:8]
			sec_yf = float (sec_y)
			print('nd0= '+sec_nd0)
			print('nd1= '+sec_nd1)
			print (sec_xy[2])
			outfile.write(sec_nd0+','+sec_x+sec_y+ '\n')
			#break
		#for line in infile:
			if 'node_' in line:
				sec_ndr = line.split(': (')
				sec_ndr0 = sec_ndr[0]
				sec_ndr1 = sec_ndr[1]
				sec_rxy = sec_ndr1.split(',')
				sec_rx = sec_rxy[0]
				sec_rxf = float (sec_rx)
				sec_ry1 = sec_rxy[1]
				sec_ry = sec_ry1[0:8]
				sec_ryf = float (sec_ry)
				dist = math.sqrt ((sec_rxf - sec_xf) ** 2 + (sec_ryf - sec_yf) ** 2)
				if dist <= r and 'sec_ndr0' != 'sec_nd0':
					outfile.write(sec_ndr0+'tsssss,'+sec_rx+sec_ry+sec_rxy[2] +'\n')
					#break
		prev_line = line
"""

if __name__ == "__main__":
    main()
