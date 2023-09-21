import keyboard
from pydub import AudioSegment
from pydub.playback import play
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Ses dosyasını yükleyin (ses dosyanızın adını ve yolunu değiştirin)
ses_dosyasi = AudioSegment.from_file("ses.mp3", format="mp3")

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tuşla Ses Çalma Uygulaması")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Herhangi bir tuşa basın", self)
        self.label.setGeometry(150, 50, 200, 50)

        self.button = QPushButton("Çıkış", self)
        self.button.setGeometry(150, 100, 100, 30)
        self.button.clicked.connect(self.cikis)

    def cikis(self):
        keyboard.unhook_all()  # Tuş dinlemeyi kapat
        sys.exit()

def tusa_basildi(event):
    if event.event_type == keyboard.KEY_DOWN:
        play(ses_dosyasi)
        pencere.label.setText("Tuşa basıldı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()

    keyboard.hook(tusa_basildi)

    sys.exit(app.exec_())
