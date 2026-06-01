import os
import glob
import sys

dir_path = r"C:\Users\emirh\Desktop\emirhan_2602"
if not os.path.exists(dir_path):
    print("Dizin bulunamadi:", dir_path)
    sys.exit(1)

classes_file = os.path.join(dir_path, "classes.txt")

try:
    with open(classes_file, "w", encoding="utf-8") as f:
        f.write("iha\n")
except Exception as e:
    print(f"classes.txt yazilamadi: {e}")
    sys.exit(1)

txt_files = glob.glob(os.path.join(dir_path, "*.txt"))
count = 0

for txt_file in txt_files:
    if os.path.basename(txt_file) == "classes.txt":
        continue
    
    with open(txt_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    modified = False
    
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 5: # Gecerli YOLO formati: <class> <x> <y> <w> <h>
            if parts[0] != "0": # Eger sinif 0 degilse
                parts[0] = "0"
                modified = True
            new_lines.append(" ".join(parts) + "\n")
        else:
            new_lines.append(line) # Bos satir vs ise dokunma
            
    if modified:
        with open(txt_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            count += 1
            
print(f"Islem tamamlandi. classes.txt 'iha' olarak guncellendi ve {count} adet etiket dosyasindaki cizimlerin siniflari 0 (iha) yapildi.")
