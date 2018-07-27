from pymongo import MongoClient

class Account:
	def __init__(self):
		self.db = MongoClient('localhost', 8000)
		self.data = self.db.base.account

	def create(self, username, password, info):
		self.data.insert_one({'username' : username, 'password' : password, 'info' : info})

	def read(self, username, password):
		account = self.data.find_one({'username' : username, 'password' : password})
		return account

	def update(self, change, new, acc):
		acc[change] = new
		self.data.update_one(acc)

	def delete(self, acc):
		self.data.delete_one(acc)

