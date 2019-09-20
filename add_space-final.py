# This script adds a blanck space in the row if it finds no digit on a specific column
from xml.dom import minidom
import math
import fileinput

def main():

	
	infile = open('abc.txt', 'r') 
	outfile = open('mobility-spacing.txt', 'w+')
	prev_line = ''
	for line in infile:                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
		if '$node_(' in line and 'setdest' not in line:
			outfile.write(line)
		# 	print(line)
		if '$ns_ at' in line:
			splite0 = line.split('$ns')
			sss = splite0[1]
			splite1 = line.split('est ')
			sec0 = str (splite1[0])
			sec1 = str (splite1[1])
			sec2 = str ( sec1.split(' ') )
			print ('sec1-'+sec1)
			sec3 = sec1[7]
			blnspc = str (sec3)			
			if  blnspc != ' ':
				sec11 = line.split('$ns_')
				sec11_0 = sec11[0]
				sec11_1 = sec11[1]
				sec_ts = sec11_1.split('est ')
				sec_tss = sec_ts[0]
				sectss = str (sec_tss)
				sec_ts1 = sec_ts[1]
				sec_ts1_2 = str (sec_ts1)
				sec_ts1_xyt = sec_ts1.split(' ')
				sec_x = sec_ts1_xyt[0]
				sec_y = sec_ts1_xyt[1]
				sec_t = sec_ts1_xyt[2]
				outfile.write('$ns_'+sectss+'est '+sec_x+'  '+sec_y+' '+sec_t)
			else:
				outfile.write (line)
				#outfile.write (sec_x+ '--'+ sec_y+ '#'+ sec_t)
		prev_line = line


if __name__ == "__main__":
    main()

"""
Version.2
-------------------------------------------------------------------
# This script adds a blanck space in the row if it finds no digit on a specific column
from xml.dom import minidom
import math
import fileinput

def main():

	
	infile = open('NV250_600s_Tex.txt', 'r') 
	outfile = open('250mobility-spacing.txt', 'w+')
	prev_line = ''
	for line in infile:                                #<<<<<<<<<<<<<S-1--- This section is for export nodes timestep wise 
		if '$node_(' in line and 'setdest' not in line:
			outfile.write(line)
		# 	print(line)
		if '$ns_ at' in line:
			splite0 = line.split('$ns')
			sss = splite0[1]
			splite1 = sss.split('est ')
			sec0 = str (splite1[0])
			sec1 =  splite1[1]
			sec2 = str ( sec1.split(' ') )
			print ('sec1-'+ sec1)
			sec3 = sec1[7]
			blnspc = str (sec3)			
			if  blnspc != ' ':
				sec11 = line.split('$ns_')
				sec11_0 = sec11[0]
				sec11_1 = sec11[1]
				sec_ts = sec11_1.split('est ')
				sec_tss = sec_ts[0]
				sectss = str (sec_tss)
				sec_ts1 = sec_ts[1]
				sec_ts1_2 = str (sec_ts1)
				sec_ts1_xyt = sec_ts1.split(' ')
				sec_x = sec_ts1_xyt[0]
				sec_y = sec_ts1_xyt[1]
				sec_t = sec_ts1_xyt[2]
				print('x= '+sec_x)
				print('y= '+sec_y)
				outfile.write('$ns_'+sectss+'est '+sec_x+'  '+sec_y+'  '+sec_t)
			else:
				outfile.write (line)
		prev_line = line


if __name__ == "__main__":
    main()"""
