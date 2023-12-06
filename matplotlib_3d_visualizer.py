import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading
import random
import time


class RealTimeScatter:
    def __init__(self, connections):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.sc = self.ax.scatter([], [], [])
        self.x, self.y, self.z = [], [], []
        self.connections = connections
        self.lines = []

        self.ax.view_init(
            elev=-90, azim=-90
        )  # to make plot look like normal coords system

        # Setting axis labels
        self.ax.set_xlabel("X Axis")
        self.ax.set_ylabel("Y Axis")
        self.ax.set_zlabel("Z Axis")

    def update_plot(self):
        while True:
            self.sc._offsets3d = (self.x, self.y, self.z)
            if not self.lines:
                self.create_connections()
            for line, (start, end) in zip(self.lines, self.connections):
                line.set_data(
                    [self.x[start], self.x[end]], [self.y[start], self.y[end]]
                )
                line.set_3d_properties([self.z[start], self.z[end]])
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

    def create_connections(self):
        self.lines = []
        for start, end in self.connections:
            if (start > len(self.x) - 1) or (end > len(self.x) - 1):
                continue
            (line,) = self.ax.plot(
                [self.x[start], self.x[end]],
                [self.y[start], self.y[end]],
                [self.z[start], self.z[end]],
                "r-",
            )
            self.lines.append(line)
