#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--separator")
separator = parser.parse_args()

print(separator.separator)
