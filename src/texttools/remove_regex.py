import argparse
import re

argparse_help="Removes string \"Remove\" from text"
argparse_name='--remove-regex'
argparse_nargs = 1
argparse_metavar=('Remove')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      remove_regex(namespace, values[0])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def remove_regex(namespace, rem_regex):
  """
  Remove string rem from text

  :param namespace: Namespace of parser
  :param rem-regex: Remove matching this string
  """
  namespace.text = re.sub(rem_regex, '', namespace.text)

