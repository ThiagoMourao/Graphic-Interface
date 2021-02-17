import sys
from controler import new_img
from PyQt5.QtWidgets import QApplication
from interface.app_calculator import Calculator


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculator = new_img()
    calculator.show()
    qt.exec_()