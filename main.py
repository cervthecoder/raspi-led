# Vyřešit přijímání argumentu, aby se nemuselo přepisovat modes.py

import modes
import sys

if __name__ == '__main__':
    args = sys.argv
    args = [str(arg) for arg in args]
    args1 = [arg+", " for arg in args[2:-1]]
    args = [args[1]] + args1 + [args[-1]]
    print(args)
    if args[0] != args[1]:
        if args[0] == 'simple_color':
            args = sys.argv
            args = [str(arg) for arg in args]
            color = args[2]
            print(f"modes.simple_color(color, {args[3]})")
            eval(f"modes.simple_color(color, {args[3]})", {"color":color})
        if args[0] in modes.methods():
            arg = ''.join(args[1:])
            print(f"modes.{args[0]}({arg})")               
            eval(f"modes.{args[0]}({arg})")
    elif args[0] == args[1]:
            eval(f"modes.{args[0]}()")
    elif args[0]=="help":
            print("help message")

