import argparse

argparse_help="dings"
argparse_name='--remove'
argparse_nargs = 1
argparse_metavar=('Remove')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      remove(namespace, values[0])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def remove(namespace, rem):
  namespace.text = namespace.text.replace(rem, '')

