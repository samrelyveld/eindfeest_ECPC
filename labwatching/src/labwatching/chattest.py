from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QKeySequence, QShortcut

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hotkeys Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a QTabWidget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Create tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tabs to QTabWidget
        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        # Layout for Tab 1
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("This is Tab 1"))
        self.tab1.setLayout(tab1_layout)

        # Layout for Tab 2
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("This is Tab 2"))
        self.tab2.setLayout(tab2_layout)

        # Layout for Tab 3
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QLabel("This is Tab 3"))
        self.tab3.setLayout(tab3_layout)

        # Add shortcut for switching to Tab 2 using Alt+2
        shortcut_alt_2 = QShortcut(QKeySequence("Alt+2"), self)
        shortcut_alt_2.activated.connect(self.go_to_tab_2)

    def go_to_tab_2(self):
        """Switch to Tab 2."""
        self.tab_widget.setCurrentIndex(1)  # Tab indices start from 0

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
