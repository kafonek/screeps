__rapydscript_print = console.log  ### Let us use print() instead of console.log()

def main():
	if Game.time % 5 == 0:
		print(Game.time)

	for name in Game.rooms:
		manager = CreepManager(room)
		manager.print_creeps()

	

module.exports.loop = main()