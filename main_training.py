from ultralytics import YOLO
from pathlib import Path

BASE_DIR = r"C:\Users\Аина\Desktop\DiplomWork\dataset"
SAVE_DIR = r"C:\Users\Аина\Desktop\DiplomWork\Real-Time-Object-Detection-in-Python\main_model"

data_yaml = Path(BASE_DIR) / "data.yaml"

print("🚀 ОБУЧЕНИЕ МОДЕЛИ")
print(f"📁 data.yaml: {data_yaml}")
print(f"📁 save dir: {SAVE_DIR}")
print("=" * 50)

model = YOLO("yolo26n.pt")

results = model.train(
    data=str(data_yaml),
    epochs=30,
    imgsz=640,
    batch=8,
    device="cpu",
    workers=0,
    save=True,
    project=SAVE_DIR,
    name="trained",
)

print("\n✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!")
print(r"📁 Модель сохранена: C:\Users\Аина\Desktop\DiplomWork\Real-Time-Object-Detection-in-Python\main_model\trained\weights\best.pt")