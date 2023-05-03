from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import os

from youtube_process import YotubeProcess


class YoutubeDownloaderApp(QDialog):
    def __init__(self, parent=None):
        super(YoutubeDownloaderApp, self).__init__(parent)

        self.url_line = QLineEdit()
        self.url_line.setPlaceholderText("https://youtu.be/test") # Youtube video share link

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.clicked_start_button)

        self.dictionary_label = QLabel(str(os.getcwd()))
        self.dictionary_label.setWordWrap(True)

        self.dictionary_button = QPushButton("Select Folder")
        self.dictionary_button.clicked.connect(self.clicked_dictionary_button)

        self.video_check = QCheckBox("Video")
        self.mp3_check = QCheckBox("MP3")

        h_box = QHBoxLayout()
        h_box.addWidget(self.video_check)
        h_box.addWidget(self.mp3_check)

        grid = QGridLayout()
        grid.addWidget(self.url_line, 0, 0)
        grid.addWidget(start_button, 0, 1)
        grid.addWidget(self.dictionary_label, 1, 0)
        grid.addWidget(self.dictionary_button, 1, 1)
        grid.addLayout(h_box, 2, 0, 1, 2)

        self.setFixedSize(450, 150)
        self.setLayout(grid)

        self.count = 0

    def clicked_start_button(self):
        try:
            if self.video_check.isChecked() or self.mp3_check.isChecked():
                ytp = YotubeProcess(
                    r"%s" % (self.dictionary_label.text()), self.url_line.text())
                ytp.download_video()
                if self.mp3_check.isChecked():
                    ytp.convert_mp3(not (self.video_check.isChecked()))
        except:
            QMessageBox.warning(
                self, "Error", "Error occurred during operation. Please , try again it")

    def clicked_dictionary_button(self):
        selected_dictionary = QFileDialog.getExistingDirectory(
            self, app.applicationName()+" - Open File", self.dictionary_label.text())
        self.dictionary_label.setText(selected_dictionary)


app = QApplication(sys.argv)
app.setApplicationName("Youtube Downloader")
window = YoutubeDownloaderApp()
window.show()
sys.exit(app.exec())
