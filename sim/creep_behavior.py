class roleHarvester:
	def run(self, creep):
		if creep.carry.energy > creep.carryCapacity:
			energy_source = creep.room.find(FIND_SOURCES)[0]
			if creep.harvest(energy_source) == ERR_NOT_IN_RANGE:
				creep.moveTo(energy_source)
			else:
				if creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
					creep.moveTo(Game.spawns['Spawn1'])
