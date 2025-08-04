import sys

from Diversos.sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])