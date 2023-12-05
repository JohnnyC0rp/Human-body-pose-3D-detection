import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading
import random
import time

class RealTimeScatter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.sc = self.ax.scatter([], [], [])
        self.x, self.y, self.z = [], [], []

    def update_plot(self, new_frames):
        while True:
            self.x.append(random.random())
            self.y.append(random.random())
            self.z.append(random.random())

            self.sc._offsets3d = (self.x, self.y, self.z)
            plt.draw()
            time.sleep(0.1)

    def show(self):
        thread = threading.Thread(target=self.update_plot)
        thread.daemon = True
        thread.start()
        plt.show()

# if __name__ == "__main__":
#     plot = RealTimeScatter()
#     plot.show()
