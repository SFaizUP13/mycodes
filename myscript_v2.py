from xml.dom import minidom

xmldoc = minidom.parse("Trace.xml")
#x2 = 0
#y2 = 0
#vid = 0
xmin = float ('0.0')
xmax = float ('0.0')
ymin = float ('0.0')
ymax = float ('0.0')
row = ''
fcd = xmldoc.getElementsByTagName("fcd-export")[0]
timesteps = fcd.getElementsByTagName("timestep")
for timestep in timesteps:
	t = timestep.attributes['time'].value
	print('Timestep =' + t)
	vehicles = timestep.getElementsByTagName("vehicle")
	for vehicle in vehicles:
		svid = float (vehicle.attributes['id'].value)
		svx = float (vehicle.attributes['x'].value)
		svy = float (vehicle.attributes['y'].value)
		#print '<'+ 'svid='+ svid, '>'+ '['+ svx, ','+ svy +']'
		print svid, svx, svy
		for vehicle in vehicles:
			rvid = float (vehicle.attributes['id'].value)
			#rx = float ('600.00')
			#ry = float ('400.00')
			r = float('200')
			xmin = float (svx-r)
			xmax = float (svx+r)
			ymin = float (svy-r)
			ymax = float (svy+r)

			if rvid != svid:
				x2 = float (vehicle.attributes['x'].value)
				y2 = float (vehicle.attributes['y'].value)
				if x2 < xmax and y2 < ymax:
					if x2 > xmin and y2 > ymin: 
		#				print 'rvid='+ rvid, '('+ x2, ','+ y2 +')'
						print rvid
				for timestep in timesteps:
					row = str(t)+":"+ str(rvid)+","+ str(svx)+","+str(svy)+"\n"
					file =open ("row.txt",'w')
   					file.write(row)

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
			
