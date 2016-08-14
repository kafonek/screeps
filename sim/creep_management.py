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
		classmap = {'BasicHarvester' : BasicHarvesterBehavior}
		for creep in self.creeps:
			cls = creep.memory.class
			if cls in classmap:
				behavior = classmap[cls]
				behaviorClass = behavior(self.room, creep)
				behaviorClass.tick()

			
### Deals with Creep Creation			
class _Creep:
	"I'd call this a Creep but it breaks the game?"
	body = []
	memory = {'class' : 'AbstractBaseCreep'} # Override this in subclasses
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
	memory = {'class': 'BasicHarvester'}

### Deals with Creep Behavior
class _CreepBehavior:
	def __init__(self, room, creep):
		self.room = room
		self.creep = creep
		self.memory = creep.memory

class BasicHarvesterBehavior(_CreepBehavior):
	def tick(self):
		if Game.time % 5 == 0:
			self.creep.say(Game.time)



