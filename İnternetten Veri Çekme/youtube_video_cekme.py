import os
import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from pytube import YouTube
from ultralytics import YOLO

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("VİDEO İNDİRİCİ")
        self.setGeometry(200, 200, 750, 500)

        self.baslik = QLabel("VİDEO İNDİRİCİ", self)
        self.baslik.setStyleSheet("font-size: 22pt; font-weight: bold; border: 2px solid black; padding: 10px;")

        self.urlLabel = QLabel("Video URL:", self)
        self.urlLabel.setStyleSheet("padding: 4px; font-size: 10pt;")

        self.konumLabel = QLabel("Konum: ", self)
        self.konumLabel.setStyleSheet("padding: 14px; font-size: 10pt;")

        self.urlInput = QLineEdit(self)
        self.urlInput.setFixedSize(200, 40)
        self.urlInput.setPlaceholderText("URL girin")
        self.urlInput.setStyleSheet("font-size: 10pt;")

        self.konumInput = QLineEdit(self)
        self.konumInput.setFixedSize(200, 40)
        self.konumInput.setPlaceholderText("İndirilecek konum")
        self.konumInput.setStyleSheet("font-size : 10pt;")

        self.indirButton = QPushButton("İndir", self)
        self.indirButton.setStyleSheet("font-size: 10pt;")
        self.indirButton.setFixedSize(120, 40)
        self.indirButton.clicked.connect(self.videoIndir)

        self.acButton = QPushButton("Video'yu Aç", self)
        self.acButton.setStyleSheet("font-size: 10pt;")
        self.acButton.setFixedSize(120, 40)
        self.acButton.hide()
        self.acButton.clicked.connect(self.videoAc)

        self.uyari = QLabel(self)
        self.uyari.setStyleSheet("font-size: 10pt")

        layout = QVBoxLayout()

        h_box0 = QHBoxLayout()
        h_box0.addStretch()
        h_box0.addWidget(self.baslik)
        h_box0.addStretch()

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.urlLabel)
        h_box1.addWidget(self.urlInput)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.konumLabel)
        h_box2.addWidget(self.konumInput)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.indirButton)

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.uyari)
        h_box4.addStretch()

        h_box5 = QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.acButton)
        h_box5.addStretch()

        layout.addLayout(h_box0)
        layout.addStretch()
        layout.addLayout(h_box1)
        layout.addLayout(h_box2)
        layout.addLayout(h_box3)
        layout.addLayout(h_box4)
        layout.addLayout(h_box5)
        layout.addStretch()
        self.setLayout(layout)

    def videoIndir(self):
        if self.urlInput.text() and self.konumInput.text():
            link = YouTube(self.urlInput.text())
            self.video = link.streams.get_highest_resolution()
            self.video.download(self.konumInput.text())
            self.dizin = self.konumInput.text()
            self.urlInput.clear()
            self.konumInput.clear()
            self.uyari.setText("Video İndirme İslemi Basarili!")
            self.acButton.show()
        elif self.urlInput.text() and not self.konumInput.text():
            self.uyari.setText("Dosya yolunu giriniz!")
        elif not self.urlInput.text() and self.konumInput.text():
            self.uyari.setText("URL adresini giriniz!")
        else:
            self.uyari.setText("URL adresini ve dosya yolunu giriniz!")

    def videoAc(self):
        dosyalar = os.listdir(self.dizin)
        videoDosyasi = max(dosyalar, key=lambda dosya: os.path.getctime(os.path.join(self.dizin, dosya)))
        self.dosyaYolu = self.dizin + "\\" + videoDosyasi
        video = cv2.VideoCapture(self.dosyaYolu)
        model = YOLO('yolov8n.pt')
        ret = True
        while ret:
            ret, frame = video.read()
            # negatif = np.max(frame) - frame
            sonuc = model.predict(source=frame)

            cv2.imshow("Video", frame)
            cv2.imshow("Tahminler", sonuc)
            # cv2.imshow("Negatif Video", negatif)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                ret = False
        video.release()
        cv2.destroyAllWindows()


app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()

sys.exit(app.exec_())

