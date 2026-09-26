import os
import time

os.environ["HF_HOME"] = "./pretrained"

import torch
from PIL import Image
from transformers import AutoImageProcessor, RfDetrForObjectDetection
from visualize import show_detections

image = Image.open("./2008_002610.jpg")

processor = AutoImageProcessor.from_pretrained("stevenbucaille/rf-detr-base")
model = RfDetrForObjectDetection.from_pretrained("stevenbucaille/rf-detr-base")

inputs = processor(images=image, return_tensors="pt")

start_time = time.perf_counter()

with torch.no_grad():
    outputs = model(**inputs)

end_time = time.perf_counter()
print("Elapsed time:", end_time - start_time)

target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(
    outputs, target_sizes=target_sizes, threshold=0.5
)[0]

for score, label, box in list(
    zip(results["scores"], results["labels"], results["boxes"])
)[:8]:
    box = [round(i, 2) for i in box.tolist()]
    print(
        f"Detected {model.config.id2label[label.item()]} with confidence "
        f"{round(score.item(), 3)} at location {box}"
    )

# バウンディングボックスを描画して表示
show_detections(image, results, model.config.id2label)
