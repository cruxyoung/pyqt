
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message box')
        self.show()
# 点击关闭询问是否关闭
    def closeEvent(self, event):
        # 第一个字符串显示在标题栏上
        # 第二个字符串是对话框上显示的文本
        # 第三个参数指定了显示在对话框上的按钮集合
        # 最后是默认选中的按钮
        # 返回值被储存在reply变量中
        reply = QMessageBox.question(self,'Message',
                                     "Are you sure to quit?",QMessageBox.Yes|
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()

if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())