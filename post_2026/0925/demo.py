import os
import time

os.environ["HF_HOME"] = "./pretrained"

import torch
from PIL import Image
from transformers import RTDetrImageProcessor, RTDetrV2ForObjectDetection
from visualize import show_detections

image = Image.open("./2008_000847.jpg")

image_processor = RTDetrImageProcessor.from_pretrained("PekingU/rtdetr_v2_r50vd")
model = RTDetrV2ForObjectDetection.from_pretrained("PekingU/rtdetr_v2_r50vd")

inputs = image_processor(images=image, return_tensors="pt")

start_time = time.perf_counter()

with torch.no_grad():
    outputs = model(**inputs)

end_time = time.perf_counter()
print("Elapsed time:", end_time - start_time)

results = image_processor.post_process_object_detection(
    outputs, target_sizes=torch.tensor([(image.height, image.width)]), threshold=0.5
)

for result in results:
    for score, label_id, box in zip(
        result["scores"], result["labels"], result["boxes"]
    ):
        score, label = score.item(), label_id.item()
        box = [round(i, 2) for i in box.tolist()]
        print(f"{model.config.id2label[label]}: {score:.2f} {box}")

# バウンディングボックスを描画して表示
show_detections(image, results, model.config.id2label)
