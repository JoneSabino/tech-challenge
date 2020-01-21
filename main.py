from datetime import timedelta
from ripple import Ripple
from timeloop import Timeloop

tl = Timeloop()


@tl.job(interval=timedelta(seconds=1))
def run_job():
    """
    Function that runs the all the routine with the periodicity specified in the decorator
    """
    print('Starting job')
    r = Ripple()
    response = r.get_server_info()
    values = r.get_values(response)
    r.write_csv(values)
    print('Job finished successfully')


if __name__ == '__main__':
    tl.start(block=True)








