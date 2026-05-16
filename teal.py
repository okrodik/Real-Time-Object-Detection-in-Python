import os
import shutil
import random

def split_dataset(source_base, output_base, train_perc=0.8, val_perc=0.1, test_perc=0.1):
    # Пути к исходным папкам
    src_images = os.path.join(source_base, "images")
    src_labels = os.path.join(source_base, "labels")

    # Списки целевых подпапок
    splits = ['train', 'val', 'test']
    for s in splits:
        os.makedirs(os.path.join(output_base, s, "images"), exist_ok=True)
        os.makedirs(os.path.join(output_base, s, "labels"), exist_ok=True)

    # Получаем список всех файлов (ориентируемся по изображениям)
    # Берем только файлы с расширениями изображений
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    files = [f for f in os.listdir(src_images) if f.lower().endswith(valid_extensions)]
    
    # Перемешиваем для случайного распределения
    random.shuffle(files)

    # Расчет количества файлов для каждой части
    total = len(files)
    num_train = int(total * train_perc)
    num_val = int(total * val_perc)
    
    # Распределение имен файлов по группам
    train_files = files[:num_train]
    val_files = files[num_train : num_train + num_val]
    test_files = files[num_train + num_val :]

    def move_data(file_list, split_name):
        for filename in file_list:
            base_name = os.path.splitext(filename)[0]
            
            # Пути для изображений
            img_src = os.path.join(src_images, filename)
            img_dst = os.path.join(output_base, split_name, "images", filename)
            
            # Пути для меток (предполагаем расширение .txt)
            label_name = base_name + ".txt"
            label_src = os.path.join(src_labels, label_name)
            label_dst = os.path.join(output_base, split_name, "labels", label_name)

            # Копируем изображение
            shutil.copy(img_src, img_dst)
            
            # Проверяем наличие метки и копируем, если она есть
            if os.path.exists(label_src):
                shutil.copy(label_src, label_dst)
            else:
                print(f"Предупреждение: Метка для {filename} не найдена в {src_labels}")

    # Запуск процесса
    print(f"Начинаю распределение {total} файлов...")
    move_data(train_files, 'train')
    move_data(val_files, 'val')
    move_data(test_files, 'test')
    
    print("--- Распределение завершено ---")
    print(f"Train: {len(train_files)}")
    print(f"Val: {len(val_files)}")
    print(f"Test: {len(test_files)}")

# --- ВАШИ ПУТИ ---
source_path = r"C:\Users\Аина\Desktop\DiplomWork\converted_foto"
output_path = r"C:\Users\Аина\Desktop\DiplomWork\dataset"

# Запуск функции
split_dataset(source_path, output_path)