import requests
import torch
from PIL import Image
from transformers import AutoImageProcessor, Mask2FormerForUniversalSegmentation
import numpy as np
import cv2


COLORS = [
    (163, 8, 154), (31, 241, 13), (147, 39, 121), (246, 231, 135), (100, 87, 247), 
    (139, 122, 15), (81, 185, 168), (96, 11, 110), (49, 118, 245), (14, 118, 68), 
    (144, 168, 104), (58, 38, 203), (197, 203, 5), (137, 48, 203), (106, 140, 32), 
    (27, 240, 225), (63, 165, 168), (108, 26, 117), (29, 146, 246), (244, 186, 126), 
    (2, 233, 72), (85, 150, 219), (229, 24, 54), (254, 139, 135), (226, 138, 195)
]

# load Mask2Former fine-tuned on COCO instance segmentation
processor = AutoImageProcessor.from_pretrained("facebook/mask2former-swin-small-coco-instance")
model = Mask2FormerForUniversalSegmentation.from_pretrained("facebook/mask2former-swin-small-coco-instance")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

# model predicts class_queries_logits of shape `(batch_size, num_queries)`
# and masks_queries_logits of shape `(batch_size, num_queries, height, width)`
class_queries_logits = outputs.class_queries_logits
masks_queries_logits = outputs.masks_queries_logits

# you can pass them to processor for postprocessing
result = processor.post_process_instance_segmentation(outputs, target_sizes=[image.size[::-1]])[0]
# we refer to the demo notebooks for visualization (see "Resources" section in the Mask2Former docs)
predicted_instance_map = result["segmentation"]

# 元画像
ori_img = np.array(image).astype(np.uint8)

# セグメンテーション結果
seg_img = cv2.cvtColor(predicted_instance_map.cpu().numpy().astype(np.uint8), cv2.COLOR_GRAY2RGB)
for lbl in np.unique(seg_img):
    seg_img = np.where(seg_img==lbl, COLORS[lbl], seg_img)
seg_img = seg_img.astype(np.uint8)
    
# 合成画像
alpha = 0.9
blend_img = cv2.addWeighted(ori_img, 1, seg_img, alpha, 0)

# 出力
output_img = np.hstack([ori_img, seg_img, blend_img], dtype=np.uint8)
cv2.imwrite("mask2former_seg_img.png", output_img)