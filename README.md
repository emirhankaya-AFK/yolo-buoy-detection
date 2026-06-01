# YOLO Maritime Buoy Detection & Auto-Labeling Suite (YOLO Buoy Detection)

An end-to-end, high-performance computer vision suite designed to auto-label, verify, clean, and train YOLO (You Only Look Once) object detection models specifically for maritime environments (Unmanned Surface Vehicles - USV / İDA) to detect buoys (dubalar).

## 🚀 Features

- **🤖 Automated Dataset Annotation**: Automatically labels raw images using a parent YOLO model (`predict_auto_label.py`) to drastically reduce manual bounding box drawing time.
- **🛠️ Label Verification & Alignment**:
  - `check_labels.py`: Validates annotation formatting, bounding box constraints, and file matching.
  - `etiket_ata.py` & `yolo_etiket_duzelt.py`: Auto-fixes class mappings, corrects label offsets, and handles directory alignments.
- **📈 Seamless YOLO Model Training**: Lightweight training pipeline (`train_yolo.py`) utilizing standard `ultralytics` framework.
- **🏷️ Configuration Standard**: Centralized `data.yaml` setting up class indexes (buoys, navigation marks, etc.) for high accuracy object detection.

## 📁 Project Structure

- `predict_auto_label.py`: Auto-labeling script using pre-trained weights.
- `train_yolo.py`: Simplified model training wrapper.
- `yolo_etiket_duzelt.py`: Label cleaning and correction utility.
- `etiket_ata.py`: Class assignment script.
- `check_labels.py`: Automated dataset integrity validation tool.
- `data.yaml`: YOLO dataset structural configuration.

## 🛠️ Tech Stack

- **Framework**: `Ultralytics YOLO`
- **Core Library**: OpenCV, PyTorch
- **Scripting**: Python 3.11

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd yolo-buoy-detection
   ```

2. **Install dependencies**:
   ```bash
   pip install ultralytics opencv-python torch
   ```

3. **Auto-Label raw images**:
   - Place raw images in your designated input directory and run:
   ```bash
   python predict_auto_label.py
   ```

4. **Train the model**:
   - Update `data.yaml` with your absolute folder paths and run:
   ```bash
   python train_yolo.py
   ```

---

*Designed and developed with 💙 by Emirhan Kaya.*
