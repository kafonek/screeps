### Deals with Room Management
class RoomManager:
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
		self.behaviorManager()

	def spawnManager(self):
		if len(self.creeps) < 1:
			creep = new BasicHarvester(self.spawn)
			creep.spawn()

	def behaviorManager(self):
		for creep in self.creeps:
			if Game.time % 5 == 0:
				creep.say("hello world")

			
### Deals with Creep Creation			
class _Creep:
	"I'd call this a Creep but it breaks the game?"
	body = []
	memory = {'role' : 'AbstractBaseCreep'} # Override this in subclasses
	name = None
	def __init__(self, spawner):
		self.spawner = spawner

	def spawn(self):
		resp = self.spawner.canCreateCreep(self.body, self.name)
		if resp == OK:
			print("Spawning new " + self.type)
			print("Body: " + self.body)
			print("Memory: " + self.memory)
			self.spawner.createCreep(self.body, self.name, self.memory)
		else:
			print("Tried to spawn a " + self.type + " but got code " + resp)

	def run(self, creep):
		"Subclasses should specify behavior here.  creep will be the instantiated creep object"
		pass


class BasicHarvester(_Creep):
	body = [WORK, MOVE, CARRY]
	memory = {'role': 'BasicHarvester'}

	def run(self, creep):
		if Game.time % 5 == 0:
			creep.say("Hello World")





class roleHarvester:
	def run(self, creep):
		if creep.carry.energy > creep.carryCapacity:
			energy_source = creep.room.find(FIND_SOURCES)[0]
			if creep.harvest(energy_source) == ERR_NOT_IN_RANGE:
				creep.moveTo(energy_source)
			else:
				if creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
					creep.moveTo(Game.spawns['Spawn1'])
