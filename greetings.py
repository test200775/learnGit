#!/usr/bin/python

import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--firstname", help="person first name",type=str,required=True)
parser.add_argument("--lastname", help="person last name",type=str,required=True)

args = parser.parse_args()

print("Welcome, %s %s\n" % (args.firstname,args.lastname))