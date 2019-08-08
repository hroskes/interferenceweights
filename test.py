#!/usr/bin/env python

from sample import Sample

couplings = {
  "ghv1": 0,
  "ghz2": 1,
  "ghw2": 1,
  "ghz4": 1,
  "ghw4": 1,
  "ghz1prime2": 0,
  "ghw1prime2": 0,
  "ghzgs1prime2": 0,
}

print Sample("VBF", **couplings).weight
