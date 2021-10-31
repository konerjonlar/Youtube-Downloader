from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget)
from pytube import YouTube
import pyautogui as pya
import clipboard
#I'll select text and run with shourt cut so this function necessary
def copy():
    pya.hotkey("ctrl", "c")    
    text = clipboard.paste()
    if text[:23] != "https://www.youtube.com":
        return
    return text
def get_streams(url):
    streams = YouTube(url).streams
    for i in streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
        pass

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTopLeftGroupBox()
        self.createDownloadButton()
        

        self.createProgressBar()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.downloadButton, 2, 0)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)

        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)
    def createDownloadButton(self):
        self.downloadButton = QGroupBox("Group 1")
        layout = QVBoxLayout()
        button = QPushButton("indirmek için tıklayınız")
        button.setDefault(True)
        layout.addWidget(button)
        self.downloadButton.setLayout(layout)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")
        



        #radioButton1 = QRadioButton("Radio button 1")
        #radioButton2 = QRadioButton("Radio button 2")
        #radioButton3 = QRadioButton("Radio button 3")
        #radioButton1.setChecked(True)
        
        
        nameLabel = QLabel('Video URL\'sini giriniz',self)
        print(copy())
        nameLineEdit = QLineEdit(copy())

        layout = QVBoxLayout()
        layout.addWidget(nameLabel)
        layout.addWidget(nameLineEdit)
        tamam = QPushButton("Url'yi girdikten sonra tıklayınız")
        
        url = nameLineEdit.text()
        
        
        layout.addWidget(tamam)
        radioButtons = {}
        
        def createRadioButtons(url):
            url = nameLineEdit.text()
            print(url)
            streams = YouTube(url).streams
            for i in streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
                radioButtons["RadioButton"+str(i)] = QRadioButton(i.resolution,self)
            for i in radioButtons.values():
                layout.addWidget(i)
                i.show()
            return streams
        if(copy()):
            createRadioButtons(copy())
        tamam.clicked.connect(createRadioButtons)



        

        
        



        # layout.addWidget(radioButton1)
        # layout.addWidget(radioButton2)
        # layout.addWidget(radioButton3)

        

        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)
        
        

    def createProgressBar(self):
        
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
