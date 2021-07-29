import random
from .base import Algorithm

class RandomAlgorithm(Algorithm):

	def evaluate(self, *args, **kwargs):
		return random.getrandbits(1)
