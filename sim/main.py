def main():
	console.log('working')
	for creep in Game.creeps:
		roleHarvester.run(creep)

	

module.exports.loop = main()