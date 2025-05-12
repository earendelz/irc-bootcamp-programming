# irc-bootcamp-programming

Farrel Fitra Mulyadi, J0403231122, TPL 60

Divisi VTOL Programming

---

# Resume Bootcamp Day 2
**1. Pengenalan Divisi Programming**
   
   - Divisi Programming bertugas untuk mengendalikan gerakan robot, memproses data dari sensor, dan membuat keputusan cerdas.

   - Divisi Programming pada IRC dibagi menjadi tiga jenis, yaitu Programming VTOL, Programming Transporter, dan Ground Control Station (GCS) RP

   - Tools yang digunakan programmer VTOL: Python, Mission Planner, Roboflow, Dronekit, dan YOLO

   - Tools yang digunakan programmer transporter: Arduino, Platform IO, dan WOKWI

   - Tools yang digunakan programmer GCS: Mission Planner

   - Keterampilan yang dibutuhkan secara umum adalah bahasa pemrograman (C++, python), komunikasi (UART, I2C, SPI, Bluetooth/WIFI), Mikrokontroller (Arduino, ESP32, dll), Sensor $ Aktuator (Motor, Servo, IR, dsb)

---

**2. Flowchart dan Pseudocode**

   - Pengertian Flowchart: Representasi grafis proses atau algoritma dengan simbol standar untuk menggambarkan alur langkah-langkah

   - Pengertian Pseudocode: Penulisan algoritma dalam deskripsi mirip bahasa pemrograman yang mudah dipahami tanpa terikat sintaks tertentu.

---

**3. Data Types & Variables**

   **a. Variabel di Arduino (C/C++)**

   - Tipe Data: Harus dideklarasikan sebelum digunakan (int, float, char, dll).

   - Deklarasi: int ledPin = 13;

   - Skop: Bisa global atau lokal.

   - Sintaks: Lebih ketat dan memerlukan tipe data eksplisit.

   **b. Variabel di Python**
   
   - Tipe Data: Tipe data ditentukan otomatis (int, float, str, dll)
   
   - Deklarasi: ledPin = 13
   
   - Skop: Bisa global atau lokal.
   
   - Sintaks: Lebih fleksibel dan sederhana.

---
   
**4. Toolchain**

   Toolchain yang digunakan adalah: Arduino IDE, Platform IO, VS Code, Google Collab, PyCharm, WOKWI, Roboflow 

---

 **5. Git**

Git adalah sistem kontrol versi yang digunakan untuk mencatat perubahan pada file secara terstruktur dan terkelola, memungkinkan banyak orang bekerja pada proyek yang sama tanpa konflik. 

---

**6. Embedded System**

Embedded system adalah sistem komputer khusus yang dirancang untuk
menjalankan tugas tertentu dalam perangkat yang lebih besar, dengan
keterbatasan daya, memori, dan pemrosesan.

Contohnya adalah: Arduino Board (paling murah), EPS32 Board, STM32 Board, Raspiberry Pi Board (paling mahal namun kuat)

---

# Dokumentasi dan Penjelasan Tugas camera_display.py
![Screenshot (750)](https://github.com/user-attachments/assets/7706a449-8ef9-49e6-b61a-52d15688e172)

### Fungsi:
- Membuka kamera laptop
- Menampilkan nama peserta di atas tampilan kamera
- Menampilkan waktu saat ini di layar
- Menampilkan jumlah wajah yang terdeteksi
- Memberi kotak di sekeliling wajah yang terdeteksi

### Penjelasan Kode:
- `cv2.VideoCapture(0)` membuka kamera default
- `cv2.putText()` digunakan untuk menampilkan teks di layar
- `cv2.CascadeClassifier` digunakan untuk mendeteksi wajah menggunakan model Haar Cascade
- Setiap frame:
  - Dibaca dari kamera
  - Diproses untuk deteksi wajah
  - Diberi kotak pada wajah
  - Ditambahkan teks nama, jam, dan jumlah wajah
    
---


# Dokumentasi dan Penjelasan Tugas led_servo.ino

![Screenshot (751)](https://github.com/user-attachments/assets/d458c627-92e3-4422-a781-f570a48090bf)

### Link Projek
https://wokwi.com/projects/430739116739424257

### Fungsi:
- Menyalakan dan mematikan LED setiap 1 detik
- Menggerakkan servo dari 0° ke 180° dan kembali terus-menerus

### Penjelasan Kode:
- `ledPin` dan `servoPin` untuk LED dan servo
- `pinMode(ledPin, OUTPUT)` mengatur pin LED sebagai output
- Variabel `previousMillis` dan `millis()` digunakan agar LED berkedip tiap 1 detik tanpa menggunakan `delay()`
- LED akan berubah status (nyala/mati) setiap 1000 milidetik
- Servo digerakkan menggunakan `myServo.write(angle)` di dalam loop.
  - Nilai `angle` akan naik dari 0 ke 180 secara bertahap
  - Jika mencapai 180 atau 0, arah gerakan dibalik dengan `step = -step`
  - `delay(15)` memberikan jeda agar servo bergerak halus
