#!/usr/bin/env python3

import argparse
from texttools import selectsplit
from texttools import contains
from texttools import replacespace
from texttools import replacespecial
from texttools import remove
from texttools import replace

parser = argparse.ArgumentParser()
parser.add_argument('text', help='Text')

selectsplit.register_to_parser(parser)
contains.register_to_parser(parser)
replacespace.register_to_parser(parser)
replacespecial.register_to_parser(parser)
remove.register_to_parser(parser)
replace.register_to_parser(parser)

args = parser.parse_args()

print(args.text)
