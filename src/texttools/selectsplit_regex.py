import argparse
import re

argparse_help="Splits text at SplitString-regex and selects SelectPart (number)"
argparse_name='--selectsplit-regex'
argparse_nargs = 2
argparse_metavar=('SelectPart', 'SplitString-regex')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      selectsplit_regex(namespace, values[0], values[1])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def selectsplit_regex(namespace, select, split_regex):
  """
  Splits text at "split" (string) and selects "select" (number)

  :param namespace: Namespace of parser
  :param select: Select this part (number)
  :param split: Split regex here (string)
  """
  select = int(str(select))
  namespace.text = re.split(split_regex, namespace.text)[select]

