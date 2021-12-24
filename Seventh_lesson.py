import sqlite3 as sql

class DBWorker:
  def __init__(self, db_name):
    self.cur_db = sql.connect(db_name)
    self.cursor = None
    self.result = None

  def connect_db(self):
    self.cursor = self.cur_db.cursor()

  def use_query(self, query):
      self.cursor.execute(query)
      self.result = self.cursor.fetchall()
      self.cur_db.commit()
  def return_result(self):
    return self.result    
