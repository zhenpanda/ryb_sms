import pickle
import os
import hashlib

class Keeper:

	def __init__(self, fname):
		self.fname = fname
		self.files = {'cfilepath': 'temp1234.rybdb', 'pwfile': 'printer.rybdb', 'markerfile': 'sal_marker.rybdb',
						'dbpw': self.hashpw("Exodar$2011"), 'resetpw': True, 
						'bg_img': {'Brooklyn': 'images\\background_STU_BRK.jpg',
									'Elmhurst': 'images\\background_STU_ELM.jpg',
									'Flushing': 'images\\background_STU_FLU.jpg',
									'Chinatown': 'images\\background_STU_CHI.jpg'}}
		
		try:
			self.load()
		except:
			self.save()

	def hashpw(self, pw):
		md5_hasher = hashlib.md5()
		md5_hasher.update(str.encode(pw))
		return md5_hasher.digest()

	def load(self):
		self.files = pickle.load(open(self.fname, "rb"))

	def save(self):
		pickle.dump(self.files, open(self.fname, "wb"))

#Keeper('keeper.db')