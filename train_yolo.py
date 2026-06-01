from ultralytics import YOLO

# Load a model
model = YOLO('yolo11n.pt')  # load a pretrained model
# Train the model
results = model.train(data=r'C:\Users\emirh\Desktop\dataset_iha_hazir\data.yaml', epochs=80, imgsz=640, batch=16)
