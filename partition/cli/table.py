import sys

from PIL import Image
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QColor
from PyQt5.QtWidgets import QTableView, QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, \
    QApplication, QHBoxLayout, QFileDialog

from partition.utils.constants import group
from partition.utils.random_utils import partition


def get_max_len(ls):
    return max(set(map(lambda a: len(a[1]), ls)))


def read_pix_size(image_path):
    img = Image.open(image_path)
    img_size = img.size  # 图片的长和宽
    return img_size[0], img_size[1]


def num_to_char(num):
    """数字转中文"""
    num = str(num)
    new_str = ""
    num_dict = {"0": u"零", "1": u"一", "2": u"二", "3": u"三", "4": u"四", "5": u"五", "6": u"六", "7": u"七", "8": u"八",
                "9": u"九"}
    listnum = list(num)
    shu = []
    for i in listnum:
        shu.append(num_dict[i])
    new_str = "".join(shu)
    return new_str


class WindowClass(QWidget):
    def read_file_path(self):
        # directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")   #起始路径
        # print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                          "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔
        return fileName1

    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)
        self.layout = QHBoxLayout()
        path = self.read_file_path()
        if "".__eq__(path):
            print("未曾指定数据文件")
            exit(0)

        data = partition(path)
        row = get_max_len(data)
        # palette.setColor(QPalette.Background, QColor(0, 0, 0, 255))
        # palette.setColor(QPalette.Background, QColor(0x00, 0xff, 0x00, 0x00))
        tableWidget = QTableWidget()
        palette = tableWidget.palette()
        p = self.read_file_path()
        back_ground = "resource/木棉.jpg" if "".__eq__(p) else p
        palette.setBrush(QPalette.Window, QBrush(QPixmap(back_ground)))
        wid, high = read_pix_size(back_ground)
        self.resize(wid, high)
        # 设置透明背景
        palette.setBrush(QPalette.Base, QBrush(QColor(255, 255, 255, 0)))
        self.setPalette(palette)

        # tableWidget.setAutoFillBackground(True)

        # tableWidget.setStyleSheet("background-color:#F76677")
        tableWidget.verticalHeader().setDefaultSectionSize(45)
        tableWidget.setRowCount(12)
        # vertical_palette = tableWidget.verticalHeader().palette()
        # vertical_palette.setBrush(QPalette.Base, QBrush(QColor(255, 255, 255, 0)))
        tableWidget.verticalHeader().setPalette(palette)

        tableWidget.setRowCount(row)  # 行数
        tableWidget.setColumnCount(group)  # 列数
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        tableWidget.horizontalHeader().setHidden(True)  # 表格首行隐藏
        tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        # tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
        tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # textFont = QFont("song", 8, QFont.Bold)
        textFont = QFont("Microsoft YaHei", 11)
        tableWidget.setFont(textFont)

        # 不显示表边框
        tableWidget.setShowGrid(False)

        self.layout.addWidget(tableWidget)

        ls = []
        for i in range(1, row + 1):
            ls.append(i)

        columns = list(map(lambda s: (str(s[0])) + "麦", data))
        rows = list(map(lambda s: num_to_char(s) + "组", ls))
        tableWidget.setHorizontalHeaderLabels(columns)
        tableWidget.setVerticalHeaderLabels(rows)
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        for i in range(len(data)):  # 注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
            members = data[i][1]
            for m in range(len(members)):
                item = QTableWidgetItem(members[m])
                # item.setTextColor(QColor("red"))
                tableWidget.setItem(m, i, item)
                self.setLayout(self.layout)


def run():
    app = QApplication(sys.argv)
    win = WindowClass()
    win.setAutoFillBackground(True)
    desktop = QApplication.desktop()
    screen = desktop.screenGeometry()
    win.move((screen.width() - win.width()) / 2, (screen.height() - win.height()) / 2)
    # 设置窗口的标题
    win.setWindowTitle("木棉棉的春天 ~ ")
    # win.setWindowIcon(QIcon("./images/myappico.ico"))
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
