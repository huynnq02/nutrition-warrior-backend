# food_detection/yolo/detect.py
import torch
from pathlib import Path
from PIL import Image


def load_yolo_model(model_path='yolo.pt'):
    model_path = Path(__file__).parent / model_path  # Adjust the path to the model file
    device = select_device('')
    model = attempt_load(model_path, map_location=device)
    stride = int(model.stride.max())
    return model, stride, device

def detect_food(image_path, model, stride, device):
    # Load image
    img0 = Image.open(image_path)

    # Inference
    img = torch.zeros((1, 3, img0.shape[0], img0.shape[1]), device=device)  # Init img
    img[0] = torch.from_numpy(img0).to(device).float()  # Convert

    # Inference
    img = img.float() / 255.0  # 0 - 255 to 0.0 - 1.0
    pred = model(img, augment=False)[0]

    # Apply NMS
    pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic=False)[0]

    # Process detections
    food_items = []
    for det in pred:
        if det is not None and len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()
            for *xyxy, conf, cls in reversed(det):
                food_items.append({
                    'class': int(cls),
                    'confidence': float(conf),
                    'bbox': [float(xyxy[0]), float(xyxy[1]), float(xyxy[2]), float(xyxy[3])]
                })

    return food_items

