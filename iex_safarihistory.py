#!/usr/bin/python


from iex_base import iExBase

import sqlite3 as lite
import shutil
import sys
import os

import urlparse
import re, urllib

class iExSafariHistory(iExBase):

	dbfile = "/Volumes/Data/mobile/Library/Safari/History.plist"

	def db_print(self):
		self.db_init()

		f = open(self.tmpdbfile, 'r')
		#print f.read()


		GRUBER_URLINTEXT_PAT = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

		line = f.read()
		urls = [ mgroups[0] for mgroups in GRUBER_URLINTEXT_PAT.findall(line) ]

		for url in urls:
			print url

		self.db_clean()
