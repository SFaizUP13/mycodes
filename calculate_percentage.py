#This script calculates the percentage of error
from xml.dom import minidom
import math
import fileinput

def main():
	prv_timestep=''
	with open('NS_mob400_outputfile_errorpercen.txt', 'w+') as output:
		with open ('NS_mob400_outputfile.txt', 'r+') as infile:
			lines = infile.readlines()
			for itr in range(0, len(lines)):
				line = lines[itr]
				splitline= line.split(';')
				timestep = splitline[0]
				splittime = timestep.split('.')
				timesecond = splittime[0]
				nodes = splitline[1]
				splitnodes = nodes.split('/')
				matched = int(splitnodes[0])
				total = int(splitnodes[1])
				if timestep != prv_timestep:
					Errorpercent = ((float(total)-float(matched))/float(total))*100.00
					error = ("{0:.2f}".format(Errorpercent))
					print (str(matched)+' '+str(total))
					#output.write(str(timestep)+':'+str(matched)+'ddd'+str(total)+'perc'+str(error)+'\n')
					output.write(str(timestep)+'; '+str(error)+', '+str(total)+'\n')
					prv_timestep = timestep





if __name__ == "__main__":
    main()