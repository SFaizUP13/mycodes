#Latest version in proper working 07/11/2019
from xml.dom import minidom
import math
import fileinput

def main():

	 
	outfile = open('NV21_MaxTmobility_range200.txt', 'w+')
	time1 =''
	nodes = 0
	node_x = []
	node_y = []
	node_num = []
	r = 200
	dist = []
	with open('NV21_MaxTmobility_TimStepArrang_sorted.txt', 'r+') as infile:
		lines = infile.readlines()
		for i in range(0, len(lines)):
		    line = lines[i]
		    if 'Timestep:' in line:
		    	if nodes == 1:
		    		nodes = 0
		    		for xty in range(len(node_num)):
		    			#outfile.write(node_num[xty]+' ('+str(node_x[xty])+', '+str(node_y[xty])+') \n')
		    			outfile.write('Receiver:'+str(node_num[xty])+'\n')
		    			for xty2 in range(len(node_num)):
		    				dist.append(math.sqrt((node_x[xty2] - node_x[xty])**2 + (node_y[xty2] - node_y[xty])**2))
			    		#outfile.write(node_num[xty]+' ('+str(node_x[xty])+', '+str(node_y[xty])+') \n')
			    		for itr in range(len(node_num)):
			    			if xty != itr:
			    				if dist[itr] <= r:
			    					#distance = dist[itr]#outfile.write('In-range'+node_num[itr]+' ('+str(node_x[itr])+', '+str(node_y[itr])+') '+ '\n')
			    					outfile.write(str(node_num[itr])+'\n')
			    		del dist[:]
    				del node_x[:]
    				del node_y[:]
    				del node_num[:]
		    	time1 = line
		    	outfile.write(line)
		    	print (line)
		    if 'Timestep:' not in line:
		    	sec_nd = line.split(' ')
		    	nodeNum = int(sec_nd[0])
		    	#sec_nd0_1_2 = sec_nd0_1.split('node_(')
		    	#sec_nd0 = sec_nd0_1_2[1]
		    	#sec_nd1 = sec_nd[1]
		    	#sec_nd_xy = sec_nd[1]
		    	#sec_xy = sec_nd_xy.split(',')
		    	sec_x = sec_nd[1]
		    	#sec_xf = float (sec_x)
		    	sec_y = sec_nd[2]
		    	#sec_y = sec_y1[0:8]
		    	#sec_yf = float (sec_y)
		    	#print('nd0= '+sec_nd0)
		    	#print('nd1= '+sec_nd1)
		    	node_num.append(nodeNum)
		    	node_x.append(float(sec_x))
		    	node_y.append(float(sec_y))
		    	nodes = 1

		


if __name__ == "__main__":
    main()



#----------------------------------------------------------------------------------


#First ready version of the ditance calculation script from text file

from xml.dom import minidom
import math
import fileinput

def main():

	 
	outfile = open('range_test.txt', 'w+')
	time1 =''
	nodes = 0
	node_x = []
	node_y = []
	node_num = []
	r = 700
	dist = []
	with open('arranged_nodes.txt', 'r+') as infile:
		lines = infile.readlines()
		for i in range(0, len(lines)):
		    line = lines[i]
		    if 'Timestep' in line:
		    	if nodes == 1:
		    		nodes = 0
		    		for xty in range(len(node_num)):
		    			outfile.write(node_num[xty]+' ('+str(node_x[xty])+', '+str(node_y[xty])+') \n')
		    			for xty2 in range(len(node_num)):
		    				dist.append(math.sqrt((node_x[xty2] - node_x[xty])**2 + (node_y[xty2] - node_y[xty])**2))
			    		#outfile.write(node_num[xty]+' ('+str(node_x[xty])+', '+str(node_y[xty])+') \n')
			    		for itr in range(len(node_num)):
			    			if xty != itr:
			    				if dist[itr] <= r:
			    					outfile.write('   In-range'+node_num[itr]+' ('+str(node_x[itr])+', '+str(node_y[itr])+') '+str(dist[itr])+ '\n')
			    		del dist[:]
    				del node_x[:]
    				del node_y[:]
    				del node_num[:]
		    	time1 = line
		    	outfile.write(line)
		    	print (line)
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
		    	node_num.append(sec_nd0)
		    	node_x.append(float(sec_x))
		    	node_y.append(float(sec_y))
		    	nodes = 1

		


if __name__ == "__main__":
    main()
