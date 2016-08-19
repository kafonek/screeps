class _Room:
	def __init__(self, room_name):
		self.room = Game.rooms[room_name]
		self.memory = self.room.memory
		self.name = self.room.name
		self.find_constants()

	def find_constants(self):
		if 'spawn' not in self.memory:
			print("Setting constants")
			self.memory['spawn'] = self.room.find(FIND_MY_SPAWNS)[0]
			self.memory['creeps'] = self.room.find(FIND_MY_CREEPS)
		
		self.spawn = self.memory['spawn']
		self.creeps = self.memory['creeps']
			


