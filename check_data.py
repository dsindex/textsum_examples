#!/bin/env python

import sys
sys.path.append('textsum')
import data

data_path = 'data/data'
for ret in data.ExampleGen(data_path, num_epochs=10) :
  print ret

