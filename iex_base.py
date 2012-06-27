#!/usr/bin/python


import sqlite3 as lite
import shutil
import sys
import os

class iExBase(object):

	dbfile = "empty"
	tmpdbfile = "/tmp/iex_tmp.db"

	def __init__(self):
		print "init"

	def db_init(self):
		shutil.copy(self.dbfile,self.tmpdbfile)

	def db_clean(self):
		os.remove(self.tmpdbfile)

	def db_print(self):
		print "empty"
