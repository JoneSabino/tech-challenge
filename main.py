import sys
from datetime import timedelta
from ripple import Ripple
from timeloop import Timeloop
import os
import var

tl = Timeloop()

count = 0


@tl.job(interval=timedelta(seconds=1))
def run_job():
    """
    Function that runs the all the routine with the periodicity specified in the decorator
    """

    global count
    r = Ripple()
    print('\nProcess started\n') if count == 0 else print('-----')
    response = r.get_server_info()
    values = r.get_values(response)
    print('API call number: ', count+1)
    r.calculate_time(values, count)
    r.write_csv(values)
    count += 1
    if count == var.MAX:
        print('Job finished successfully')
        os._exit(0)  # This is for Windows only, I guess. For UNIX like OS, use sys.exit('message')


if __name__ == '__main__':
    tl.start(block=True)








