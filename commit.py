if __name__ == '__main__':
	import sys
	commit_msg = None
	if len(sys.argv) > 1:
		commit_msg = ' '.join(sys.argv[1:])
	import glob
	files = ['main.py'] + [f for f in glob.glob('*.py') if f not in ['main.py', 'commit.py']]


	from subprocess import Popen, PIPE
	def run(cmd):
		proc = Popen(cmd, stdout=PIPE, shell=True)
		text = proc.communicate()[0]
		return text


	cmd = 'rapydscript %s -pbm --output js/main.js' % ' '.join(files)
	run(cmd)

	run('git add .')
	if not commit_msg:
		run('git commit -m "updates" .')
	else:
		run('git commit -m "%s" .' % commit_msg)
	run('git push')

