def memcache(fn, mem_name):
	def wrapped(self, *args, **kwargs):
		if mem_name in self.memory:
			return self.memory[mem_name]
		else:
			result = fn(self, *args, **kwargs)
			self.memory[mem_name] = result
			return result

class Room:
	
	@memcache('creep_count')
	def stats(self):
		return {'creep_count' : len(self.find(FIND_MY_CREEPS))}
			


