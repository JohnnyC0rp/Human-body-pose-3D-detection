import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading
import random
import time


class RealTimeScatter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.sc = self.ax.scatter([], [], [])
        self.x, self.y, self.z = [], [], []

    def update_plot(self):
        while True:
            self.sc._offsets3d = (self.x, self.y, self.z)
            plt.draw()
            time.sleep(0.1)

    def show(self):
        thread = threading.Thread(target=self.update_plot)
        thread.daemon = True
        thread.start()
        plt.show()

    def load_new_landmarks(self, landmarks):
        if landmarks:
            self.x, self.y, self.z = [], [], []
            for landmark in landmarks:
                self.x.append(landmark.x)
                self.y.append(landmark.y)
                self.z.append(landmark.z)


# if __name__ == "__main__":
#     plot = RealTimeScatter()
#     plot.show()
