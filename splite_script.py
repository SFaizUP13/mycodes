from xml.dom import minidom
import math
import fileinput

def main():

	with open ('split-TDout.txt', 'w+') as outfile:
		with open ('TDtrace_out.txt', 'r+') as infile:
			lines = infile.readlines()
			for i in range(0, len(lines)):
				line = lines[i]
				split1 = line.split('/DeviceList/0/$ns3::WifiNetDevice/Phy/State/Tx') # For Transmitting data
				#split1 = line.split('/DeviceList/0/$ns3::WifiNetDevice/Phy/State/RxOk') # For receiving data
				nodenum= split1[0]
				SA = split1[1]
				outfile.write(nodenum+SA)






if __name__ == "__main__":
    main()
