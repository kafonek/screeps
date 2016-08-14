class CreepManager:
	def __init__(self, room):
		self.room = Game.rooms[room]
		self.creeps = self.room.find(FIND_MY_CREEPS)

	