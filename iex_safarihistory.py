#!/usr/bin/python


from iex_base import iExBase

import sqlite3 as lite
import shutil
import sys
import os

class iExSafariHistory(iExBase):

	dbfile = "/Volumes/Data/wireless/Library/CallHistory/call_history.db"

	def db_print(self):
		self.db_init()
		con = lite.connect(self.tmpdbfile)
		with con:
			cur = con.cursor()
			cur.execute("SELECT * from call")
			rows = cur.fetchall()
			for row in rows:
				print row
		
		self.db_clean()
