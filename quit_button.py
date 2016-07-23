import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__();

        self.initUI()

    def initUI(self):
        # 创建一个按钮， 构造（button显示的文本， 父组建（example（继承自QWidget）））
        qbtn = QPushButton('Quit',self)
        # 信号clicked被发送，QCoreApplication类包含了时间主循环，处理和转发所有事件
        # instance()返回一个实例化对象
        # 点击信号连接到quit，结束应用
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit Button')
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())