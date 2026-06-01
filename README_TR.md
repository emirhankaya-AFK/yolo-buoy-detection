# YOLO İDA Duba Tespit ve Otomatik Etiketleme Sistemi (YOLO Buoy Detection)

İnsansız Deniz Araçları (İDA / USV) için geliştirilmiş, deniz üzerindeki dubaların (buoy) tespiti amacıyla YOLO nesne algılama modellerini otomatik etiketleme, doğrulama, etiket düzeltme ve eğitme süreçlerini uçtan uca yöneten yüksek performanslı bir bilgisayarlı görü paketidir.

## 🚀 Özellikler

- **🤖 Otomatik Veri Seti Etiketleme**: Önceden eğitilmiş YOLO ağırlıklarını (`predict_auto_label.py`) kullanarak ham görüntüleri otomatik olarak etiketler ve manuel etiketleme süresini %90 oranında azaltır.
- **🛠️ Etiket Doğrulama ve Düzeltme**:
  - `check_labels.py`: Etiket formatlarını, sınır kutularını (bounding box) ve dosya eşleşmelerini otomatik doğrular.
  - `etiket_ata.py` & `yolo_etiket_duzelt.py`: Sınıf eşlemelerini düzeltir, koordinat kaymalarını onarır ve etiket dosyalarındaki hataları giderir.
- **📈 Kolay YOLO Modeli Eğitimi**: Standart `ultralytics` altyapısı kullanarak modeli eğitmeyi sağlayan temiz eğitim betiği (`train_yolo.py`).
- **🏷️ Standart Konfigürasyon**: Sınıf tanımlarını ve dizin yollarını barındıran `data.yaml` entegrasyonu.

## 📁 Proje İçeriği

- `predict_auto_label.py`: Ham görüntüleri otomatik etiketleyen ana bilgisayarlı görü betiği.
- `train_yolo.py`: YOLO model eğitimini başlatan betik.
- `yolo_etiket_duzelt.py`: Hatalı etiket koordinatlarını ve formatları onaran yardımcı araç.
- `etiket_ata.py`: Görüntülere ve txt dosyalarına sınıf eşlemesi yapan araç.
- `check_labels.py`: Veri seti bütünlüğünü test eden doğrulama betiği.
- `data.yaml`: YOLO eğitim veri seti konfigürasyon dosyası.

## 🛠️ Teknoloji Yığını

- **Kütüphaneler**: `Ultralytics YOLO`, OpenCV, PyTorch
- **Dil**: Python 3.11

## ⚙️ Kurulum ve Çalıştırma

1. **Depoyu klonlayın**:
   ```bash
   git clone <depo-adresi>
   cd yolo-buoy-detection
   ```

2. **Gereksinimleri yükleyin**:
   ```bash
   pip install ultralytics opencv-python torch
   ```

3. **Otomatik etiketlemeyi çalıştırın**:
   ```bash
   python predict_auto_label.py
   ```

4. **Modeli eğitin**:
   - `data.yaml` dosyasını kendi veri yollarınıza göre güncelleyin ve çalıştırın:
   ```bash
   python train_yolo.py
   ```

---

*Emirhan Kaya tarafından sevgiyle tasarlandı ve geliştirildi. 💙*
