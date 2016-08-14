def main():
	if Game.time % 5 == 0:
		console.log(Game.time)
	for name in Game.rooms:
		console.log(name)
		console.log(Game.rooms[name].energyAvailable)

	

module.exports.loop = main()