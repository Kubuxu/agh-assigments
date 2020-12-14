import threading
import time


locks = []
for i in range(5):
    l = threading.Lock()
    locks.append(l)


class Philosopher(threading.Thread):
    def __init__(self, n, left, right):
        threading.Thread.__init__(self)
        self.n = n
        self.left = left
        self.right = right

    def run(self):
        for i in range(30):
            print(f"Phil {self.n} is taking left fork {self.left}")
            locks[self.left].acquire()
            print(f"Phil {self.n} is taking right fork {self.right}")
            locks[self.right].acquire()
            print(f"Phil {self.n} is eating")
            time.sleep(0.1)
            print(f"Phil {self.n} is putting down right fork {self.right}")
            locks[self.right].release()
            print(f"Phil {self.n} is putting down left fork {self.left}")
            locks[self.left].release()
        print(f"Phil {self.n} finished eating")

phils = [Philosopher(n, n, (n+1)%5) for n in range(5)]

for i in range(5):
    phils[i].start()
