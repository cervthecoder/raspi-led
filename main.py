# Vyřešit přijímání argumentu, aby se nemuselo přepisovat modes.py

import modes
import sys

if __name__ == '__main__':
    args = sys.argv.remove('main.py')
    print(args)
    print(args)
    args = [str(arg) for arg in args]
    args1 = [arg+", " for arg in args[1:-1]]
    args = args1 + [args[-1]]
    print(args)
    try:
        if args[0] in modes.methods():
            eval(f"modes.{args[0]}("".join({args[1:]}))")
        elif args[0]=="help":
            print("help message")
    except:
        raise(ValueError)
