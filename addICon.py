import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

#qwidget是所有用户界面类的基础类，默认构造方法没有父类，没有父类的widget作为窗口使用
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # 将窗口在屏幕上显示，并设置了他的尺寸，分别是（x轴位置，y轴位置，窗口的宽度，窗口的高度）
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        # 设置显示的icon
        self.setWindowIcon(QIcon('web.png'))

        self.show()

if __name__ == '__main__':
    # 所有的qt必须创建一个application应用
    app=QApplication(sys.argv)
    #
    ex = Example()
    sys.exit(app.exec_())





# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     调整widget组建的大小
#     w.resize(250,150)
#     widget组建出现的位置
#     w.move(30,300)
#     给窗口增加title
#     w.setWindowTitle('Simple')
#     显示出widget组建， widget对象在这里第一次被内存中创建，并在屏幕上显示
#     w.show()
#     应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
# exec_()方法有一个下划线。因为exec是Python保留关键字。因此，用exec_()来代替
#     sys.exit(app.exec_())