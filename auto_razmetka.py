import os
import glob
from PIL import Image

from ultralytics import YOLO

model_path = r"C:\Users\Аина\Desktop\DiplomWork\Real-Time-Object-Detection-in-Python\runs\detect\my_model\trained\weights\best.pt"
images_dir = r"C:\Users\Аина\Desktop\DiplomWork\all dataset\images"
labels_dir = r"C:\Users\Аина\Desktop\DiplomWork\all dataset\labels"

os.makedirs(labels_dir, exist_ok=True)

model = YOLO(model_path)

image_paths = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.webp"):
    image_paths.extend(glob.glob(os.path.join(images_dir, ext)))

for img_path in image_paths:
    img = Image.open(img_path)
    w, h = img.size

    results = model.predict(img_path, conf=0.25, iou=0.45, imgsz=640, verbose=False)
    r = results[0]

    out_file = os.path.join(labels_dir, os.path.splitext(os.path.basename(img_path))[0] + ".txt")

    lines = []
    if r.boxes is not None and len(r.boxes) > 0:
        for box in r.boxes:
            cls_id = int(box.cls.item())
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            xc = ((x1 + x2) / 2) / w
            yc = ((y1 + y2) / 2) / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h

            lines.append(f"{cls_id} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

print(f"Готово. Размечено изображений: {len(image_paths)}")
print(f"Разметка сохранена в: {labels_dir}")