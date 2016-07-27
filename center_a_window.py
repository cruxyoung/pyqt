import sys
# QDesktopWidget提供了桌面窗口的信息，包含了屏幕尺寸
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(250,150)
        # 窗口剧中法制的代码在自定义的center（）方法中
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 获得主窗口的一个举行特定几何图形，包含了窗口的框架
        qr = self.frameGeometry()
        # 算出相对于显示器的绝对值，并从这个值中获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 举行已经设置好了宽和高，现在把矩形的中心点设置到屏幕的中间去，矩形的大小并不会改变
        qr.moveCenter(cp)
        # 移动了应用窗口的左上方的点到qr矩形的左上方的点，因此剧中显示在我们的屏幕上
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())