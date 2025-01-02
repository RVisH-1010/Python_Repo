print("day 6 of py tut...")
# 1.cmmd line utility argpass
import argparse

parser = argparse.ArgumentParser()
# add cmmd line
parser.add_argument("url", help="url of the file to dowload")
parser.add_argument("output" , help="nmae of file to save ")
# parse the  argument
args = parser.parse_args()
# use arguments in the code
print(args.url)
print(args.output)
