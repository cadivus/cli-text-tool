import argparse

argparse_help="Sets text to \"True\" if text contains string or to \"False\" if not."
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
  """
  Sets text to "True" if namespace.text contains string cont or to "False" if not.

  :param namespace: Namespace of parser
  :param cont: check for this string
  """
  namespace.text = str(cont in namespace.text)

