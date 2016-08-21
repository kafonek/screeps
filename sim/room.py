#def memcache(fn):
#	print("In memcache of " + fn)
#	def wrapped(self, *args, **kwargs):
#		return fn(self, *args, **kwargs)

class Room:
	
	@memcache
	def stats(self):
		return {'creep_count' : len(self.find(FIND_MY_CREEPS))}
			


