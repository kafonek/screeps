from subprocess import Popen, PIPE
def run(cmd):
	proc = Popen(cmd, stdout=PIPE, shell=True)
	text = proc.communicate()[0]
	return text

if __name__ == '__main__':
	import sys, os, glob
	commit_msg = None
	if len(sys.argv) > 1:
		commit_msg = ' '.join(sys.argv[1:])
	root, directories, files = next(os.walk('.'))
	for directory in directories:
		if '.' not in directory:
			files = glob.glob('%s/*.py' % directory)
			# Put main.py at the front of the list just for readability in the javascript
			index = files.index(os.path.join(directory, 'main.py'))
			files.insert(0, files.pop(index))

			outfile = os.path.join(directory, 'js', 'main.js')

			cmd = 'rapydscript %s -pbm --output %s' % (' '.join(files), outfile)
			run(cmd)

	# Commit everything in the project
	run('git add .')
	if not commit_msg:
		run('git commit -m "updates" .')
	else:
		run('git commit -m "%s" .' % commit_msg)
	run('git push')

