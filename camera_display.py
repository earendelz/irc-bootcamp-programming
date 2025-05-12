import cv2
from datetime import datetime

nama = "Farrel Fitra Mulyadi"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak bisa membuka kamera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in wajah:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.putText(frame, f"{nama}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Wajah terdeteksi: {len(wajah)}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, waktu, (10, 90), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 1)

    cv2.imshow('Kamera', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"foto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Foto disimpan sebagai {filename}")

cap.release()
cv2.destroyAllWindows()
