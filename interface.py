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
        

        main_vertical_layout = QVBoxLayout(central_widget)
        main_vertical_layout.setContentsMargins(0, 0, 0, 0)
        main_vertical_layout.setSpacing(0) 

        # Главный горизонтальный layout
        main_horizontal_layout = QHBoxLayout()
        main_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        main_horizontal_layout.setSpacing(0) 


        
        left_container = QWidget()
        left_container.setFixedSize(870, 720)  
        left_container.setStyleSheet("background: #1E1E1E")

        rigth_container = QWidget()
        rigth_container.setFixedSize(410, 720)  
        rigth_container.setStyleSheet("background: #2B2B2B")
        
        left_layout = QVBoxLayout(left_container)  
        left_layout.setContentsMargins(5, 5, 5, 5) 
        left_layout.setSpacing(5) 

        rigth_layout = QVBoxLayout(rigth_container)
        rigth_layout.setContentsMargins(0, 0, 0, 0)
        rigth_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Виджет для заголовка
        header_widget = QWidget()
        header_widget.setStyleSheet("background-color: #333333;")
        header_widget.setFixedSize(860, 30)
        
        header_layout = QHBoxLayout(header_widget) 
        header_layout.setContentsMargins(10, 0, 0, 0)

        # Заголовок секции видео
        video_header = QLabel("Видеопоток с веб-камеры")
        video_header.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")   
        header_layout.addWidget(video_header) 
        
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
        fps_layout.setContentsMargins(10, 5, 10, 5)
        fps_layout.setSpacing(10)

#FPS виджет
        self.fps_widgets = QWidget()
        self.fps_widgets.setFixedSize(80, 60)
        self.fps_widgets.setStyleSheet("background-color: #532D2D;")

        fps_widgets_layout = QVBoxLayout(self.fps_widgets)
        fps_widgets_layout.setContentsMargins(5, 5, 5, 5)

        fps_widgets_label = QLabel("FPS: 0")
        fps_widgets_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")   
        fps_widgets_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        fps_widgets_layout.addWidget(fps_widgets_label)
#FPS Виджет конец
#FPS Качетсво начало
        self.permisson_widgets = QWidget()
        self.permisson_widgets.setFixedSize(120, 60)
        self.permisson_widgets.setStyleSheet("background-color: #532D2D;")

        permisson_widgets_layout = QVBoxLayout(self.permisson_widgets)
        permisson_widgets_layout.setContentsMargins(5, 5, 5, 5)

        permisson_widgets_label = QLabel("Разрешение: 0")
        permisson_widgets_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")   
        permisson_widgets_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        permisson_widgets_layout.addWidget(permisson_widgets_label)
#FPS Качетсво конец

#FPS Объект конец
        self.object_widgets = QWidget()
        self.object_widgets.setFixedSize(100, 60)
        self.object_widgets.setStyleSheet("background-color: #532D2D;")

        object_widgets_layout = QVBoxLayout(self.object_widgets)
        object_widgets_layout.setContentsMargins(5, 5, 5, 5)

        object_widgets_label = QLabel("Качетсво: 0")
        object_widgets_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white;")   
        object_widgets_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        object_widgets_layout.addWidget(object_widgets_label)

#FPS Объект конец

        fps_layout.addWidget(self.fps_widgets)
        fps_layout.addWidget(self.permisson_widgets)
        fps_layout.addWidget(self.object_widgets)
        fps_layout.addStretch()


        left_layout.addWidget(header_widget)
        left_layout.addWidget(self.video_label)
        left_layout.addWidget(fps_widget)

#Левая часть все


#header
        right_header = QWidget()
        right_header.setStyleSheet("background-color: #333333;")
        right_header.setFixedSize(410, 50)

        right_header_layout = QHBoxLayout(right_header)
        right_header_layout.setContentsMargins(0, 0, 0, 0)

        header_label = QLabel("Панель управления")
        header_label.setStyleSheet("font-weigth: bold; font-size: 14px; color: white;")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_header_layout.addWidget(header_label)

#header_konec

#setting
        right_video_setting_widget = QWidget()
        right_video_setting_widget.setStyleSheet("background-color: #333333;")
        right_video_setting_widget.setFixedSize(380, 120)

        right_video_setting_layout = QVBoxLayout(right_video_setting_widget)
        right_video_setting_layout.setContentsMargins(10, 10, 10, 10)
        right_video_setting_layout.setSpacing(10)


        right_video_setting_label = QLabel("Источник видео")
        right_video_setting_label.setStyleSheet("font-weigth: bold; font-size: 14px; color: white;")

        self.combo_camera = QComboBox()
        self.combo_camera.addItems(["Камера 0 (встроенная)", "Камера 1 (внешняя)", "Выбрать файл "])

        self.combo_camera.setStyleSheet("""
            QComboBox {
                color: white;
                border: 1px solid #5B5B5B;
                padding: 8px;
            }
        """)

        startstop_layout = QHBoxLayout()
        startstop_layout.setSpacing(10)


        self.start_button_camera = QPushButton("Старт")
        self.start_button_camera.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)

        
        self.stop_button_camera = QPushButton("Стоп")
        self.stop_button_camera.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 3px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #B00000;
            }
            QPushButton:pressed {
                background-color: #480607;
            }
        """)


        startstop_layout.addWidget(self.start_button_camera)
        startstop_layout.addWidget(self.stop_button_camera)



        right_video_setting_layout.addWidget(right_video_setting_label)
        right_video_setting_layout.addWidget(self.combo_camera)
        right_video_setting_layout.addLayout(startstop_layout)

#setting stop

#model start
        
        model_setting_widget = QWidget()
        model_setting_widget.setStyleSheet("background-color: #333333;")
        model_setting_widget.setFixedSize(380, 190)

        model_setting_layout = QVBoxLayout(model_setting_widget)
        model_setting_layout.setContentsMargins(10, 10, 10, 10)
        model_setting_layout.setSpacing(10)



        self.model_setting_combobox = QComboBox()
        self.model_setting_combobox.addItems(["Model1", "Model2"])
        self.model_setting_combobox.setStyleSheet("""
            QComboBox {
                color: white;
                border: 1px solid #5B5B5B;
                padding: 8px;
            }
        """)

        model_setting_header_label = QLabel("Классы объектов:")
        model_setting_header_label.setStyleSheet("font-style: bold; font-size: 14px; color: white")

        model_setting_spicok_label = QLabel("""Класс 1 (человек)
Класс 2 (автомобиль)
Класс 3 (телефон)
Класс 4 (телевизор)
Класс 5 (шкаф)
Класс 6 (мяч)""")
        model_setting_spicok_label.setStyleSheet("font-style: bold; font-size: 12px; color: #AAAAAA")


        model_setting_layout.addWidget(self.model_setting_combobox)
        model_setting_layout.addWidget(model_setting_header_label)
        model_setting_layout.addWidget(model_setting_spicok_label)

#model stop
        
#Setting
        
        right_detect_setting = QWidget()
        right_detect_setting.setStyleSheet("background-color: #333333")
        right_detect_setting.setFixedSize(380, 175)

        right_detect_setting_layout = QVBoxLayout(right_detect_setting)
        right_detect_setting_layout.setContentsMargins(10, 10, 10, 10)
        right_detect_setting_layout.setSpacing(10)

        right_detect_setting_header_label = QLabel("Настройка детекции")
        right_detect_setting_header_label.setStyleSheet("font-style: bold; font-size: 14px; color: white")

        self.right_detect_setting_porog_label = QLabel("Порог уверенности: 50")
        self.right_detect_setting_porog_label.setStyleSheet("font-style: bold; font-size: 12px; color: white")

        self.right_detect_setting_slider_porog = QSlider(Qt.Orientation.Horizontal)  # Указываем ориентацию
        self.right_detect_setting_slider_porog.setRange(25, 75)  # Диапазон от 0 до 100
        self.right_detect_setting_slider_porog.setValue(50)  # Начальное значение 50
        self.right_detect_setting_slider_porog.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.right_detect_setting_slider_porog.setTickInterval(5)
        self.right_detect_setting_slider_porog.setStyleSheet("""
        QSlider::groove:horizontal {
            height: 6px;
            background: #4B4B4B;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #4B4B4B;
            border: 2px;
            width: 18px;
            height: 18px;
            margin: -6px 0;
            border-radius: 9px;
        }

    """)


        self.right_detect_setting_iou_label = QLabel("Порог IoU: 50")
        self.right_detect_setting_iou_label.setStyleSheet("font-style: bold; font-size: 12px; color: white")

        self.right_detect_setting_iou_porog = QSlider(Qt.Orientation.Horizontal)  # Указываем ориентацию
        self.right_detect_setting_iou_porog.setRange(25, 75)  # Диапазон от 0 до 100
        self.right_detect_setting_iou_porog.setValue(50)  # Начальное значение 50
        self.right_detect_setting_iou_porog.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.right_detect_setting_iou_porog.setTickInterval(5)
        self.right_detect_setting_iou_porog.setStyleSheet("""
        QSlider::groove:horizontal {
            height: 6px;
            background: #4B4B4B;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #4B4B4B;
            border: 2px;
            width: 18px;
            height: 18px;
            margin: -6px 0;
            border-radius: 9px;
        }

    """)

        right_detect_setting_visible_layout1 = QHBoxLayout()
        right_detect_setting_visible_layout1.setSpacing(10)

        right_detect_setting_visible_layout2 = QHBoxLayout()
        right_detect_setting_visible_layout2.setSpacing(10)

        self.right_detect_setting_visible_checkbox1 = QCheckBox()
        self.right_detect_setting_visible_checkbox2 = QCheckBox()

        right_detect_setting_visible_label1 = QLabel("Показывать bourding box")
        right_detect_setting_visible_label2 = QLabel("Показывать уверенность")
        right_detect_setting_visible_label1.setStyleSheet("font-style: bold; font-size: 12px; color: white")    
        right_detect_setting_visible_label2.setStyleSheet("font-style: bold; font-size: 12px; color: white")   

        right_detect_setting_visible_layout1.addWidget(self.right_detect_setting_visible_checkbox1)    
        right_detect_setting_visible_layout1.addWidget(right_detect_setting_visible_label1)


        right_detect_setting_visible_layout2.addWidget(self.right_detect_setting_visible_checkbox2)    
        right_detect_setting_visible_layout2.addWidget(right_detect_setting_visible_label2)
 


        right_detect_setting_layout.addWidget(right_detect_setting_header_label)
        right_detect_setting_layout.addWidget(self.right_detect_setting_porog_label)
        right_detect_setting_layout.addWidget(self.right_detect_setting_slider_porog)
        right_detect_setting_layout.addWidget(self.right_detect_setting_iou_label)
        right_detect_setting_layout.addWidget(self.right_detect_setting_iou_porog)
        right_detect_setting_layout.addLayout(right_detect_setting_visible_layout1)
        right_detect_setting_layout.addLayout(right_detect_setting_visible_layout2)


#setting stop
        

#скриншот
        right_detect_scrinshot_widget = QWidget()
        right_detect_scrinshot_widget.setStyleSheet("background-color: #333333")
        right_detect_scrinshot_widget.setFixedSize(380, 70)

        right_detect_scrinshot_layout = QVBoxLayout(right_detect_scrinshot_widget)
        right_detect_scrinshot_layout.setContentsMargins(10, 10, 10, 10)
        right_detect_scrinshot_layout.setSpacing(10)

        right_detect_scrinshot_label = QLabel("Сохранение результатов")
        right_detect_scrinshot_label.setStyleSheet("font-style: bold; font-size: 12px; color: white")   

        self.right_detect_scrinshot_button = QPushButton("Скриншот")
        self.right_detect_scrinshot_button.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 3px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QPushButton:pressed {
        background-color: #3d8b40;
    }
""")


        right_detect_scrinshot_layout.addWidget(right_detect_scrinshot_label)
        right_detect_scrinshot_layout.addWidget(self.right_detect_scrinshot_button)


#Сркиншот стоп


        rigth_layout.addWidget(right_header)
        rigth_layout.addWidget(right_video_setting_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        rigth_layout.addWidget(model_setting_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        rigth_layout.addWidget(right_detect_setting, alignment=Qt.AlignmentFlag.AlignCenter)
        rigth_layout.addWidget(right_detect_scrinshot_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        rigth_layout.addStretch()        


        bottom_widget = QWidget()
        bottom_widget.setFixedSize(1280, 30)
        bottom_widget.setStyleSheet("background-color: #333333;")
        
        bottom_layout = QHBoxLayout(bottom_widget)
        bottom_layout.setContentsMargins(10, 0, 10, 0)
        
        # Статус=
        self.status_label = QLabel("Статус камеры: Готов к работе")
        self.status_label.setStyleSheet("color: #AAAAAA; font-size: 12px;")
        


        # Обнаружено
        self.deteling_label = QLabel("Обнаружено: 0")
        self.deteling_label.setStyleSheet("color: #AAAAAA; font-size: 12px;")
        
        # Время работы
        self.time_label = QLabel("Время работы: 00:00")
        self.time_label.setStyleSheet("color: #AAAAAA; font-size: 12px;")

        
        # Добавляем все в статус-бар
        bottom_layout.addWidget(self.status_label)
        bottom_layout.addWidget(self.deteling_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.time_label)


        # Добавляем левый контейнер в главный layout
        main_horizontal_layout.addWidget(left_container)
        main_horizontal_layout.addWidget(rigth_container)

        main_vertical_layout.addLayout(main_horizontal_layout)
        main_vertical_layout.addWidget(bottom_widget)

        self.init_functions()
    
    def init_functions(self):
        self.start_button_camera.clicked.connect(self.start_camera)
        self.stop_button_camera.clicked.connect(self.stop_camera)
        self.right_detect_scrinshot_button.clicked.connect(self.take_screenshot)

        self.right_detect_setting_slider_porog.valueChanged.connect(self.update_confidence_slider)
        self.right_detect_setting_iou_porog.valueChanged.connect(self.update_iou_slider)
        
        # Подключение комбобоксов
        self.combo_camera.currentIndexChanged.connect(self.camera_change)
        self.model_setting_combobox.currentIndexChanged.connect(self.model_change)
        
        # Подключение чекбоксов
        self.right_detect_setting_visible_checkbox1.stateChanged.connect(self.bounding_box_checkbox)
        self.right_detect_setting_visible_checkbox2.stateChanged.connect(self.confidence_checkbox)
        
        # Таймер для обновления времени
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Обновление каждую секунду
        self.secund = 0

    def start_camera(self):
        print("Камера работает")
        self.status_label.setText("Статус: камера работает")
    
    def stop_camera(self):
        print("Камера неработает")
        self.status_label.setText("Статус: камера не работает")
    
    def take_screenshot(self):
        print("Скриншот сохранен")
        self.status_label.setText("Статус: Скриншот сохраненон не работает")
    
    def update_confidence_slider(self, x):
        self.right_detect_setting_porog_label.setText(f"Порог уверенности: {x}%")
        print(f"Порог уверенности изменен на {x}%")

    def update_iou_slider(self, x):
        self.right_detect_setting_iou_label.setText(f"Порог IoU: {x}%")
        print(f"Порог IoU изменен на {x}%")

    def camera_change(self, index):
        sources = ["встроенная камера", "Внешняя камера", "Файл"]
        if index < len(sources):
            print(f"Выбран источник: {sources[index]}")
            self.status_label.setText(f"Статус: Выбран {sources[index]}")

    def model_change(self, index):
        models = ["Model1", "Model2"]
        if index < len(models):
            print(f"Выбран источник: {models[index]}")
            self.status_label.setText(f"Статус: Выбран {models[index]}")

    def bounding_box_checkbox(self, vibor):
        if vibor == Qt.CheckState.Checked.value:
            print("Bounding box включен")
            self.status_label.setText("Статус: Bounding box включен")
        else:
            print("Bounding box выключен")
            self.status_label.setText("Статус: Bounding box выключен")

    def confidence_checkbox(self, vibor):
        if vibor == Qt.CheckState.Checked.value:
            print("Отображение уверенности включен")
            self.status_label.setText("Статус: Отображение уверенности включено")
        else:
            print("Отображение уверенности выключено")
            self.status_label.setText("Статус: Отображение уверенности выключен")

    def update_time(self):
        self.secund += 1
        minutes = self.secund // 60
        seconds = self.secund % 60
        self.time_label.setText(f"Время работы: {minutes:02d}:{seconds:02d}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
