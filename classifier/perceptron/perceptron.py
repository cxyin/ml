#!/usr/bin/env python
class Perceptron:
	def _init_(self):
		pass
	def init(self, samples, e, w, b):
		self.samples = samples
		self.e = e
		self.w = w
		self.b = b
	def learn(self):
		while True:
			flag = True
			for sample in self.samples:
				if sample[-1]*(self.w[0]*sample[0] + self.w[1]*sample[1] + self.b) <= 0:
					self.w[0] += self.e*sample[-1]*sample[0]
					self.w[1] += self.e*sample[-1]*sample[1]
					self.b += self.e*sample[-1]
					print self.w, self.b
					flag = False
			if flag:
				break
				

if __name__ == '__main__':
	samples = [[3.0, 3.0, 1.0], [4.0, 3.0, 1.0], [1.0, 1.0, -1.0]]

	per = Perceptron()
	per.init(samples, 1, [0,0], 0)
	per.learn()

	print per.w, per.b
