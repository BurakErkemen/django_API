import cv2
import numpy as np
import os

# Absolute paths for the weights and config files
weights_path = "D:/GitHub/Back-End_ForAI/image_processing_backend/yolo_project/yolov3-tiny.weights"
config_path = "D:/GitHub/Back-End_ForAI/image_processing_backend/yolo_project/yolov3-tiny.cfg"
classes_path = "D:/GitHub/Back-End_ForAI/image_processing_backend/yolo_project/coco.names"

# Check if the files exist
if not os.path.exists(weights_path):
    raise FileNotFoundError(f"Weights file not found: {weights_path}")
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")
if not os.path.exists(classes_path):
    raise FileNotFoundError(f"Classes file not found: {classes_path}")

# Load Yolo
net = cv2.dnn.readNet(weights_path, config_path)
classes = []
with open(classes_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading image
image_path = "D:\GitHub\Back-End_ForAI\image_processing_backend\yolo_project\OIP.jpeg"

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found at path: {image_path}")

frame = cv2.imread(image_path)

# Check if the image was loaded successfully
if frame is None:
    raise FileNotFoundError(f"Image file not found or cannot be opened: {image_path}")

height, width, channels = frame.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.2:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)

for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = colors[class_ids[i]]
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

# Display the image
cv2.imshow("Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()