import sys
import csv
import pyqtgraph as pg
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtGui import QKeySequence, QShortcut
#from labwatching.model_test import data_analysis

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

        self.hbox = QtWidgets.QHBoxLayout()




        self.tab_widget = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()

        self.tab_widget.addTab(self.tab4, "overzicht, menu")
        self.tab_widget.addTab(self.tab1, "grafiek")
        self.tab_widget.addTab(self.tab2, "Tab opslaan")
        self.tab_widget.addTab(self.tab3, "Tab 4")


        self.layout.addWidget(self.tab_widget)
        
        self.initTab4()
        self.initTab1()
        self.initTab2()
        self.initTab3()


        self.key_binding()

        self.short_cut()


    def initTab4(self):
        layout = QtWidgets.QVBoxLayout(self.tab4)
        label = QtWidgets.QLabel("Content of Tab 1")

        self.textedit = QtWidgets.QTextEdit()
        self.textedit.append("Alt 1,2,3,4 is tab bladen")
        self.textedit.append("ctrl+s = data oplaan")
        self.textedit.append("alt+c plot weg")
        
        layout.addWidget(self.textedit)


    def initTab1(self):
        layout = QtWidgets.QVBoxLayout(self.tab1)
        label = QtWidgets.QLabel("Content of Tab 1")
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        layout.addWidget(label)
        self.plot()

    def initTab2(self):
        layout = QtWidgets.QVBoxLayout(self.tab2)
        label = QtWidgets.QLabel("Content of Tab 2")
        save_button = QtWidgets.QPushButton("save")
        
        layout.addWidget(save_button)
        save_button.clicked.connect(self.save_data)
        layout.addWidget(label)

    def initTab3(self):
        label = QtWidgets.QLabel("Content of Tab 3")
        layout = QtWidgets.QHBoxLayout(self.tab3)
        layout.addWidget(label)


        textedit = QtWidgets.QTextEdit("text")
        textedit.append("kies wat je bij je meting wil")


        
        group_box = QtWidgets.QGroupBox("Group Box")
        group_layout = QtWidgets.QVBoxLayout(group_box)

        option_1 = QtWidgets.QCheckBox("wel onzekerheid")
        option_2 = QtWidgets.QCheckBox("iets anders")
        option_1.setChecked(True)

        
        group_layout.addWidget(option_1)
        group_layout.addWidget(option_2)




        layout.addWidget(group_box)
        layout.addWidget(textedit)
        group_box.setLayout(group_layout)

    def plot(self):
        """plots the sine function
        """
        self.plot_widget.clear()
        x = np.linspace(-np.pi, np.pi, 100)
        self.plot_widget.plot(x, np.sin(x), symbol=None, pen={"color": "m", "width": 5})
        self.plot_widget.setLabel("left", "y-axis [units]")
        self.plot_widget.setLabel("bottom", "x-axis [units]")

    def key_binding(self):
        for i in range(self.tab_widget.count()):
            shortcut = QShortcut(QKeySequence(f"Alt+{i+1}"), self)  # Use QShortcut from QtGui
            shortcut.activated.connect(lambda i=i: self.tab_widget.setCurrentIndex(i))

    def short_cut(self):
        shortcut_shift_w = QShortcut(QKeySequence("Shift+w"), self)
        shortcut_shift_w.activated.connect(self.add_text_button_clicked)

        shortcut_clear = QShortcut(QKeySequence("Alt+c"), self)
        shortcut_clear.activated.connect(self.plot_remover)

        shortcut_save = QShortcut(QKeySequence("Ctrl+s"), self)
        shortcut_save.activated.connect(self.save_data)

    def plot_remover(self):
        self.plot_widget.clear()

    def add_text_button_clicked(self):
        self.textedit.append("You clicked me.")


    @Slot()
    def save_data(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)    
            writer.writerow(['Hz', 'Hz_std', 'fWHM', 'amp'])
            for a, b, c, d, in zip(self.frequentie, self.std, self.FWHM, self.ampl):
                writer.writerow([a, b, c, d])
def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = TabWidgetApp()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
