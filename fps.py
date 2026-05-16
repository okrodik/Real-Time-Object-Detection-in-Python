import time

frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # обработка кадра моделью
    results = model(frame)

    frame_count += 1
    elapsed = time.time() - start_time

    if elapsed >= 1.0:
        fps = frame_count / elapsed
        print(f"FPS: {fps:.2f}")
        frame_count = 0
        start_time = time.time()