class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		self.creeps = self.room.find(FIND_MY_CREEPS)
		self.spawn = self.room.find(FIND_MY_SPAWNS)[0]
		if Game.time % 10 == 0:
			print(dir(self.spawn))
			print(self.spawn.energy)
			

	def spawnManager(self):
		pass	

		

