console.log = print

def main():

	if Game.time % 5 == 0:
		print(Game.time)
	for name in Game.rooms:
		room = Game.rooms[name]
		creeps = room.find(FIND_MY_CREEPS)
		#console.log

	

module.exports.loop = main()