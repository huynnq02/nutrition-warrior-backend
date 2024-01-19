from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ultralytics import YOLO
import numpy as np
import os
import json
from ..model.class_name import class_names
@api_view(['POST'])
def detect_objects(request):
    """
    Detect objects in an image using custom YOLOv8n trained model.

    Required POST parameters:
    - image: The image file for object detection.

    Returns:
    Response: The HTTP response containing the detected objects.

    Raises:
    Exception: If any error occurs during object detection.
    """
    try:
        # Load the YOLOv8n model
        model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'nutrition-warrior-model.pt')
        model = YOLO(model_path)
        print("Go inside it!")
        image_file = request.FILES.get('image')
        print(image_file)
        if not image_file:
            return Response({'success': False, 'message': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        with open('uploaded_image.jpg', 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        results_list = model.predict('uploaded_image.jpg') 
        print(results_list)

        out = []
        simplified_objects = []
        unique_classes = []
        for result in results_list:
            bboxes = []
            labels = []
            scores = []

            boxes = result.boxes.cpu().numpy()
            for _, box in enumerate(boxes):
                r = box.xyxy[0].astype(int)
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                bboxes.append(r)
                labels.append(cls)
                scores.append(conf)
            
            if len(bboxes) == 0:
                continue

            

            for i in range(len(bboxes)):
                cls = labels[i]
                score = scores[i]
                class_name = class_names[cls]
                if score > 0.5 and cls not in unique_classes:
                    unique_classes.append(cls)
                    simplified_objects.append([cls, class_name, score])

    
           


        return Response({'success': True, 'message': 'Object detection successful', 'detected_objects': simplified_objects}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
