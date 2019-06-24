import argparse

argparse_help="Replaces \"Old\" with \"New\" in text"
argparse_name='--replace'
argparse_nargs = 2
argparse_metavar=('Old', 'New')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      replace(namespace, values[0], values[1])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def replace(namespace, old, new):
  """
  Remove string rem from text

  :param namespace: Namespace of parser
  :param old: Old part
  :param new: New part
  """
  namespace.text = namespace.text.replace(old, new)

