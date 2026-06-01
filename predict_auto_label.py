from ultralytics import YOLO
import os
import shutil

# Varsayılan best.pt yolu (eğitim bittikten sonra oluşacak)
# Genellikle runs/detect/train/weights/best.pt olur.
model_path = os.path.abspath("runs/detect/train/weights/best.pt")
# Eğer ilk eğitim değilse train2, train3 vb. olabilir, en güncelini bulalım:
runs_dir = os.path.abspath("runs/detect")
if os.path.exists(runs_dir):
    train_dirs = [os.path.join(runs_dir, d) for d in os.listdir(runs_dir) if d.startswith("train")]
    if train_dirs:
        # En son değiştirilen train klasörünü buluyoruz
        latest_train = max(train_dirs, key=os.path.getmtime)
        possible_best = os.path.join(latest_train, "weights", "best.pt")
        if os.path.exists(possible_best):
            model_path = possible_best

# Eğer best.pt bulunamazsa varsayılan olarak yereldeki yolo11n.pt'yi kullan veya indir
if not os.path.exists(model_path):
    local_default = os.path.abspath("yolo11n.pt")
    if os.path.exists(local_default):
        model_path = local_default
    else:
        model_path = "yolo11n.pt"  # İnternetten otomatik indirir

print(f"Kullanılacak model: {model_path}")

try:
    model = YOLO(model_path)
except Exception as e:
    print(f"Model yüklenemedi: {e}")
    exit(1)

input_dir = r"C:\Users\emirh\Desktop\yeni_resimler"
output_dir = r"C:\Users\emirh\Desktop\auto_labeled_output"
os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(input_dir) or len(os.listdir(input_dir)) == 0:
    os.makedirs(input_dir, exist_ok=True)
    print(f"UYARI: Etiketlenecek resimlerin yer alacağı '{input_dir}' klasörü boş veya mevcut değildi, otomatik oluşturuldu.")
    print("Lütfen bu klasörün içerisine etiketlemek istediğiniz duba/nesne resimlerini yerleştirip betiği yeniden çalıştırın.")
    exit(0)

print("Otomatik etiketleme başlatılıyor...")

# Resimlerin bulunduğu klasörde tahmin yap ve etiketleri kaydet
results = model.predict(source=input_dir, save_txt=True, save_conf=True, conf=0.25, project=output_dir, name="predict_labels")

print("Etiketleme tamamlandı!")

# Etiketleri ve resimleri tek bir klasöre toplama
predict_dir = os.path.join(output_dir, "predict_labels")
labels_dir = os.path.join(predict_dir, "labels")

if os.path.exists(labels_dir):
    for label_file in os.listdir(labels_dir):
        if label_file.endswith(".txt"):
            txt_path = os.path.join(labels_dir, label_file)
            base_name = os.path.splitext(label_file)[0]
            
            # Resim dosyasını bul (jpg, png, jpeg olabilir)
            img_found = False
            for ext in [".jpg", ".png", ".jpeg", ".JPG", ".PNG", ".JPEG"]:
                possible_img = os.path.join(input_dir, base_name + ext)
                if os.path.exists(possible_img):
                    # Kopyala
                    dest_img = os.path.join(output_dir, base_name + ext)
                    dest_txt = os.path.join(output_dir, label_file)
                    
                    shutil.copy2(possible_img, dest_img)
                    shutil.copy2(txt_path, dest_txt)
                    img_found = True
                    break
            
            if not img_found:
                print(f"UYARI: {label_file} için ilgili resim dosyası bulunamadı.")
                
    print(f"Tüm resimler ve etiketler '{output_dir}' klasörüne kopyalandı.")
    print("LabelImg ile bu klasörü açarak düzenleme yapabilirsiniz.")
else:
    print("Hiçbir etiket (label) bulunamadı. Yeni resimlerde nesne tespit edilmemiş olabilir.")
