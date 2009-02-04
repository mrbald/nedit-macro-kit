import os, subprocess, shutil

def tryrmtree(path):
	try:
		shutil.rmtree(path)
	except:
		pass

os.chdir(os.getenv("HOME"))
tryrmtree("dot_nedit")
shutil.copytree(".nedit", "dot_nedit")
os.remove("dot_nedit/nedit.history")
svn2remove=[]
for root, dirs, files in os.walk('dot_nedit'):
	if ".svn" in dirs:
		svn2remove.append(os.path.join(root,".svn"))
for d in svn2remove:
	shutil.rmtree(d)
subprocess.Popen(["tar","zcvf","nedit-macro-kit.tar.gz","dot_nedit"]).communicate()
tryrmtree("dot_nedit")
