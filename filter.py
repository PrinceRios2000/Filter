import time
import cv2
from flask import Flask, render_template, Response
from PIL import Image

class Filter:
	def find_filter(self, audio):
		dic = {'gray' : cv2.COLOR_BGR2GRAY,
			   'alien' : cv2.COLOR_BGR2HLS,
			   'beach' : cv2.COLOR_BGR2LUV,
			   'lime' : cv2.COLOR_BGR2Lab,
			   'black and white x 4' : cv2.COLOR_BGR2YUV_I420,
			   'smurf' : cv2.COLOR_RGB2BGRA, 
			   'apply negative' : 'apply negative',
               'apply Gray' : 'apply Gray'}
		default = 'did not find it here'
		string = audio.split()
		for key, value in dic.items():
			if audio == key:
				return value
			if key in audio:
				return value
		return string
