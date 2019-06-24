import argparse

argparse_help="dings"
argparse_name='--replacespace'
argparse_nargs = 0


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      replacespace(namespace)

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs)


def replacespace(namespace):
  namespace.text = namespace.text.replace(' ', '_')

