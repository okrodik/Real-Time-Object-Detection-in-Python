from pathlib import Path
import cv2

images_dir = Path(r"C:\Users\Аина\Desktop\DiplomWork\converted_foto\images")
labels_dir = Path(r"C:\Users\Аина\Desktop\DiplomWork\converted_foto\labels")

image_path = list(images_dir.glob("*.jpg"))[0]
label_path = labels_dir / f"{image_path.stem}.txt"

print(image_path)
print(label_path)

img = cv2.imread(str(image_path))

h, w = img.shape[:2]

with open(label_path) as f:
    lines = f.readlines()

for line in lines:
    cls, xc, yc, bw, bh = map(float, line.split())

    x1 = int((xc - bw / 2) * w)
    y1 = int((yc - bh / 2) * h)

    x2 = int((xc + bw / 2) * w)
    y2 = int((yc + bh / 2) * h)

    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 3)

output_path = "result.jpg"

cv2.imwrite(output_path, img)

print(f"Saved: {output_path}")