import modes.py as modes
import sys

if __name__ == '__main__':
    args = sys.argv
    if args[0] in modes.methods and len(args)>2:
        eval(f"modes.{args[0]}({[i for i in args[1:-1]]})")
