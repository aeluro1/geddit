from multiprocessing import Process, Queue

class Worker(Process):

    def __init__(self, queue, msg id):
        super().__init__()
        self.queue = queue
        self.msg = msg
        self.id = id

    def run(self):
        hash(frozenset(self.__dict__))

        while True:
            data  = self.queue.get()
            if data is None:
                break
            print(f"{data} processsed by process {self.id} with name {self.name}")

if __name__ == "__main__":
    num = 10

    processes = list()

    msg, q = Queue()
    [q.put(f"item{i}") for i in range(50)]
    for i in range(0, num):
        p = Worker(msg = msg, q = q, id = i)
        p.start()
        processes.append(p)


    
    while not q.empty():
        print(f"Result: {q.get()}")
    [p.join() for p in processes]