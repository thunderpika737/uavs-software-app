from ultralytics import YOLO

model = YOLO("./vision/yolov8.yaml")
results = model.train(data="./vision/model.yaml", epochs=100, imgsz=640, batch=1, val=True, pretrained=True) 