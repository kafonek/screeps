__rapydscript_print = console.log  ### Let us use print() instead of console.log()

def main():
	for room in Game.rooms:
		manager = new RoomManager(room)

module.exports.loop = main()