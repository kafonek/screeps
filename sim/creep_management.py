class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		self.room.memory.manager = self
		self.creeps = self.room.find(FIND_MY_CREEPS)
		self.spawn = self.room.find(FIND_MY_SPAWNS)[0]
		self.test = []
		if Game.time % 10 == 0:
			print(self.spawn._name)
			print(dir(self.spawn))
			print(self.spawn.energy)
		self.spawnManager()



	def spawnManager(self):
		if len(self.creeps) < 1:
			creep = new BasicHarvester(self.spawn)
			creep.spawn()
			

class Unit:
	"I'd call this a Creep but it breaks the game?"
	body = []
	memory = {}
	name = None
	def __init__(self, spawner):
		self.spawner = spawner
		
	def spawn(self):
		resp = self.spawner.canCreateCreep(self.body, self.name)
		if resp == OK:
			self.spawner.createCreep(self.body, self.name, self.memory)


class BasicHarvester(Unit):
	body = [WORK, MOVE, CARRY]
	pass


