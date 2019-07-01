from xml.dom import minidom
import math
xmldoc = minidom.parse("Trace.xml")

dis = float ('0.0')
r = float('800')
fcd = xmldoc.getElementsByTagName("fcd-export")[0]
timesteps = fcd.getElementsByTagName("timestep")
for timestep in timesteps:
	print('Timestep =' + timestep.attributes['time'].value)
	vehicles = timestep.getElementsByTagName("vehicle")
	for vehicle in vehicles:
		svid = float (vehicle.attributes['id'].value)
		svx = float (vehicle.attributes['x'].value)
		svy = float (vehicle.attributes['y'].value)
		#print '<'+ 'svid='+ svid, '>'+ '['+ svx, ','+ svy +']'
		print 'Src='+ str(svid),':'+ '('+str(svx), ','+ str(svy) +')'
		for vehicle in vehicles:
			rvid = float (vehicle.attributes['id'].value)
			if rvid != svid:
				x2 = float (vehicle.attributes['x'].value)
				y2 = float (vehicle.attributes['y'].value)
				dis = math.sqrt( ((x2-svx)**2)) + (((y2-svy)**2) )
				#if x2 < xmax and y2 < ymax:
				if dis <= r:
					print "Rec="+ str(rvid),':'+ str(dis)
			else: 
				print 'No vehicle in range'
	
			# This section for exporting it in text file
			#x2 = vehicle.attributes['x'].value
			#y2 = vehicle.attributes['y'].value
			#with open("mycode.txt", "w") as f:
			#	f.write(vid)
			#print vid, x2, y2 
			#if x2 >= x1 and y2 >= y1:
			#print 'V='+ vid,':'+ '(x='+ x2,','+ 'y=' + y2 +")"

		
			#	outputf.write(output)
			#	outputf.close()
		#print 'V='+ vehicle.attributes['id'].value,':'+ '(x=' +vehicle.attributes['x'].value,','+ 'y=' + vehicle.attributes['y'].value +")"
		#output = (vehicles + '.txt', 'w')
		#output.write (vehicle.attributes['id'].value + ":" +vehicle.attributes['x'].value + "," +vehicle.attributes["y"].value
			
