class Room:
	def stats(self):
		return {'creep_count' : len(self.find(FIND_MY_CREEPS))}
			


