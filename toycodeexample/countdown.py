from datetime import datetime, timedelta
from time import sleep

def countdown(seconds=6):
    t0 = datetime.now()
    for sec in range(seconds):
        print("{:3d}/{:3d}: {}".format(seconds- sec, seconds, datetime.now()))
        tnext = t0 + timedelta(seconds=sec+1)
        sleep((tnext - datetime.now()).total_seconds())

    print("{:3d}/{:3d}: {}".format(0, seconds, datetime.now()))
