#!/usr/bin/python

import os
import sys
import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="person first name",type=str,required=True)
parser.add_argument("--lastname", help="person last name",type=str,required=True)
parser.add_argument("--address", help="person home address",type=str, default=None, required=False)
args = parser.parse_args()

print ("\n")
print ("***********************************")
print ("Current Date: %s" % datetime.datetime.now().strftime('%d/%m/%Y'))
print ("Current Time: %s" % datetime.datetime.now().strftime('%H:%M:%S %p'))
print ("***********************************")
print("\nWelcome, %s %s." % (args.firstname,args.lastname))

userResponse = raw_input ("How can I help you today?")

if userResponse is not None:
    print ("Your with is my command :) ...")

if userResponse.address is not None:
    print ("Your home address is: %s" % userResponse.address)