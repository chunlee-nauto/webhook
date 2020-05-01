import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('value', help='some value')

args = parser.parse_args()

print ('value={}'.format(args.value))
