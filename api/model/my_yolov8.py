from ultralytics import YOLO
model = YOLO('nutrition-warrior-model.pt')
source = 'name.jpg'
results = model(source)  
print(results)