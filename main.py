from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QHeaderView, QPushButton, QFileDialog, QTableWidgetItem, QSpinBox

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

        self.load_button = QPushButton("Load grades file")
        self.load_button.clicked.connect(self.load_file)
        self.main_layout.addWidget(self.load_button)

        self.file_label = QLabel("No file selected")
        self.main_layout.addWidget(self.file_label)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.main_layout.addWidget(self.table)

        self.bonus_label = QLabel("Bonus points — press Enter to apply")
        self.main_layout.addWidget(self.bonus_label)

        self.bonus_input = QSpinBox()
        self.bonus_input.setRange(0, 100)
        self.main_layout.addWidget(self.bonus_input)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select grades file", "","CSV files (*.csv)")
        if file_name:
            self.selected_file = file_name
            self.file_label.setText(file_name)
            self.student_ids = []
            self.original_grades = []
            self.corrected_grades = []

            with open(self.selected_file, "r") as f:
                next(f)
                for line in f:
                    parts = line.split(",")
                    self.student_ids.append(parts[0])
                    self.original_grades.append(int(parts[1]))
                    self.corrected_grades.append(int(parts[1]))
            self.update_table()

    def update_table(self):
        self.table.clearContents()
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(self.student_ids[row]))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))


if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()