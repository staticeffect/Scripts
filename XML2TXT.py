#!/usr/bin/python
#
import sys, re
def ParseHugeFile(InputFilename, OutputFileHandle):	# 
	# Open input file
	# Pull one line
	#	regex to pull addr="(.*)"
	#
	# Output: write I.P. address \n
	
	reIPAddr = re.compile(r'.*addr="([^"]*)"')
	with open(InputFilename, 'r') as InputFileHandle:
		LineNum = 0
		for lineIn in InputFileHandle:
			if reIPAddr.match(lineIn):
				IP = reIPAddr.match(lineIn).group(1).strip()
			else:
				continue
			LineNum += 1
			OutputFileHandle.write(IP + '\n')
	print LineNum	
	return

if __name__ == '__main__':
	InputFilename = '/media/SP UFD U3/scan.xml'
	OutputFilename = 'IP.txt'
	with open (OutputFilename, 'w') as OutputFileHandle:
		ParseHugeFile(InputFilename, OutputFileHandle)
