import sys
import csv
import pyqtgraph as pg
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
# from labwatching.model_test import data_analysis

pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class TabWidgetApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget Demo')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        hbox = QtWidgets.QHBoxLayout()
        self.layout.addLayout(hbox)

        self.plot_widget = pg.PlotWidget()


        self.tab_widget = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        self.layout.addWidget(self.tab_widget)

        self.initTab1()
        self.initTab2()
        self.initTab3()
        self.plot()


    def initTab1(self):
        layout = QtWidgets.QVBoxLayout(self.tab1)
        label = QtWidgets.QLabel("Content of Tab 1")
        layout.addWidget(self.plot_widget)
        layout.addWidget(label)

    def initTab2(self):
        layout = QtWidgets.QVBoxLayout(self.tab2)
        label = QtWidgets.QLabel("Content of Tab 2")
        layout.addWidget(label)

    def initTab3(self):
        layout = QtWidgets.QVBoxLayout(self.tab3)
        label = QtWidgets.QLabel("Content of Tab 3")
        layout.addWidget(label)

    def plot(self):
        """plots the sine function
        """
        self.plot_widget.clear()
        x = np.linspace(-np.pi, np.pi, 100)
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "m", "width": 5})
        self.plot_widget.setLabel("left", "y-axis [units]")
        self.plot_widget.setLabel("bottom", "x-axis [units]")
        #self.plot()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     tabWidgetApp = TabWidgetApp()
#     tabWidgetApp.show()
#     sys.exit(app.exec())

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = TabWidgetApp()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
