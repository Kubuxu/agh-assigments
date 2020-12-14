import threading
import time

# solution is to define cannocnial ordering to locks

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
            first = min(self.left, self.right)
            print(f"Phil {self.n} is taking first fork {first}")
            locks[first].acquire()
            second = max(self.left, self.right)
            print(f"Phil {self.n} is taking right fork {second}")
            locks[second].acquire()
            print(f"Phil {self.n} is eating")
            time.sleep(0.1)
            print(f"Phil {self.n} is putting down left fork {second}")
            locks[second].release()
            print(f"Phil {self.n} is putting down right fork {first}")
            locks[first].release()
        print(f"Phil {self.n} finished eating")

phils = [Philosopher(n, n, (n+1)%5) for n in range(5)]

for i in range(5):
    phils[i].start()
