#!/usr/bin/python

from iex_addressbook import iExAddressBook
from iex_sms import iExSms
from iex_call import iExCall
from iex_safaribookmarks import iExSafariBookmarks
from iex_safarihistory import iExSafariHistory

#ab = iExAddressBook()
#sms = iExSms()
#call = iExCall()
#bm = iExSafariBookmarks()
sh = iExSafariHistory()

#ab.db_print()
#sms.db_print()
#call.db_print()
#bm.db_print()
sh.db_print()
