import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):
        # QInputDialog提供了一个简单便利的对话框用于从用户哪儿获得一个值，输入可以是字符串，数字，或者一个列表中的列表项
        # 显示一个输入对话框。第一个字符串参数是对话框的标题，二是对话框内的消息文本，对话框返回输入的文本值和一个布尔值
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        if ok:
            # 把从对话框接受到的文本设置到单行编辑框组件上显示
            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())