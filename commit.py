from subprocess import Popen, PIPE
import os
import glob

def run(cmd):
	proc = Popen(cmd, stdout=PIPE, shell=True)
	text = proc.communicate()[0]
	return text

def rapyd():
	root, directories, files = next(os.walk('.'))
	for directory in directories:
		if '.' not in directory:
			files = glob.glob('%s/*.py' % directory)
			# Put main.py at the front of the list just for readability in the javascript
			index = files.index(os.path.join(directory, 'main.py'))
			files.insert(0, files.pop(index))

			outfile = os.path.join(directory, 'js', 'main.js')

			cmd = 'rapydscript %s -pbm --output %s' % (' '.join(files), outfile)
			print(cmd)
			run(cmd)
			### replace rS symbol because screeps can't handle the unicode in the js file
			text = open(outfile).read()
			rs_symbol = '\xd5\x90\xd5\x8f'
			text = text.replace(rs_symbol, '__rapydscript')
			with open(outfile, 'w') as f:
				f.write(text)
			

def commit(commit_msg=None):
	# Commit everything in the project
	if isinstance(commit_msg, list):
		commit_msg = ' '.join(commit_msg)
	run('git add .')
	if not commit_msg:
		run('git commit -m "updates" .')
	else:
		run('git commit -m "%s" .' % commit_msg)
	run('git push')


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--no_commit', action='store_true', default=False, help="No-commit, doesn't push to github")
	parser.add_argument('-m', '--message', default=None, nargs='+', help="(optional) commit message on git commit")
	args = parser.parse_args()

	
	rapyd()
	if not args.no_commit:
		commit(args.message)


	

