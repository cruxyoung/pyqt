import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout,QVBoxLayout,QApplication
# QHBoxLayout,QVBoxLayout是两个基础布局管理类，他们水平或垂直的线性排列组建，
# 为了一些必要的空白，同样需要一些拉伸因子
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 创建了两个按钮
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 创建一个水平箱布局
        hbox = QHBoxLayout()
        # 增加一个拉伸因子，这回酱按钮推到窗口的右边
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        # 把水平布局放置在垂直布局内
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
