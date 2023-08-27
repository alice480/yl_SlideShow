import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import requests

SCREEN_SIZE = [450, 450]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Слайд-шоу')
        self.image = QLabel(self)
        self.photoes()
        self.count = 0
        self.initUI()

    def photoes(self):
        map_request1 = "https://static-maps.yandex.ru/1.x/?ll=125.775645,39.050298&z=15&size=450,450&l=sat"
        response = requests.get(map_request1)
        self.map_file1 = "map1.png"
        with open(self.map_file1, "wb") as file:
            file.write(response.content)
        map_request2 = "https://static-maps.yandex.ru/1.x/?ll=12.492285,41.890441&z=17&size=450,450&l=sat"
        response = requests.get(map_request2)
        self.map_file2 = "map2.png"
        with open(self.map_file2, "wb") as file:
            file.write(response.content)
        map_request3 = "https://static-maps.yandex.ru/1.x/?ll=31.134179,29.979392&z=15&size=450,450&l=sat"
        response = requests.get(map_request3)
        self.map_file3 = "map3.png"
        with open(self.map_file3, "wb") as file:
            file.write(response.content)
        map_request4 = "https://static-maps.yandex.ru/1.x/?ll=55.132684,25.119016&z=12&size=450,450&l=sat"
        response = requests.get(map_request4)
        self.map_file4 = "map4.png"
        with open(self.map_file4, "wb") as file:
            file.write(response.content)
        map_request5 = "https://static-maps.yandex.ru/1.x/?ll=38.204763,44.421812&z=17&size=450,450&l=sat"
        response = requests.get(map_request5)
        self.map_file5 = "map5.png"
        with open(self.map_file5, "wb") as file:
            file.write(response.content)
        self.pictures = [self.map_file1, self.map_file2, self.map_file3, self.map_file4, self.map_file5]

    def initUI(self):
        self.pixmap = QPixmap(self.pictures[self.count])
        self.image.move(0, 0)
        self.image.resize(450, 450)
        self.image.setPixmap(self.pixmap)
        self.counter_installing()

    def keyPressEvent(self, event):
        if event.key():
            self.image.clear()
            self.initUI()

    def counter_installing(self):
        if self.count == 4:
            self.count = 0
        else:
            self.count += 1

    def closeEvent(self, event):
        os.remove(self.map_file1)
        os.remove(self.map_file2)
        os.remove(self.map_file3)
        os.remove(self.map_file4)
        os.remove(self.map_file5)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
