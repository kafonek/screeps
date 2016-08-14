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
			creep = new BasicHarvester(self.spawn)
			creep.spawn()	

		

class Creep:
	body = []
	def __init__(self, spawner):
		self.spawner = spawner
		
	def custom_configs(self):
		"Override this in subclasses"
		pass
		
	def spawn(self):
		resp = self.spawner.canCreateCreep(self.body)
		if resp == OK:
			self.spawner.createCreep(self.body)

class BasicHarvester(Creep):
	body = [WORK, CARRY, MOVE]


