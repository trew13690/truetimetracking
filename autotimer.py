from time import sleep
import json
import os, sys, signal
import subprocess


def signal_handler(signal, frame):
    print('\npProgram exiting gracefully')
    sys.exit(1)


class Application:

    def __init__(self):
        self.version = '0.0.1'

    def start(self):
        self.__main_loop()

    def __main_loop(self):
        while True:
            try:
                print('Recording what your doing!!!')
                windowpid = subprocess.run(["xdotool", "getactivewindow"], stdout=subprocess.PIPE)

                windowpid_clean = windowpid.stdout.decode('ASCII').replace('\n', '')
                print(windowpid_clean)

                windowname = subprocess.run(['xdotool', 'getwindowname', windowpid_clean], stdout=subprocess.PIPE)
                windowname = windowname.stdout.decode().replace('\n', '')

                log_data = self.open_log()

                if windowname in log_data.keys():
                    log_data[windowname] = log_data[windowname] + 1
                else:
                    log_data[windowname] = 1

                print(log_data, '\n\n')
                self.write_data(log_data)
                sleep(1)
            except KeyboardInterrupt:
                signal.signal(signal.SIGINT, signal_handler)

            except Exception as ex:
                print(ex)

    def write_data(self, log_data):
        with open('record.json', 'w') as f:
            json.dump(log_data, f, indent=4)

    def open_log(self):
        data = None
        with open('record.json', 'r+') as f:
            data = json.load(f)
        return data


timerApp = Application()
timerApp.start()
