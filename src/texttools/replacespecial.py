import argparse

argparse_help="dings"
argparse_name='--replacespecial'
argparse_nargs = 0


def register_to_parser(parser):
  class ArgparseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
      replacespecial(namespace)

  parser.add_argument(argparse_name, action=ArgparseAction, help=argparse_help,
      nargs=argparse_nargs)


def replacespecial(namespace):
  namespace.text = namespace.text.replace(' ', '_')
  namespace.text = namespace.text.replace('ä', 'ae')
  namespace.text = namespace.text.replace('ö', 'oe')
  namespace.text = namespace.text.replace('ü', 'ue')
  namespace.text = namespace.text.replace('Ä', 'Ae')
  namespace.text = namespace.text.replace('Ö', 'Oe')
  namespace.text = namespace.text.replace('Ü', 'Ue')
  namespace.text = namespace.text.replace('ß', 'ss')
  

