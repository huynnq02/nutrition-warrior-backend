import cv2
import numpy as np

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

def perform_detection(image_path):
    net = cv2.dnn.readNet("./nutrition-warrior-model.pt", None)
    classes = None

    with open("./coco.names", 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    output_layers = get_output_layers(net)

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Normalize the image and convert to blob
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform forward pass
    detections = net.forward(output_layers)

    # Parse the detections
    detected_objects = []

    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Adjust confidence threshold 
                center_x, center_y, w, h = (obj[0:4] * np.array([width, height, width, height])).astype(int)
                x, y = int(center_x - w/2), int(center_y - h/2)

                detected_objects.append({
                    'class_name': classes[class_id],
                    'confidence': float(confidence),
                    'box': [x, y, w, h]
                })

    return detected_objects

image_path = "./test.jpg"
detected_objects = perform_detection(image_path)
print(detected_objects)
