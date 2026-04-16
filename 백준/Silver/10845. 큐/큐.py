import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()

class CircularQueue:
	def __init__(self, k):

		self.q = [None] * k
		self.front_idx = 0
		self.rear_idx = 0
		self.size = 0
		self.max_size = k


	def enqueue(self, value):
		if self.size == self.max_size:
			raise IndexError("Queue is full")

		self.q[self.rear_idx] = value
		self.rear_idx = (self.rear_idx + 1) % self.max_size
		self.size += 1

	def dequeue(self):
		if self.size == 0:
			return -1

		value = self.q[self.front_idx]
		self.front_idx = (self.front_idx + 1) % self.max_size
		self.size -= 1
		return value

	def front(self):
		if self.size == 0:
			return -1
		return self.q[self.front_idx]

	def back(self):
		if self.size == 0:
			return -1

		last_index = (self.rear_idx - 1 + self.max_size) % self.max_size
		return self.q[last_index]

	def get_size(self):
		return self.size


q = CircularQueue(100000)
for _ in range(n):

	command = list(input().split())
	if command[0] == 'push':
		q.enqueue(command[1])
	elif command[0] == 'pop':
		print(q.dequeue())
	elif command[0] == 'size':
		print(q.get_size())
	elif command[0] == 'empty':
		print(1 if q.get_size() == 0 else 0)
	elif command[0] == 'front':
		print(q.front())
	elif command[0] == 'back':
		print(q.back())


