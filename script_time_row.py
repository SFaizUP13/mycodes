# This script gets all the vehicles and their coordinates from the xml file and writes them on a text file,
# each timestep per row
# Example: Time=8.00:<vid=5.0>(4300.23,1234.16),<vid=7.0>(4834.64,1782.19),<vid=8.0>(3711.76,1597.14),

from xml.dom import minidom
import math
xmldoc = minidom.parse("Trace.xml")

dis = float ('0.0')
r = float('600')
row = ''
row1 =''
row2 =''
fcd = xmldoc.getElementsByTagName("fcd-export")[0]
timesteps = fcd.getElementsByTagName("timestep")
file =open ("row.txt",'w+')
for timestep in timesteps:
	t = timestep.attributes['time'].value
	print('Timestep =' + t)
	row1 =  'Time='+ str(t) +':'
	file.write(row1)
	vehicles = timestep.getElementsByTagName("vehicle")
	for vehicle in vehicles:
		svid = float (vehicle.attributes['id'].value)
		x1 = float (vehicle.attributes['x'].value)
		y1 = float (vehicle.attributes['y'].value)
		#print '<'+ 'svid='+ svid, '>'+ '['+ svx, ','+ svy +']'
		print '<'+ 'Src='+ str(svid), '>'+ ':'+ '[' '('+str(x1), ','+ str(y1) +')'+ ']'
		
		row =  '<vid='+ str(svid)+">("+ str(x1)+","+str(y1)+'),'
		file.write(row)
	row2 = "\n"
	file.write(row2)
