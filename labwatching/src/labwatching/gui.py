import sys
import csv
import pyqtgraph as pg
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
# from labwatching.model_test import data_analysis

# class UserInterface(QtWidgets.QMainWindow):
#     """
#     """
#     def __init__(self):
#         """
#         """
#         super().__init__()
#         central_widget = QtWidgets.QWidget()
#         self.setCentralWidget(central_widget)

#         self.data = data_analysis()

#         vbox = QtWidgets.QVBoxLayout(central_widget)

#         hbox = QtWidgets.QHBoxLayout()
#         vbox.addLayout(hbox)

#         self.plot_widget = pg.PlotWidget()
#         vbox.addWidget(self.plot_widget)


#         start_button = QtWidgets.QPushButton("Start")
#         vbox.addWidget(start_button)


#         save_button = QtWidgets.QPushButton("save")
#         vbox.addWidget(save_button)


# class MyTableWidget():
    
#     def __init__(self, parent):
#         super(QtWidgets.QWidget, self).__init__(parent)
#         self.layout = QtWidgets.QVBoxLayout(self)
        
#         # Initialize tab screen
#         self.tabs = QtWidgets.QTabWidget()
#         self.tab1 = QtWidgets.QWidget()
#         self.tab2 = QtWidgets.QWidget()
#         self.tabs.resize(300,200)
        
#         # Add tabs
#         self.tabs.addTab(self.tab1,"Tab 1")
#         self.tabs.addTab(self.tab2,"Tab 2")
        
#         # Create first tab
#         self.tab1.layout = QtWidgets.QVBoxLayout(self)
#         self.pushButton1 = QtWidgets.QPushButton("PyQt5 button")
#         self.tab1.layout.addWidget(self.pushButton1)
#         self.tab1.setLayout(self.tab1.layout)
        
#         # Add tabs to widget
#         self.layout.addWidget(self.tabs)
#         self.setLayout(self.layout)
        
#     @Slot()
#     def on_click(self):
#         print("\n")
#         for currentQTableWidgetItem in self.tableWidget.selectedItems():
#             print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     ui = UserInterface()
#     ui.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()  

class TabWidgetApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget Demo')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

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

    def initTab1(self):
        layout = QtWidgets.QVBoxLayout(self.tab1)
        label = QtWidgets.QLabel("Content of Tab 1")
        layout.addWidget(label)

    def initTab2(self):
        layout = QtWidgets.QVBoxLayout(self.tab2)
        label = QtWidgets.QLabel("Content of Tab 2")
        layout.addWidget(label)

    def initTab3(self):
        layout = QtWidgets.QVBoxLayout(self.tab3)
        label = QtWidgets.QLabel("Content of Tab 3")
        layout.addWidget(label)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tabWidgetApp = TabWidgetApp()
    tabWidgetApp.show()
    sys.exit(app.exec())