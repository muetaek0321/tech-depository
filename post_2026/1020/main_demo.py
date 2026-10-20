import os
import sys
import time
from pathlib import Path

os.environ["HF_HOME"] = "./pretrained"

import cv2
import indra_ocr
import numpy as np

# Windows環境での標準出力エンコーディング対策
sys.stdout.reconfigure(encoding="utf-8")

# モデルの読み込み
conv = indra_ocr.load(threads=4)

input("\n\n\naaaaaa")

# 画像の読み込み
img_path = "./data/PXL_20251004_065751955.jpg"
# img_path = "./data/PXL_20251004_070342022.jpg"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCRを実行
start_time = time.perf_counter()
page = conv.ocr(gray)
elapsed_time = time.perf_counter() - start_time
print(page.text)
print(f"Elapsed time: {elapsed_time:.4f}")

# 回転補正: page.lines の座標は正立(upright)した画像に対応しているため、
# 画像側も page.rotation に合わせて回転させます
vis_img = img.copy()
k = page.rotation // 90
if k != 0:
    vis_img = np.ascontiguousarray(np.rot90(vis_img, -k))

# 画像に矩形を描画して可視化
for line in page.lines:
    x0, y0, x1, y1 = map(int, line.box)
    # 矩形を描画 (緑色, 太さ3)
    cv2.rectangle(vis_img, (x0, y0), (x1, y1), (0, 255, 0), 3)

# 回転している場合にもとに戻す
if k != 0:
    vis_img = np.ascontiguousarray(np.rot90(vis_img, k))

# 結果を保存
output_path = f"./result_detected_{Path(img_path).stem}.jpg"
cv2.imwrite(output_path, vis_img)
print(f"可視化画像を保存しました: {output_path}")
