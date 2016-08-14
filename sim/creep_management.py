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
				behaviorClass = new behavior(self.room, creep)
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

	def _get(self, key):
		"Retrieve an object from persistent memory"
		if key in self.memory:
			return Game.getObjectById(self.memory[key])

	def _set(self, key, object):
		"Set an object in persistent memory"
		self.memory[key] = object.id

class BasicHarvesterBehavior(_CreepBehavior):
	def find_closest_spawn(self):
		spawn = self._get('closest_spawn')
		if not spawn:
			spawn = self.creep.pos.findClosestByPath(FIND_MY_SPAWNS)
			self._set('closest_spawn', spawn)
		return spawn

	def find_closest_energy(self):
		energy = self._get('closest_energy')
		if not energy:
			energy = self.creep.pos.findClosestByPath(FIND_SOURCES)
			self._set('closest_energy', energy)
		return energy
		
	def tick(self):
		if self.creep.carry < self.creep.energyCapacity:
			energy = self.find_closest_energy()
			resp = self.creep.harvest(energy)
			if resp == -9:
				self.creep.moveTo(closest)
		else:
			spawn = self.find_closest_spawn()
			resp = self.creep.transfer(spawn, RESOURCE_ENERGY)
			if resp == -9:
				self.creep.moveTo(spawn)





