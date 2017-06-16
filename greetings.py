#!/usr/bin/python

import os
import sys
import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="person first name",type=str,required=True)
parser.add_argument("--lastname", help="person last name",type=str,required=True)

args = parser.parse_args()

print ("Current Date: %s" % datetime.datetime.now().strftime('%d/%m/%Y'))
print("Welcome, %s %s\n" % (args.firstname,args.lastname))