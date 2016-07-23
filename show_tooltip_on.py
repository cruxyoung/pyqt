import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import  QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 设置字体，用10px大小的SansSerif字体
        QToolTip.setFont(QFont('ansserif', 10))
        # 调用此方法创建提示框，并使用富文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个按钮，并设置一个提示框
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 改变按钮的大小和位置，sizehint给了按钮一个推荐的大小
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__=='__main__':

    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())