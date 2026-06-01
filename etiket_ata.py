"""
duba_gercek_e6_2 modelini (özelleştirilmiş YOLOv5) kullanarak
Emirhan_1201_1500 klasöründeki görüntülere YOLO formatında otomatik etiket atar.

Çıktı: Her .jpg için aynı klasörde aynı isimde .txt etiket dosyası
       (YOLO formatı: <class_id> <x_center> <y_center> <width> <height>)
"""

import os
import sys
import torch
import numpy as np
from pathlib import Path

# ─── AYARLAR ───────────────────────────────────────────────────────────────────
MODEL_PATH  = r"C:\Users\emirh\Downloads\duba_gercek_e6_2\weights\last.pt"
IMAGE_DIR   = r"C:\Users\emirh\Downloads\Emirhan_1201_1500"
CONF_THRESH = 0.25   # Güven eşiği
IMG_SIZE    = 640    # Inference çözünürlüğü
# ───────────────────────────────────────────────────────────────────────────────

# PyTorch 2.6+ güvenlik kısıtlamasını geç (kendi eğittiğimiz model)
_orig_load = torch.load
def _patched_load(f, *args, **kwargs):
    kwargs["weights_only"] = False
    return _orig_load(f, *args, **kwargs)
torch.load = _patched_load


def main():
    print(f"Model yükleniyor (torch.hub): {MODEL_PATH}")

    # ultralytics/yolov5 orijinal reposundan yükle (özel katmanlar dahil)
    model = torch.hub.load(
        "ultralytics/yolov5",
        "custom",
        path=MODEL_PATH,
        force_reload=False,
        trust_repo=True,
    )
    model.conf = CONF_THRESH
    model.iou  = 0.45
    model.eval()

    print(f"Modelin sınıfları: {model.names}")

    image_dir = Path(IMAGE_DIR)
    images = sorted(image_dir.glob("*.jpg"))
    print(f"Toplam görüntü sayısı: {len(images)}\n")

    skipped   = 0
    labeled   = 0
    total_det = 0

    for i, img_path in enumerate(images, 1):
        if i % 50 == 0 or i == 1 or i == len(images):
            print(f"  [{i}/{len(images)}] {img_path.name} işleniyor...")

        results = model(str(img_path), size=IMG_SIZE)
        preds   = results.pred[0]  # [N, 6] → x1,y1,x2,y2,conf,cls

        label_path = img_path.with_suffix(".txt")

        if preds is None or len(preds) == 0:
            label_path.write_text("", encoding="utf-8")
            skipped += 1
        else:
            img_h, img_w = results.ims[0].shape[:2]

            lines = []
            for det in preds:
                x1, y1, x2, y2, conf, cls = det.tolist()
                cls_id = int(cls)
                x_c = (x1 + x2) / 2 / img_w
                y_c = (y1 + y2) / 2 / img_h
                w   = (x2 - x1) / img_w
                h   = (y2 - y1) / img_h
                lines.append(f"{cls_id} {x_c:.6f} {y_c:.6f} {w:.6f} {h:.6f}")

            label_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            labeled   += 1
            total_det += len(preds)

    print("\n" + "=" * 50)
    print(f"✅ Tamamlandı!")
    print(f"   Etiketlenen görüntü : {labeled}")
    print(f"   Boş etiket (0 obj)  : {skipped}")
    print(f"   Toplam tespit        : {total_det}")
    print(f"   Etiket klasörü       : {IMAGE_DIR}")
    print("=" * 50)


if __name__ == "__main__":
    main()
