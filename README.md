# 🚗📷 License Plate Detection with YOLOv5

Đây là dự án nhận diện **biển số xe** từ hình ảnh hoặc camera, sử dụng mô hình **YOLOv5** kết hợp với OCR (nhận dạng ký tự quang học). Ứng dụng có thể được dùng trong các hệ thống bãi giữ xe, giám sát an ninh hoặc thu phí tự động.

---

## 🧠 Mục tiêu chính

- ✅ Nhận diện xe máy/ô tô trong hình ảnh hoặc video
- ✅ Xác định vùng chứa biển số
- ✅ Cắt vùng biển số và thực hiện OCR để đọc ký tự
- ✅ (Tùy chọn) Truy xuất thông tin từ biển số

---

## 🔧 Công nghệ sử dụng

- 🧠 [YOLOv5](https://github.com/ultralytics/yolov5) – mô hình object detection
- 🐍 Python 3.8+
- 🔠 EasyOCR / Pytesseract – để nhận diện ký tự biển số
- 📹 OpenCV – xử lý hình ảnh/video
---
### 🔍 Phát hiện biển số và xe:
![Detection Demo](./runs/detect/exp/Bike.png)

### 🔠 2. Biển số đã được cắt (crop) để OCR:
![Cropped Plate](./runs/detect/exp/crops/bienso/Bike.jpg)

## ⚙️ Cài đặt & chạy

### 1. Clone dự án

```bash
git clone https://github.com/qtruong02it/License-Plate-Detection.git
cd License-Plate-Detection/YOLOv5/DA1-main

2. Cài đặt môi trường Python

python -m venv venv
source venv/bin/activate  # Hoặc: .\venv\Scripts\activate (Windows)
pip install -r requirements.txt

3. Kiểm tra YOLOv5 detect ảnh mẫu

python detect.py --source path/to/image.jpg --weights best.pt

4. Chạy nhận diện từ webcam

python camera.py

5. Chạy Flask API demo

cd flask_rest_api
python app.py


