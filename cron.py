from crawl import crawl
import time
from apscheduler.schedulers.background import BackgroundScheduler

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(crawl, 'cron', hour = 7)
    scheduler.start()
    print('scheduler starts...')

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        print('shutdown')
        scheduler.shutdown()

