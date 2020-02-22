import os, sys, signal
import json
from time import sleep



def signal_handler(signal, frame):
    print('\npProgram exiting gracefully')
    sys.exit(1)

class Stats:

    def __init__(self):
        self.write_stats()

    def readFile(self):
        with open('record.json', 'r+') as f:
            data = json.load(f)
        return data
    def write_stats(self):
        data = self.readFile()
        print('='*90)
        print('\n')
        for record in data:
            mins = str(int(data[record])/60)
            print('Activity:', record, '\nMins:', mins,'\n')
        print('='*90)
while True:
    try:
        stats = Stats()
        sleep(60)
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, signal_handler)
    except Exception as ex:
        print(ex)