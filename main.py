from PySide6.QtWidgets import QApplication, QVBoxLayout, QGridLayout, \
    QLineEdit, QPushButton, QLabel, QWidget, QComboBox ,QMainWindow, \
    QTableWidget, QTableWidgetItem

from PySide6.QtGui import QAction

import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        # Menu Bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        #Create Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)


    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        #print(list(result)) #How to print the results to see\

        self.table.setRowCount(0) # Refresh the cursor to the beginning

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        connection.close()




app = QApplication(sys.argv)
speed_calculator = MainWindow()
speed_calculator.show()
speed_calculator.load_data()
sys.exit(app.exec())