import os
os.environ["HF_HOME"] = "./pretrained"
from pathlib import Path

from yomitoku import TextDetector, TextRecognizer

import cv2
import pandas as pd


def main():
    td = TextDetector()
    tr = TextRecognizer()

    Path("./result").mkdir(parents=True, exist_ok=True)

    anno_dict = {"img": [], "text": []}

    image_dir_path = Path("./images")
    for image_path in image_dir_path.glob("*"):
        img = cv2.imread(image_path)
        
        layout = td(img)
        
        for i, pt in enumerate(layout[0].points):
            x1, y1 = pt[0]
            x2, y2 = pt[2]
            
            try:
                crop_img = img
                crop_img = crop_img[y1:y2, x1:x2]
                crop_img_name = f"{Path(image_path).stem}_{i+1}.png"
                cv2.imwrite(f"./result/{crop_img_name}", crop_img)
            except:
                continue
            
            result = tr(crop_img)
            text = result[0].contents[0]
            text = text.replace("·", "・")
            
            anno_dict["img"].append(crop_img_name)
            anno_dict["text"].append(text)
            print(text)
        
    anno_df = pd.DataFrame(anno_dict)
    anno_df.to_csv("./result/annotations.csv", encoding="cp932", index=False)
        

if __name__ == "__main__":
    main()
