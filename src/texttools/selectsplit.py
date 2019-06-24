import argparse

argparse_help="Splits text at SplitString and selects SelectPart (number)"
argparse_name='--selectsplit'
argparse_nargs = 2
argparse_metavar=('SelectPart', 'SplitString')


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      selectsplit(namespace, values[0], values[1])

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs, metavar=argparse_metavar)


def selectsplit(namespace, select, split):
  """
  Splits text at "split" (string) and selects "select" (number)

  :param namespace: Namespace of parser
  :param select: Select this part (number)
  :param split: Split here (string)
  """
  select = int(str(select))
  namespace.text = namespace.text.split(split)[select]

