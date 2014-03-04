#!/bin/python

import simplejson as json
# I use Python 2.6 and "import json" works for me
from pprint import pprint

json_data = open('1line.txt')

data = json.load(json_data)

pprint(data)

json_data.close()
