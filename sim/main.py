__rapydscript_print = console.log

def main():

	if Game.time % 5 == 0:
		print(Game.time)
	for name in Game.rooms:
		room = Game.rooms[name]
		creeps = room.find(FIND_MY_CREEPS)
		print(creeps)

	

module.exports.loop = main()