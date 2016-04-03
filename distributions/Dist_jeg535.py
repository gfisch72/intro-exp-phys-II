
import numpy as np
from base_distribution import BaseDistribution

class Dist_jeg535(BaseDistribution):
	def __init__(self):
		self.f_max = 72
		self.x_min = -7.2
		self.x_max = .72


	def pdf(self, x):
		"""This is your PDF"""
		return np.abs(x+7.2)

	def mean(self):
		"""This is the mean of the PDF"""
		return -3.24

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(15.6816)
