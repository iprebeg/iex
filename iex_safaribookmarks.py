#!/usr/bin/python


from iex_base import iExBase

import sqlite3 as lite
import shutil
import sys
import os

class iExSafariBookmarks(iExBase):

	dbfile = "/Volumes/Data/mobile/Library/Safari/Bookmarks.db"

	def db_print(self):
		self.db_init()
		con = lite.connect(self.tmpdbfile)
		with con:
			cur = con.cursor()
			cur.execute("SELECT * from bookmarks")
			rows = cur.fetchall()
			for row in rows:
				print row
		
		self.db_clean()
