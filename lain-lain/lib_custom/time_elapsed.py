# ========================== FILE: time_elapsed.py ============================
#   Menghitung waktu eksekusi program
# -----------------------------------------------------------------------------
# Referensi:
# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/12344609
# =============================================================================

import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("\t\t%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*66
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("\t\t  Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = time()
atexit.register(endlog)
log("Start Program")
