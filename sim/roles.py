class Role:
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

class BasicHarvesterBehavior(Role):
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
		creep = self.creep

		if _.sum(creep.carry) < creep.carryCapacity:
			energy = self.find_closest_energy()
			resp = creep.harvest(energy)
			if resp == ERR_NOT_IN_RANGE:
				creep.say("Off To Work")
				creep.moveTo(energy)
			else:
				creep.say("Harvest Erry Day")
		else:
			spawn = self.find_closest_spawn()
			resp = creep.transfer(spawn, RESOURCE_ENERGY)
			if resp == ERR_NOT_IN_RANGE:
				creep.say("On My Way Home")
				creep.moveTo(spawn)
			else:
				creep.say("Dump!")