# Vyřešit přijímání argumentu, aby se nemuselo přepisovat modes.py

import modes
import sys

if __name__ == '__main__':
    args = sys.argv
    args = [str(arg) for arg in args]
    try:
        if args[0] in modes.methods:
            eval(f"modes.{args[0]}("".join({args[1:]}))")
        elif args[0]=="help":
            print("help message")
    except:
        print("An error occurred try raspi-led -h")
