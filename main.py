from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""

        self.setWindowTitle("Grades Correction")
        self.resize(900, 650)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout(central_widget)

        self.title_label = QLabel("Grades Correction")
        self.title_label.setObjectName("title")
        self.main_layout.addWidget(self.title_label)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.main_layout.addWidget(self.table)

if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()