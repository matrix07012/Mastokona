import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QSlider,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLayout,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ----------------------- Widgets -----------------------

        # Name of window title
        self.setWindowTitle('konakona-gui')

        # Basic Label saying Konakona, Replacing it with image
        self.konakona_label = QLabel('konakona-setup')
        font = self.konakona_label.font()
        font.setPointSize(20)
        self.konakona_label.setFont(font)
        self.konakona_label.setAlignment(Qt.AlignHCenter)

        # Line Edit to enter video path + Button for directory search
        self.video_path = QLineEdit()
        self.video_path.setMaxLength(255)
        self.video_path.setPlaceholderText('Enter Video Filepath')

        self.search_button = QPushButton('S')
        self.search_button.setMaximumSize(20, 40)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.video_path)
        layout2.addWidget(self.search_button)

        # Timer slider + label
        self.timer_label = QLabel('Set timer when to post')
        font2 = self.timer_label.font()
        font2.setPointSize(15)
        self.timer_label.setFont(font2)
        self.timer_label.setAlignment(Qt.AlignHCenter)

        self.timer_slider = QSlider(Qt.Horizontal)
        self.timer_slider.setMinimum(0)
        self.timer_slider.setMaximum(60)
        self.timer_slider.setTickPosition(QSlider.TicksBelow)
        self.timer_slider.setTickInterval(5)
        self.timer_slider.setSingleStep(1)

        self.timer_value = QLabel('slider value: 0')
        self.timer_value.setStyleSheet('color: grey')
        font3 = self.timer_value.font()
        font3.setPointSize(10)
        self.timer_value.setFont(font3)
        self.timer_value.setAlignment(Qt.AlignHCenter)

        # Multi chance slider + label
        self.multi_label = QLabel('Multi-image Chance')
        # font2 = self.multi_label.font()
        # font2.setPointSize(15)
        self.multi_label.setFont(font2)
        self.multi_label.setAlignment(Qt.AlignHCenter)

        self.multi_slider = QSlider(Qt.Horizontal)
        self.multi_slider.setMinimum(0)
        self.multi_slider.setMaximum(10)
        self.multi_slider.setTickPosition(QSlider.TicksBelow)
        self.multi_slider.setTickInterval(1)
        self.multi_slider.setSingleStep(1)

        self.multi_value = QLabel('slider value: 0')
        self.multi_value.setStyleSheet('color: grey')
        # font3 = self.multi_value.font()
        # font3.setPointSize(10)
        self.multi_value.setFont(font3)
        self.multi_value.setAlignment(Qt.AlignHCenter)

        # Multi-image number ComboBox
        self.multi_box_label = QLabel('Choose Multi-Image number:')
        font4 = self.multi_box_label.font()
        font4.setPointSize(10)

        self.multi_box = QComboBox()
        self.multi_box.addItems(['Random', '2', '3', '4'])

        layout3 = QHBoxLayout()
        layout3.addWidget(self.multi_box_label)
        layout3.addWidget(self.multi_box)

        # Video chance slider + label
        self.video_label = QLabel('Video Chance')
        # font2 = self.multi_label.font()
        # font2.setPointSize(15)
        self.video_label.setFont(font2)
        self.video_label.setAlignment(Qt.AlignHCenter)

        self.video_slider = QSlider(Qt.Horizontal)
        self.video_slider.setMinimum(0)
        self.video_slider.setMaximum(10)
        self.video_slider.setTickPosition(QSlider.TicksBelow)
        self.video_slider.setTickInterval(1)
        self.video_slider.setSingleStep(1)

        self.video_value = QLabel('slider value: 0')
        self.video_value.setStyleSheet('color: grey')
        # font3 = self.multi_value.font()
        # font3.setPointSize(10)
        self.video_value.setFont(font3)
        self.video_value.setAlignment(Qt.AlignHCenter)

        self.save_checkbox = QCheckBox('Save images and clips')
        layout4 = QHBoxLayout()
        layout4.addWidget(self.save_checkbox)
        layout4.setAlignment(Qt.AlignHCenter)

        # ------ When something is done connects the functions ------
        self.timer_slider.valueChanged.connect(self.timer_slider_value)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.multi_slider.valueChanged.connect(self.multi_slider_value)
        # self.multi_box.currentIndexChanged.connect(self.multi_box_int)
        self.multi_box.currentTextChanged.connect(self.multi_box_str)
        self.video_slider.valueChanged.connect(self.video_slider_value)
        self.save_checkbox.stateChanged.connect(self.save_checkbox_state)

        # -------- Laying out window structure (real layout) --------
        layout = QVBoxLayout()
        layout.addWidget(self.konakona_label)

        layout.addLayout(layout2)

        layout.addWidget(self.timer_label)
        layout.addWidget(self.timer_slider)
        layout.addWidget(self.timer_value)

        layout.addWidget(self.multi_label)
        layout.addWidget(self.multi_slider)
        layout.addWidget(self.multi_value)

        layout.addLayout(layout3)

        layout.addWidget(self.video_label)
        layout.addWidget(self.video_slider)
        layout.addWidget(self.video_value)

        layout.addLayout(layout4)

        # --------- Qt stuff that needs to be here ---------
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # ---------------- A bunch of functions ----------------
    def search_button_clicked(self):
        print('clicked')

    def timer_slider_value(self, i):
        self.timer_value.setText('slider value: {}'.format(i))
        # if value == 0 then make it gray

    def multi_slider_value(self, i):
        self.multi_value.setText('slider value: {}'.format(i))
        # if value == 0 then make it gray

    def multi_box_int(self, i):
        print('multi-box int: {}'.format(i))

    def multi_box_str(self, s):
        print('multi-box str: {}'.format(s))

    def video_slider_value(self, i):
        self.video_value.setText('slider value: {}'.format(i))
        # if value == 0 then make it gray

    def save_checkbox_state(self, s):
        print('Save-Checkbox: {}'.format(s == Qt.Checked))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()