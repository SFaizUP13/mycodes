#This script compares the maximum simulation time of each node (output file (time file) of script_maxSimTime_mobility) with the 
# transmit/received file of NS3 (files after the split and reduced decimal) and gives output as transmit/reaceived which we treat
# as our actual transmit/received files for further process 
from xml.dom import minidom
import math
import fileinput

def main():
       # 
    array=[0]*50 #Value to be set equal to the number of nodes
    prv_time = 0
    with open ('NV50_compare_maxSinTime_transmit.txt', 'w+') as output:
		with open('NV50_mobility_time_out.txt', 'r') as timefile:	
			timelines = timefile.readlines()
			for itr2 in range(0, len(timelines)):
				timeline = timelines[itr2]
				time_split = timeline.split(' >>> ')
				max_time = time_split[0]
				maxtime_Nod = time_split[1]
				print (max_time+' > '+maxtime_Nod)
				maxtime_Nod_int = int(maxtime_Nod)
				array[maxtime_Nod_int]= max_time
				print (str(array)+str(maxtime_Nod_int))
				#output.write(rcv_time+' '+rcvnodnum+'\n')
			with open('NV50_600s_TD_rducDecml.txt', 'r') as rcvfile:
				rcvlines = rcvfile.readlines()
				for itr1 in range(0, len(rcvlines)):
					rcvline = rcvlines[itr1]
					rcvline_split = rcvline.split(' ')
					rcv_time = rcvline_split[0]
					rcvNod = rcvline_split[1]
					rcvNode = rcvNod.split('/NodeList/')
					rcvnodnum = rcvNode[1]
					rcvnodnum_int = int(rcvnodnum)
					time_in_array = array[rcvnodnum_int]
					time_in_array_int= float(time_in_array)
					print (time_in_array)
					rcv_time_int = float(rcv_time)
					if rcv_time_int <= time_in_array_int:
						output.write(rcvline)



if __name__ == "__main__":
    main()







"""
from xml.dom import minidom
import math
import fileinput

def main():
       # 
    array=[]
    prv_time = 0
    with open ('compare_maxSinTime_receivd.txt', 'w+') as output:
		with open('NV10_mobility_time_out.txt', 'r') as timefile:	
			timelines = timefile.readlines()
			for itr2 in range(0, len(timelines)):
				timeline = timelines[itr2]
				time_split = timeline.split(' >>> ')
				max_time = time_split[0]
				maxtime_Nod = time_split[1]
				print (max_time+' > '+maxtime_Nod)
				#output.write(rcv_time+' '+rcvnodnum+'/n')
				with open('NV10-receivd_rducDecml.txt', 'r') as rcvfile:
					rcvlines = rcvfile.readlines()
					for itr1 in range(0, len(rcvlines)):
						rcvline = rcvlines[itr1]
						rcvline_split = rcvline.split(' ')
						rcv_time = rcvline_split[0]
						rcvNod = rcvline_split[1]
						rcvNode = rcvNod.split('/NodeList/')
						rcvnodnum = rcvNode[1]
						#print (rcv_time+max_time+'>>>'+rcvnodnum+maxtime_Nod+'/n')
						if rcvnodnum == maxtime_Nod and rcv_time >= max_time:
							#output.write(str(rcv_time)+' '+str(rcvNod)+'/n')
							pass#write=rcvline
							#output.write(rcvline)
						else:
							write=rcvline
							output.write(write)
							#output.write(write+'>>>'+rcv_time+'-'+rcvnodnum+'   '+max_time+'-'+maxtime_Nod+ '/n')
			prv_time = rcv_time



if __name__ == "__main__":
    main()
"""
