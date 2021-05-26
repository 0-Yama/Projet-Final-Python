import threading


class MyThread(threading.Thread):

    def __init__(self, nom, delai):
        self.delay = delai
        self.process_ended = False
        self.process_type = ''
        threading.Thread.__init__(self, name=nom)

    def initialise_process(self, type):
        self.process_type = type

    def kill_process(self):
        self.process_ended = True

    def run_process(self):
        pass