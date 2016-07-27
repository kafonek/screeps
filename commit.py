if __name__ == '__main__':
	import sys
	print(sys.argv)
	import glob
	files = ['main.py'] + [f for f in glob.glob('*.py') if f not in ['main.py', 'commit.py']]


	from subprocess import Popen, PIPE
	def run(cmd):
		proc = Popen(cmd, stdout=PIPE, shell=True)
		text = proc.communicate()[0]
		return text


	cmd = 'rapydscript %s -pbm' % ' '.join(files)
	run(cmd)

	run('git add .')
	run('git commit -m "updating" .')
	run('git push')

