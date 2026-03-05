import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLabel, QComboBox, 
                            QCheckBox, QSlider, QGroupBox, QGridLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
import cv2
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.setWindowTitle("YOLO26 - Распознавание физических объектов | Оконешников Родион КИСП-23")
        self.setFixedSize(1280, 720)
        
        # Главный центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главный горизонтальный layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Левый контейнер (виджет, а не layout)
        left_container = QWidget()
        left_container.setFixedSize(870, 720)  # Исправлено: setFixedSize для виджета
        left_container.setStyleSheet("background: #1E1E1E")

        rigth_container = QWidget()
        rigth_container.setFixedSize(410, 720)  # Исправлено: setFixedSize для виджета
        rigth_container.setStyleSheet("background: #2B2B2B")
        
        left_layout = QVBoxLayout(left_container)  # Исправлено: связываем layout с контейнером

        rigth_layout = QVBoxLayout(rigth_container)

        # Виджет для заголовка
        header_widget = QWidget()
        header_widget.setStyleSheet("background-color: #333333;")
        header_widget.setFixedSize(860, 30)
        
        header_layout = QHBoxLayout(header_widget)  # Исправлено: создаем layout для header_widget

        # Заголовок секции видео
        video_header = QLabel("Видеопоток с веб-камеры")
        video_header.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")
        
        header_layout.addWidget(video_header)  # Исправлено: добавляем в layout, а не в виджет

        
        # Виджет для отображения видео
        self.video_label = QLabel()
        self.video_label.setFixedSize(860, 484) 
        self.video_label.setStyleSheet("background-color: #333333; color: white;")
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label.setText("Камера не подключена")

    
        fps_widget = QWidget()
        fps_widget.setStyleSheet(("background-color: #333333;"))
        fps_widget.setFixedSize(860, 70)

        fps_layout = QHBoxLayout(fps_widget)




        left_layout.addWidget(header_widget)
        left_layout.addWidget(self.video_label)
        left_layout.addWidget(fps_widget)


        # Добавляем левый контейнер в главный layout
        main_layout.addWidget(left_container)
        main_layout.addWidget(rigth_container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())