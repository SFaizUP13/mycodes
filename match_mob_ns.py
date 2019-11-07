# This script compares the RCV in both files (from Mob to NS) if matched increaments the RCV counter and
# compares its transmitter if matched increaments matchedRcvCounter at each timestep
from xml.dom import minidom
import math
import fileinput

def main():
	TotalRcvCounter = 0
	matchedRcvCounter = 0
	prv_mobTime = ''
	a = 0
	with open ('NS_mob_outputfile.txt', 'w+') as output:
		with open ('NV21_NS3_RCVsorted_removnewLine2.txt', 'r+') as nsfile:
			nslines = nsfile.readlines()
			with open ('NV21_MaxTmobility_removnewLine.txt', 'r+') as mobfile:
				moblines = mobfile.readlines()
				for mobitr in range(0, len(moblines)):
					mobline = moblines[mobitr]
					splitmobline = mobline.split('_')
					mobTime = splitmobline[0]
					mobNodes = splitmobline[1]
					splitmobNodes = mobNodes.split('-')
					rcvNodemob = int(splitmobNodes[0])
					tdrNodesmob = int(splitmobNodes[1])
					split2mobline = mobline.split('-')
					mobTS_RcvSec = split2mobline[0]
					if prv_mobTime != mobTime:
						output.write(str(prv_mobTime)+';'+str(matchedRcvCounter)+'/'+str(TotalRcvCounter)+'\n')
						TotalRcvCounter = 0
						matchedRcvCounter = 0
						prv_mobTime = mobTime
					a = 0
					for nsitr in range(0, len(nslines)):
						nsline = nslines[nsitr]
						splitnsline = nsline.split('_')
						nsTime = splitnsline[0]
						nsNodes = splitnsline[1]
						splitnsNodes = nsNodes.split('-')
						nsrcvNode = int(splitnsNodes[0])
						tdrNodesns = int(splitnsNodes[1])
						split2nsline = nsline.split('-')
						nsTS_RcvSec = split2nsline[0]
						if mobTime == nsTime:
							#output.write(str(rcvNodemob)+' '+str(tdrNodesmob)+'   '+str(nsrcvNode)+' '+str(tdrNodesns)+'\n')
							if rcvNodemob == nsrcvNode:								
								if a == 0:
									TotalRcvCounter += 1
									a = 1
								if tdrNodesmob == tdrNodesns:
									matchedRcvCounter += 1
									#output.write(str(rcvNodemob)+' '+str(tdrNodesmob)+'  '+str(matchedRcvCounter)+'/'+str(TotalRcvCounter)+'\n')
									break
				output.write(str(prv_mobTime)+';'+str(matchedRcvCounter)+'/'+str(TotalRcvCounter)+'\n')


							



if __name__ == "__main__":
    main()





# from xml.dom import minidom
# import math
# import fileinput

# def main():
# 	TotalRcvCounter = 0
# 	matchedRcvCounter = 0
# 	TotalTdrCounter = 0
# 	matchedTdrCounter = 0
# 	prv_mobTS_RcvSec = ''
# 	prv_mobTime = ''
# 	prv_mobitr = ''
# 	prv_nsitr = ''
# 	index = -1
# 	with open ('outputfile.txt', 'w+') as output:
# 		with open ('NV21_NS3_RCVsorted_removnewLine22.txt', 'r+') as nsfile:
# 			nslines = nsfile.readlines()
# 			with open ('NV21_MaxTmobility_removnewLine40S.txt', 'r+') as mobfile:
# 				moblines = mobfile.readlines()
# 				for mobitr in range(0, len(moblines)):
# 					mobline = moblines[mobitr]
# 					splitmobline = mobline.split('_')
# 					mobTime = splitmobline[0]
# 					mobNodes = splitmobline[1]
# 					split2mobline = mobline.split('-')
# 					mobTS_RcvSec = split2mobline[0]
# 					for nsitr in range(0, len(nslines)):
# 						nsline = nslines[nsitr]
# 						splitnsline = nsline.split('_')
# 						nsTime = splitnsline[0]
# 						nsNodes = splitnsline[1]
# 						split2nsline = nsline.split('-')
# 						nsTS_RcvSec = split2nsline[0]
# 						if mobTime == nsTime:
# 							if mobNodes == nsNodes:# and index<nsitr:
# 								print(str(mobNodes)+'ss'+str(nsNodes))
# 								matchedRcvCounter += 1
# 						# if mobTime == nsTime and index < nsitr:
# 						# 	TotalRcvCounter += 1
# 						# 	index = nsitr
# 						if mobTime != prv_mobTime:
# 							output.write(str(mobTime)+';'+str(matchedRcvCounter)+'/'+str(TotalRcvCounter)+'\n')
# 							prv_mobTime = mobTime
# 							#output.write(str(matchedRcvCounter)+'/'+str(TotalRcvCounter)+'\n')
# 							matchedRcvCounter = 0
# 							TotalRcvCounter = 0



# if __name__ == "__main__":
#     main()










# from xml.dom import minidom
# import math
# import fileinput

# def main():
# 	TotalRcvCounter = 0
# 	matchedRcvCounter = 0
# 	TotalTdrCounter = 0
# 	matchedTdrCounter = 0
# 	prv_mobTS_RcvSec = ''
# 	prv_mobTimeSec = ''
# 	prv_mobitr = ''
# 	prv_nsitr = ''
# 	with open ('outputfile.txt', 'w+') as output:
# 		with open ('NV21_NS3_RCVsorted_removnewLine22.txt', 'r+') as nsfile:
# 			nslines = nsfile.readlines()
# 			with open ('NV21_MaxTmobility_removnewLine40S.txt', 'r+') as mobfile:
# 				moblines = mobfile.readlines()
# 				for mobitr in range(0, len(moblines)):
# 					mobline = moblines[mobitr]
# 					if 'Timestep:' in mobline:
# 						splitmobline = mobline.split('-')
# 						mobTS_RcvSec = splitmobline[0]
# 						mobTdrNode = int(splitmobline[1])
# 						splitmobTS_RcvSec = mobTS_RcvSec.split('_')
# 						mobTimeSec =  splitmobTS_RcvSec[0]
# 						mobRcvNode = int(splitmobTS_RcvSec[1])
# 						#print(mobRcvNode)
# 					for nsitr in range(0, len(nslines)):
# 						nsline = nslines[nsitr]
# 						if 'Timestep:' in nsline:
# 							splitnsline = nsline.split('-')
# 							nsTS_RcvSec = splitnsline[0]
# 							nsTdrNode = int(splitnsline[1])
# 							splitnsTS_RcvSec = nsTS_RcvSec.split('_')
# 							nsTimeSec = splitnsTS_RcvSec[0]
# 							nsRcvNode = int(splitnsTS_RcvSec[1])
# 							prv_nsline = nsline
# 						if mobTS_RcvSec != prv_mobTS_RcvSec:
# 							output.write(str(mobTS_RcvSec)+'-'+str(matchedTdrCounter)+' outof '+str(TotalTdrCounter)+'\n')
# 							TotalRcvCounter += 1
# 							prv_mobTS_RcvSec = mobTS_RcvSec
# 							print(nsRcvNode)
# 							matchedTdrCounter = 0
# 							TotalTdrCounter = 0
# 						if mobTS_RcvSec == nsTS_RcvSec:
# 							if mobitr != prv_mobitr and prv_nsitr != nsitr:
# 								TotalTdrCounter += 1
# 								prv_mobTimeSec = mobTimeSec
# 								if mobTdrNode == nsTdrNode:
# 									matchedTdrCounter += 1
# 									prv_mobitr = mobitr
# 									prv_nsitr = nsitr
							

# # 05/11/2019  16:00




# if __name__ == "__main__":
#     main()
