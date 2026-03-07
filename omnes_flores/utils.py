import sys
from datetime import datetime

disable_log = False

def set_disable_log(flag: bool):
    global disable_log
    disable_log = flag

def print_log(text):
    global disable_log
    if not disable_log:
        print(f"\033[46m[omnes-flores] {datetime.now().strftime("%Y/%m/%d-%H:%M:%S.%f")[:-3]} {text}\033[0m", file=sys.stderr)
