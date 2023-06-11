import requests
import multiprocessing as mp

from download import Downloader

headers = {}

class Worker(mp.Process):
    def __init__(self, jobs, results):
        super().__init__()
        self._jobs = jobs
        self._results = results
        self._downloader = Downloader()

    def run(self):
        while True:
            url = self._jobs.get()
            if url is None:
                self._results.put(None)
                break

            try:
                self._results.put("Success")
                pass
                # requests with allow_redirects = True, headers
            except Exception as e:
                print(str(e))

class Listener(mp.Process):
    """Process for recording downloaded data to file with multiprocessing support"""
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def run(self):
        with open("temp.txt", "w") as f:
            while True:
                item = self._queue.get()
                if item is None:
                    break

        # return some value as an asyncresult


class Master():

    def __init__(self, jobs, num_workers):
        num_workers = mp.cpu_count()
        manager = mp.Manager()

        failed_posts = manager.dict()
        succeeded_posts = manager.dict()
        counter = manager.Value()

        jobs = manager.Queue()
        results = manager.Queue()

        listener = Listener(results)
        listener.start()

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
        
        jobs.join() # Wait for process to terminate; if using pool, need to use close() beforehand to stop accepting new jobs
        listener.join()