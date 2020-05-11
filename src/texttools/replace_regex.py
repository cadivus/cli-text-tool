import argparse
import re

argparse_help="Replaces \"Old Regex\" with \"New\" in text"
argparse_name='--replace-regex'
argparse_nargs = 2
argparse_metavar=('Old', 'New')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      replace_regex(namespace, values[0], values[1])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def replace_regex(namespace, old_regex, new):
  """
  Remove string rem from text

  :param namespace: Namespace of parser
  :param old_regex: Old part-regex
  :param new: New part
  """
  namespace.text = re.sub(old_regex, new, namespace.text)

