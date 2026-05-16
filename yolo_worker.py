import cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal
from ultralytics import YOLO
import time 

class YoloThread(QThread):
    # Сигналы для связи с интерфейсом
    change_pixmap_signal = pyqtSignal(np.ndarray)
    count_signal = pyqtSignal(int)
    fps_signal = pyqtSignal(int)
    resolution_signal = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()
        self._run_flag = False
        self.model = YOLO(r"C:\Users\Аина\Desktop\DiplomWork\Real-Time-Object-Detection-in-Python\main_model\trained\weights\best.pt")  # Путь к вашей модели
        self.camera_index = 0
        self.conf_threshold = 0.5
        self.iou_threshold = 0.5
        self.show_boxes = True
        self.show_conf = True

    # Изменения внутри метода run класса YoloThread
    def run(self):
        self._run_flag = True
        cap = cv2.VideoCapture(self.camera_index)
        
        # ДОБАВИТЬ: отправка разрешения
        if cap.isOpened():
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.resolution_signal.emit(frame_width, frame_height)
        
        # ДОБАВИТЬ: переменные для FPS
        frame_count = 0
        fps_start_time = time.time()

        while self._run_flag:
            ret, frame = cap.read()
            
            if not ret:
                # Если это было видео — оно закончилось. Если камера — сбой.
                # Если мы хотим, чтобы видео или фото не пропадало:
                if isinstance(self.camera_index, str): # Если это файл
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # Перематываем в начало
                    continue
                else:
                    break

            # Инференс YOLO
            results = self.model.predict(
                frame, 
                conf=self.conf_threshold, 
                iou=self.iou_threshold,
                device='cpu'
            )
            
            # Отрисовка разметки
            annotated_frame = results[0].plot(
                conf=self.show_conf, 
                boxes=self.show_boxes
            )
            
            # Отправка кадра в интерфейс
            self.change_pixmap_signal.emit(annotated_frame)
            self.count_signal.emit(len(results[0].boxes))

            frame_count += 1
            if frame_count % 30 == 0:
                current_time = time.time()
                fps = int(30 / (current_time - fps_start_time))
                self.fps_signal.emit(fps)
                fps_start_time = current_time
            
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()