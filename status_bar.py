#status bar
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 调用了QtGui.QMainWindow类的statusBar（）方法，创建了一个状态栏，
        # 随后方法方法返回状态栏对象，然后用showMessage（）方法在状态栏上显示信息
        self.statusBar().showMessage('Ready')

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('statusbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())