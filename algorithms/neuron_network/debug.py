class Debug:
	def __init__(self, title):
		self.title = "----------"+title+"----------"
		length = len(title) + 20
		self.signature = "-"*length
		self.buffer = []
	def buff(self, log):
		self.buffer.append(log)
	def log(self, empty=True):
		print(self.title)
		for b in self.buffer:
			print(b)
		print(self.signature)
		if empty:
			self.release()
	def release(self):
		self.buffer = []