class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		self.creeps = self.room.find(FIND_MY_CREEPS)
		self.spawn = self.room.find(FIND_MY_SPAWNS)[0]
		self.test = []
		if Game.time % 10 == 0:
			print(self.spawn._name)
			print(dir(self.spawn))
			print(self.spawn.energy)
		self.spawnManager()


	def spawnManager(self):
		creep = new Duder()
		print(creep)

class Duder:
	def __init__(self):
		self.body = []


class BasicHarvester(Duder):
	pass


