from .base import Algorithm

class DesertionAlgorithm(Algorithm):

	def evaluate(self, age, *args, **kwargs):
		age=int(age)
		if age % 2 == 0:
			result=1
		else:
			result=0
		return result


