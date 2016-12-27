import timeit

class timer:
	def __init__(msg_queue=None):
		self.start = timeit.default_timer()
		self.end = None
		self.elapsed = None

		self.msg_queue = msg_queue


	def mark():
		log_msg = "Mark here or w/e"
		#include time also
		self.msg_queue.append(log_msg)


	def stop():
		self.end = timeit.default_timer()
		self.elapsed = self.end - self.start
		return self.elapsed

class perfmon:
	def __init__():
		self.log_msgs = [] #queue of msgs
		pass

	#returns a timer object 
	def spawn():
		return timer(msg_queue=self.log_msgs)


def main():
	pass



if __name__ == "__main__":
	main()