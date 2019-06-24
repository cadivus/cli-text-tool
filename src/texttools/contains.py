import argparse

argparse_help="dings"
argparse_name='--contains'
argparse_nargs = 1
argparse_metavar=('Contains')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      contains(namespace, values[0])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def contains(namespace, cont):
  namespace.text = str(cont in namespace.text)

