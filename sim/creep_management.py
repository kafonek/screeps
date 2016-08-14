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
		### Can't think of a more elegant way to work this right now
		roles = {'BasicHarvester' : harvest}
		for creep in self.creeps:
			if Game.time % 5 == 0:
				role = creep.memory.role
				if role in roles:
					behavior = roles[role]
					behavior(creep)

			
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


class BasicHarvester(_Creep):
	body = [WORK, MOVE, CARRY]
	memory = {'role': 'BasicHarvester'}


### Creep behavior actions
def harvest(creep):
	creep.say("hello world")