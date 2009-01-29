#! /usr/bin/env python

import sys, pdb
from swk import *

g_logfile=LogFile()

def GetParam():
	from optparse import OptionParser
	usage = "usage: %prog [options] rootpath"
	parser = OptionParser(usage)
	parser.add_option("-b", "--boolean", action="store_true", dest="boolean", help="boolean example", default=False)
	parser.add_option("-s", "--string", dest="string", help="string example", default="defaultString")
    
	(options, args) = parser.parse_args()

	return (options, args)
	
def doSomething(args):
	pass

def main():
	(options, args)=GetParam()
	doSomething(args)
	print "hello world"

if __name__ == "__main__":
    main()
