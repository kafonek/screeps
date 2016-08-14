class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		print("CreepManager init for " + self.room.name)
		print(self.room.energyAvailable)

		
	def print_creeps(self):
		print("There are")
		

