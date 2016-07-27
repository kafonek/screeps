def main():
	console.log('working')
	creep = Game.creeps['Harvester1']
	sources = creep.room.find(FIND_SOURCES)
	if creep.carry.energy < creep.carryCapacity:
		if creep.harvest(sources[0]) == ERR_NOT_IN_RANGE:
			creep.moveTo(sources[0])
	else:
		if creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE:
			creep.moveTo(Game.spawns['Spawn1'])

module.exports.loop = main()