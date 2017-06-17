from django.shortcuts import render

# Create your views here.
import sched, time
import thread

s = sched.scheduler(time.time, time.sleep)

def get_up_status():
    # Do stuff

    s.enter(60, 1, get_up_status)

def start_sched_job(fn_name, fn_args):
    s.enter(60, 1, fn_name, fn_args)
    thread.start(s.run())

