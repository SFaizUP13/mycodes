#This script takes input the NS3 traces (saperated in transmit and receive files), compares SA of both files, 
#converts SA into node number and returnes a file as receiving output file 

from xml.dom import minidom
import math
import fileinput

def main():
       # 
    prv_time = 0
    with open ('compare_out1.txt', 'w+') as output:
		with open('split-rcvout_rducDecml.txt', 'r') as rcvfile:
			rcvlines = rcvfile.readlines()
			for itr1 in range(0, len(rcvlines)):
				cmpr1 = rcvlines[itr1]
				# cmpr1_1= rcvlines[itr1-1]
				# cmpr1_1split= cmpr1_1.split(' ')
				# t_1= cmpr1_1split[0]
				rcv_split = cmpr1.split(' ')
				rcv_time = rcv_split[0]
				rcvNod = rcv_split[1]
				SA1 = rcv_split[2]
				print (rcv_time)
				with open('split-TDout_rducDecml.txt', 'r') as TDfile:	
					TDlines = TDfile.readlines()
					for itr2 in range(0, len(TDlines)):
						cmpr2 = TDlines[itr2]
						td_split = cmpr2.split(' ')
						td_time = td_split[0]
						td_Nod = td_split[1]
						SA2 = td_split[2]
						if rcv_time == td_time and SA1 ==SA2:
							output.write(rcv_time+' '+rcvNod+' '+td_Nod +'\n')
				prv_time = rcv_time



if __name__ == "__main__":
    main()