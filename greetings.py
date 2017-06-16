#!/usr/bin/python

import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="person full name",type=str,required=True)

args = parser.parse_args()

if args.name:
    print("Welcome, %s\n" % args.name)