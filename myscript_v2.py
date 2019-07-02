#This script gets the traces from xml file and calculates the distance between them and exports data into a text file

from xml.dom import minidom
import math
xmldoc = minidom.parse("Trace.xml")


r = float('600')
row = ''
row1 =''
row2 =''
fcd = xmldoc.getElementsByTagName("fcd-export")[0]
timesteps = fcd.getElementsByTagName("timestep")
file =open ("output.txt",'w+')
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
		print '<'+ 'Src='+ str(svid), '>'+ ':'+ '[('+str(x1), ','+ str(y1) +')]'
		sv = 'srcv='+ str(svid), str(x1), str(y1)
		row = str(sv)
		file.write(row)				
		for vehicle in vehicles:
			rvid = float (vehicle.attributes['id'].value)
			x2 = float (vehicle.attributes['x'].value)
			y2 = float (vehicle.attributes['y'].value)
			if  rvid != svid:
				dis = math.sqrt(((x2-x1)**2)) + (((y2-y1)**2))
				if dis <= r:
					print "Rec="+ str(rvid),':'+ str(x2)+","+str(y2)
					rv = 'rcv='+ str(rvid), str(x2), str(y2)
					row3 = str(rv)
					file.write(row3)
	row2 = "\n"
	file.write(row2)		
