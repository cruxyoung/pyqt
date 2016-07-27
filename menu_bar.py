#menu_bar

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    # 创建一个菜单项的菜单栏，这个菜单项包含一个选中后中断应用的动作
    def initUI(self):
        # QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为
        # 创建了一个有指定图标，文本位exit的标签，还未这个动作了定义了一个快捷键。
        exitAction = QAction(QIcon('exit.png'),'&Exit', self)
        # 快捷键
        exitAction.setShortcut('Crtl+Q')
        # 当鼠标赋予菜单项智商就会显示的一个状态提示
        exitAction.setStatusTip('Exit application')
        # 选中特定的动作（exit），一个触发信号会被发射，信号连接到QApplication组件的quit（）方法
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        # menuBar（）创建了一个菜单栏
        menubar = self.menuBar()
        # 然后创建一个file菜单
        fileMenu = menubar.addMenu('&File')
        # 将退出动作添加到file菜单中。
        fileMenu.addAction(exitAction)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())