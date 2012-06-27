#!/usr/bin/python

import sqlite3 as lite
import shutil
import sys
import os

dbfile = "/Volumes/Data/mobile/Library/SMS/sms.db"
tmpdbfile = "/tmp/iex_tmp.db"

def init():
	shutil.copy(dbfile,tmpdbfile)


def clean():
	os.remove(tmpdbfile)

def print_sms():

	init()

	con = lite.connect(tmpdbfile)
	
	with con:

		cur = con.cursor()
		cur.execute("SELECT * from message")

		rows = cur.fetchall()

		for row in rows:
			print row

	clean()
