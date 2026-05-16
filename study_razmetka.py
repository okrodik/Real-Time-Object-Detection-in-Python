from ultralytics import YOLO
from pathlib import Path

BASE_DIR = r"C:\Users\Аина\Desktop\YOLO_Project"

data_yaml = Path(BASE_DIR) / 'data.yaml'

print("🚀 ОБУЧЕНИЕ МОДЕЛИ")
print(f"📁 data.yaml: {data_yaml}")
print("="*50)

# Загружаем модель
model = YOLO('yolo26n.pt')

results = model.train(
    data=str(data_yaml),
    epochs=30,              # 30 эпох
    imgsz=640,               # размер картинок
    batch=8,                 # батч
    device='cpu',            # процессор
    workers=0,               # для Windows
    save=True,               # сохранять веса
    project='my_model',      # папка с результатами
    name='trained',          # имя модели
    exist_ok=True,           # перезаписать
)

print("\n✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!")
print("📁 Модель сохранена: my_model/trained/weights/best.pt")