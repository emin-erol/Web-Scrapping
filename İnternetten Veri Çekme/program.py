import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class VideoPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 854, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_widget = QVideoWidget()
        self.video_widget.setMinimumSize(854, 480)
        self.layout.addWidget(self.video_widget)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        self.play_button = QPushButton("Play Video")
        self.play_button.clicked.connect(self.play_video)
        self.layout.addWidget(self.play_button)

    def play_video(self):
        video_url = "https://www.youtube.com/watch?v=VIDEO_ID"  # Video ID'sini buraya girin
        media_content = QMediaContent(QUrl(video_url))
        self.media_player.setMedia(media_content)
        self.media_player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoPlayerWindow()
    window.show()
    sys.exit(app.exec_())

