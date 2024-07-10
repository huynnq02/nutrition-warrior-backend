from ultralytics import YOLO
model = YOLO('./nutrition-warrior-model.pt')
source = './eggggg.jpg'
results = model(source)  
print(results)