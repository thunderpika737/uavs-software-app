from ultralytics import YOLO, settings

model = YOLO("./vision/yolov8.yaml")
results = model.train(data="./vision/paths.yaml", epochs=100, imgsz=640, batch=1, val=True)