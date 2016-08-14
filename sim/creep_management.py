class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		self.creeps = self.room.find(FIND_MY_CREEPS)
		self.spawn = self.room.find(FIND_MY_SPAWNS)[0]
		if Game.time % 10 == 0:
			print(dir(self.spawn))
			print(self.spawn.energy)
		self.spawnManager()


	def spawnManager(self):
		if len(self.creeps) < 2:
			creep = new Creep()
			resp = self.spawn.canCreateCreep(creep.body)
			print(resp)
			if resp == OK:
				self.spawn.createCreep(creep.body, creep.name, creep.memory)
			

		

class Creep:
	@property
	def body(self):
		return []

	@property
	def memory(self):
		return {}

	@property
	def name(self):
		return None


class BasicHarvester(Creep):
	@property
	def body(self):
		return [WORK, CARRY, MOVE]


