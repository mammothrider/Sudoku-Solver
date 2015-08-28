#coding: UTF-8
import win32gui
import win32api
import win32con
import time
from PIL import ImageGrab
from PIL import Image

class digitRecoginzer:
	
	def screenshot(self, rect):
		"""
		create a screenshot
		"""
		src_image = ImageGrab.grab((rect[0],\
									rect[1],\
									rect[2],\
									rect[3]))
		#src_image.show()
		return src_image