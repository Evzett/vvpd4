import sys

from PyQt5 import QtWidgets

from started_window import StartedWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    mainwindow = StartedWindow()
    mainwindow.setupUi(window)
    window.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()