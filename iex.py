#!/usr/bin/python

from iex_addressbook import iExAddressBook
from iex_sms import iExSms
from iex_call import iExCall
from iex_safaribookmarks import iExSafariBookmarks
from iex_safarihistory import iExSafariHistory

ab = iExAddressBook()
ab.db_print()

sms = iExSms()
sms.db_print()

call = iExCall()
call.db_print()

bm = iExSafariBookmarks()
bm.db_print()

#sh = iExSafariHistory()
#sh.db_print()
