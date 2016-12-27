import timeit

class timer:
	def __init__(self, msg_queue=None):
		self.start = timeit.default_timer()
		self.end = None
		self.elapsed = None

		self.msg_queue = msg_queue


	def log(self, msg):
		if self.msg_queue:
			self.msg_queue.append(msg)
		else:
			print(msg)


	def stop_msg(self, time):
		return "%f \tStopped" % time


	def mark(self, msg=""):
		#include time also
		self.log(msg)


	def stop(self):
		self.end = timeit.default_timer()
		self.elapsed = self.end - self.start
		self.log(self.stop_msg())
		return self.elapsed

class perfmon:
	def __init__(self):
		self.log_msgs = [] #queue of msgs
		pass

	#returns a timer object 
	def spawn(self):
		return timer(msg_queue=self.log_msgs)

	def repeat(self, func, func_arg_dict=None, n=1000):
		mytimer = None
		if func_arg_dict:
			mytimer = self.spawn()
			for i in range(n):
				func(**func_arg_dict)
				mytimer.mark()
			mytimer.stop()
		else:
			func()


def main():
	pass



if __name__ == "__main__":
	main()