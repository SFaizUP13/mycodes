from xml.dom import minidom
import math
import fileinput

def main():
	prv_timestep=''
	pcheck = 0
	totalCounter = 0
	matchedCounter = 0
	with open('900s_range500_matchCount.txt', 'w+') as output:
		with open ('1-899_RCVsorted_TimeArrang_Arrange.txt', 'r+') as nsfile:
			nslines = nsfile.readlines()
			with open ('900s_mobility_range500.txt', 'r+') as mobfile:
				moblines = mobfile.readlines()
				for mbitr in range(0, len(moblines)):
					mobline = moblines[mbitr]
					if 'Timestep' in mobline:
						mobTimeRcv = mobline.strip()
					if 'Timestep' not in mobline:
						mobtdr = int(mobline)
						totalCounter +=1
						#print(totalCounter)
						for nsitr in range(0, len(nslines)):
							nsline = nslines[nsitr]
							if 'Timestep' in nsline:
								nsTimeRcv = nsline.strip()
								prv_nsTime = nsTimeRcv
								if mobTimeRcv == nsTimeRcv and mobTimeRcv != prv_timestep:
									output.write(str(mobTimeRcv)+'\n')
									prv_timestep = mobTimeRcv
									pcheck = 1
									totalCounter = 1
									print(mobTimeRcv)
							if 'Timestep' not in nsline and mobTimeRcv == nsTimeRcv:
								#print(str(mobTimeRcv)+'ttt'+str(nsTimeRcv))
								if 'Timestep' not in nsline:
									nstdr = int(nsline)
									if mobtdr == nstdr:
										matchedCounter += 1
									#print(matchedCounter)
					if mobTimeRcv != prv_timestep and pcheck == 1:
						output.write(str(matchedCounter)+'/'+str(totalCounter)+'\n')
						totalCounter = 0
						matchedCounter = 0
						pcheck =0






if __name__ == "__main__":
 	main()
