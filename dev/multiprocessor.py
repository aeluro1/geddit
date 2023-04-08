import requests
import multiprocessing as mp

from download import Downloader

headers = {}

class Worker(mp.Process):
    def __init__(self, jobs):
        super().__init__()
        self._jobs = jobs
        self._downloader = Downloader()

    def run(self):
        while True:
            url = self._jobs.get()
            if url is None:
                break

        req = url.strip()

        try:
            pass
            # requests with allow_redirects = True, headers
        except Exception as e:
            print(str(e))

class Master():

    def __init__(self, jobs, num_workers):
        num_workers = mp.cpu_count()

        failed_posts = mp.Manager().dict()
        succeeded_posts = mp.Manager.dict()

        iolock = mp.Lock()

        jobs = mp.Queue()
        results = mp.Queue()

        workers = []
        for i in range(num_workers):
            workers.append(Worker(jobs, results))
            workers[i].start()
        
        for i in len(workers):
            jobs.put(None)

        while True:
            results.get()
            if jobs.empty():
                break

        for i in num_workers:
            workers[i].join()
        
        jobs.join()



########

from itertools import repeat
import multiprocessing as mp
import os
import pprint

def f(d: dict) -> None:
    pid = os.getpid()
    d[pid] = "Hi, I was written by process %d" % pid

if __name__ == '__main__':
    with mp.Manager() as manager:
        d = manager.dict()
        with manager.Pool() as pool:
            pool.map(f, repeat(d, 10))
        # `d` is a DictProxy object that can be converted to dict
        pprint.pprint(dict(d))