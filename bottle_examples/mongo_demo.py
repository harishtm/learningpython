from pymongo import MongoClient


class MongoDBConnectionManager:

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.connection = None

	def __enter__(self):
		self.connection = MongoClient(host=self.host, port=self.port)
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.connection.close


with MongoDBConnectionManager('localhost', 27017) as dbclient:
	db_names = dbclient.connection.list_database_names()
	if 'student' in db_names:
		db = dbclient.connection['student']
		all_tables = db.list_collection_names()
		if 'user' in all_tables:
			all_users = db.user.find({})
			for each_student in all_users:
				print(each_student.get('name'), each_student.get('age'))

