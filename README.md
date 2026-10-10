# YOLO Maritime Buoy Detection & Auto-Labeling Suite (YOLO Buoy Detection)

[English](README.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md)

## English

### Purpose
An end‑to‑end computer vision suite for maritime environments that automates labeling, verification, cleaning, and training of YOLO object detection models to detect buoys (and related navigation marks) for Unmanned Surface Vehicles (USV/İDA).

### Verified Features
- **Automated Dataset Annotation** – `predict_auto_label.py` runs a parent YOLO model to generate bounding boxes for raw images, reducing manual labeling effort.  
- **Label Verification & Alignment** –  
  - `check_labels.py` validates annotation format, bounding box constraints, and file‑image correspondence.  
  - `etiket_ata.py` and `yolo_etiket_duzelt.py` fix class mappings, correct label offsets, and align directory structures.  
- **Seamless YOLO Model Training** – `train_yolo.py` provides a lightweight wrapper around the Ultralytics training pipeline.  
- **Configuration Standard** – `data.yaml` centralizes class indexes (buoys, navigation marks, etc.) for reproducible training.

### Tech Stack
- **Framework**: Ultralytics YOLO  
- **Core Libraries**: OpenCV, PyTorch  
- **Language**: Python 3.11  

### Setup & Usage
1. **Clone the repository**  
   ```bash
   git clone <your-repository-url>
   cd yolo-buoy-detection
   ```
2. **Install dependencies**  
   ```bash
   pip install ultralytics opencv-python torch
   ```
3. **Auto‑label raw images**  
   Place images in the chosen input folder and run:  
   ```bash
   python predict_auto_label.py
   ```
4. **Prepare `data.yaml`**  
   Update the file with absolute paths to your training/validation directories and class names.  
5. **Train the model**  
   ```bash
   python train_yolo.py
   ```

### Testing / Validation
- Run `check_labels.py` to verify that generated labels conform to YOLO format, that bounding boxes lie within image bounds, and that each image has a corresponding label file.

### Limitations
- This repository is intended as a tutorial / private project; no production‑grade guarantees are provided.  
- Users must adapt paths, class definitions, and possibly hyper‑parameters to their specific datasets and hardware.  
- The suite relies on a pre‑existing parent YOLO model for auto‑labeling; performance depends on the quality of those weights.

---

## Türkçe

### Amaç
Deniz ortamları için görüntü etiketleme, doğrulama, temizleme ve YOLO nesne algılama modeli eğitimi işlemlerini otomatikleştiren uç‑tan‑uca bir bilgisayar görüntüsü paketi. Amacı, deniz çubukları (dubalar) ve ilgili navigasyon işaretlerini USV/İDA platformları için tespit etmektir.

### Doğrulanmış Özellikler
- **Otomatik Veri Kümesi Etiketleme** – `predict_auto_label.py`, önceden eğitilmiş bir YOLO modeli kullanarak ham görüntüler için sınırlayıcı kutular üretir ve el ile etiketleme zamanını azaltır.  
- **Etiket Doğrulama ve Düzenleme** –  
  - `check_labels.py`: Etiket formatı, sınırlayıcı kutu sınırlamaları ve görüntü‑etiket eşleşmesini kontrol eder.  
  - `etiket_ata.py` ve `yolo_etiket_duzelt.py`: Sınıf eşleşmelerini düzeltir, etiket offsetlerini düzeltir ve dizin yapılarını hizalar.  
- **Sorunsuz YOLO Model Eğitimi** – `train_yolo.py`, Ultralytics eğitim ardışık düzeninin hafif bir sarmalayıcısıdır.  
- **Yapılandırma Standardı** – `data.yaml`, sınıf indekslerini (dubalar, navigasyon işaretleri vb.) merkezi bir şekilde tutarak tekrarlanabilir eğitim sağlar.

### Teknoloji Yığını
- **Çerçeve**: Ultralytics YOLO  
- **Çekirdek Kütüphaneler**: OpenCV, PyTorch  
- **Dil**: Python 3.11  

### Kurulum & Kullanım
1. **Depoyu klonlayın**  
   ```bash
   git clone <your-repository-url>
   cd yolo-buoy-detection
   ```
2. **Bağımlılıkları yükleyin**  
   ```bash
   pip install ultralytics opencv-python torch
   ```
3. **Ham görüntüleri otomatik etiketleyin**  
   Görüntüleri seçtiğiniz giriş klasörüne yerleştirip çalıştırın:  
   ```bash
   python predict_auto_label.py
   ```
4. **`data.yaml` dosyasını hazırlayın**  
   Eğitim/doğrulama klasörlerinin mutlak yollarını ve sınıf isimlerini güncelleyin.  
5. **Modeli eğitin**  
   ```bash
   python train_yolo.py
   ```

### Test / Doğrulama
- `check_labels.py` çalıştırarak etiketlerin YOLO formatına uygunluğunu, sınırlayıcı kutuların görüntü sınırları içinde olduğunu ve her görüntünün karşılık gelen etiket dosyasının olduğunu kontrol edin.

### Sınırlamalar
- Bu depo öğretici / özel bir proje olarak nitelendirilmiştir; üretim seviyesinde garantiler sunmaz.  
- Kullanıcılar, kendi veri setlerine ve donanımlarına göre yollar, sınıf tanımları ve hiperparametreleri uyarlamalıdır.  
- Otomatik etiketleme için bir üst‑seviye YOLO modeline bağımlıdır; bu modelin kalitesi sonuçları doğrudan etkiler.

---

## Deutsch

### Zweck
Eine End‑to‑End‑Computer‑Vision‑Lösung für maritime Umgebungen, die das Beschriften, Überprüfen, Bereinigen und Trainieren von YOLO‑Objekterkennungsmodellen automatisiert, um Boots‑ und Navigationszeichen für unbemannte Oberflächenfahrzeuge (USV/İDA) zu erkennen.

### Verifizierte Funktionen
- **Automatisierte Datensatz‑Annotation** – `predict_auto_label.py` nutzt ein vortrainiertes YOLO‑Modell, um Begrenzungsrahmen für Rohbilder zu erzeugen und den manuellen Aufwand zu reduzieren.  
- **Label‑Verifizierung und ‑Ausrichtung** –  
  - `check_labels.py` prüft das Annotation‑Format, Beschränkungen der Begrenzungsrahmen und die Zuordnung von Bild‑ zu Label‑Dateien.  
  - `etiket_ata.py` und `yolo_etiket_duzelt.py` korrigieren Klassen‑Zuordnungen, beheben Label‑Offsets und richten Verzeichnisstrukturen aus.  
- **Nahtloses YOLO‑Modelltraining** – `train_yolo.py` stellt einen dünnen Wrapper um das Ultralytics‑Training bereit.  
- **Konfigurationsstandard** – `data.yaml` zentralisiert Klassenindizes (Boots, Navigationszeichen usw.) für reproduzierbares Training.

### Technologie‑Stack
- **Framework**: Ultralytics YOLO  
- **Kernbibliotheken**: OpenCV, PyTorch  
- **Sprache**: Python 3.11  

### Einrichtung & Nutzung
1. **Repository klonen**  
   ```bash
   git clone <your-repository-url>
   cd yolo-buoy-detection
   ```
2. **Abhängigkeiten installieren**  
   ```bash
   pip install ultralytics opencv-python torch
   ```
3. **Rohbilder automatisch beschriften**  
   Legen Sie die Bilder in den gewünschten Eingabeordner ab und führen Sie aus:  
   ```bash
   python predict_auto_label.py
   ```
4. **`data.yaml` vorbereiten**  
   Aktualisieren Sie die Datei mit den absoluten Pfaden zu Ihren Trainings‑/Validierungsordnern und den Klassennamen.  
5. **Modell trainieren**  
   ```bash
   python train_yolo.py
   ```

### Test / Validierung
- Führen Sie `check_labels.py` aus, um zu überprüfen, ob die erzeugten Labels dem YOLO‑Format entsprechen, ob die Begrenzungsrahmen innerhalb der Bildgrenzen liegen und ob jedes Bild eine entsprechende Label‑Datei besitzt.

### Einschränkungen
- Dieses Repository dient als Tutorial / privates Projekt; es werden keine Produktionsgarantien übernommen.  
- Nutzer müssen Pfade, Klassendefinitionen und ggf. Hyperparameter an ihre spezifischen Datensätze und Hardware anpassen.  
- Die automatische Annotation beruht auf einem vorhandenen Eltern‑YOLO‑Modell; die Qualität dieses Modells beeinflusst das Ergebnis direkt.
