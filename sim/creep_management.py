class CreepManager:
	def __init__(self, roomname):
		self.room = Game.rooms[roomname]
		self.creeps = self.room.find(FIND_MY_CREEPS)
		print("CreepManager for " + self.room.name + " inited.  Creepcount: " + len(self.creeps))

		
	def print_creeps(self):
		print("There are")
		

