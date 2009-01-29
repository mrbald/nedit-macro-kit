#! /usr/bin/env python

import sys, re, getopt

import getopt, sys

def raw(text):
	nexTxt=re.sub(r"([.^$*{+?}\[\]|()])",r"\\\1",text)
	return nexTxt

def grep(option):
	if option.ignore_case:
		grep_re=re.compile(option.pattern,re.IGNORECASE)
	else:
		grep_re=re.compile(option.pattern)
	sub_re=re.compile("^",re.MULTILINE)
	for filename in option.fileList:
		try:
			f=file(filename)
			content=f.read()
			f.close()
		except:
			sys.stderr.write("Error while reading "+filename+".\n")
			continue
		start=0
		count=0
		while 1:
			res=grep_re.search(content,start)
			if res!=None:
				match=sub_re.sub("\t",res.group(0))
				newStr=filename+":("+str(res.start(0))+","+str(res.end(0))+"):\n"+match
				print newStr
				start=res.end(0)
				count=count+1
			else:
				break

class ty_option:
	def __init__(self):
		self.regex = False
		self.regex = False
		self.ignore_case = False
		self.line_number = False
		self.pattern = ""
		self.patternBefore = ""
		self.patternAfter = ""
		self.fileList = ""

def usage():
	return """
	grep.py [PARAM] FILES
	-i case insensitive
	-E use python regex
	-F use fixed string
	-h help
	-b regex before
	-a regex after
	"""

def main():
	option=ty_option()
	try:
		strOptions="ihE:F:a:b:"
		opts, args = getopt.getopt(sys.argv[1:],strOptions)
	except getopt.GetoptError:
		sys.stderr.write("Bad options.\n")
		sys.stderr.write(usage())
		sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
		if o == "-i":
			option.ignore_case=True
		if o == "-E":
			option.regex=True
			option.pattern=a
		if o == "-F":
			option.regex=False
			option.pattern=a
		if o == "-b":
			option.patternBefore=a
		if o == "-a":
			option.patternAfter=a
		if o in ("-h", "--help"):
			sys.stdout.write(usage())
			sys.exit(0)
	
	if option.pattern=="":
		sys.stderr.write("No pattern.\n")
		sys.stderr.write(usage())
		sys.exit(1)
	
	option.fileList=args
	if option.fileList=="":
		sys.stderr.write("No file.\n")
		sys.stderr.write(usage())
		sys.exit(1)

	if not option.regex:
		option.pattern=raw(option.pattern)
	
	option.pattern=option.patternBefore+option.pattern+option.patternAfter
	grep(option)


if __name__ == "__main__":
	main()

