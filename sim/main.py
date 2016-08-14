__rapydscript_print = console.log  ### Let us use print() instead of console.log()

def main():
	if Game.time % 5 == 0:
		print(Game.time)

	for room in Game.rooms:
		manager = new CreepManager(room)
	


module.exports.loop = main()