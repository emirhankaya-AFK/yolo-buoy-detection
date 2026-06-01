import os

labels_dir = r"c:\Users\emirh\Desktop\Kodlar\datasets\labels\train"
classes_file = os.path.join(labels_dir, "classes.txt")

print(f"Checking {classes_file}...")
if os.path.exists(classes_file):
    with open(classes_file, 'r') as f:
        classes = f.read().splitlines()
    print(f"Classes found: {classes} (count: {len(classes)})")
else:
    print("classes.txt NOT FOUND in labels dir!")

bad_files = []
all_indices = set()

for filename in os.listdir(labels_dir):
    if filename.endswith(".txt") and filename != "classes.txt":
        filepath = os.path.join(labels_dir, filename)
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.split()
                if parts:
                    idx = int(parts[0])
                    all_indices.add(idx)
                    if idx >= len(classes):
                        bad_files.append((filename, idx))

print(f"All indices found in labels: {all_indices}")
if bad_files:
    print(f"Found {len(bad_files)} instances where index >= class list length.")
    for f, idx in bad_files[:10]:
        print(f"  {f}: index {idx}")
else:
    print("All labels match the class list (if it has at least one class).")
