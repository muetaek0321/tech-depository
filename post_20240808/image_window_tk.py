import tkinter as tk

import cv2
import numpy as np
from PIL import Image, ImageTk

from utils import imread_jpn


def image_window(
    title: str,
    img: np.ndarray
) -> None:
    """日本語のタイトルを表示可能な画像表示ウィンドウ
    
    Args:
        title (str): ウィンドウタイトル
        img (np.ndarray): OpenCV形式の画像データ
    """
    height, width = img.shape[:2]
    
    window = tk.Tk()
    window.geometry(f"{width}x{height}")
    window.title(title)
    
    # キャンバス作成
    canvas = tk.Canvas(window, height=height, width=width)
    # キャンバス表示
    canvas.pack()
    
    # Pillow形式に変換→tkinter用に変換
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    # キャンバスに画像を表示
    canvas.create_image(0, 0, image=img_tk, anchor='nw')
    
    window.mainloop()


if __name__ == "__main__":
    print("日本語タイトルの画像ウィンドウを表示します")
    # タイトル（日本語文字列）
    title = "テスト"
    
    # 表示する画像を読み込み（OpenCV）
    img = imread_jpn("./サンプル画像.jpg")
    
    # # 試しにOpenCVのウィンドウで表示してみる
    # cv2.imshow(title, img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    image_window(title, img)
    
    print("終了します")