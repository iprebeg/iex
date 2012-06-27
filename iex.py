#!/usr/bin/python

#import iex_call
#import iex_sms

#iex_call.print_calls()
#iex_sms.print_sms()

from iex_addressbook import iExAddressBook
from iex_sms import iExSms
from iex_call import iExCall

ab = iExAddressBook()
ab.db_print()

sms = iExSms()
sms.db_print()

call = iExCall()
call.db_print()
