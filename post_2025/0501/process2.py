from mmap import mmap
import struct

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 定数
LENGTH = 600000


def main() -> None:
    # mmapの準備
    mm = mmap(-1, LENGTH, "test_memory")

    # 共有メモリからバイト列を読み込み
    byte_data = mm.read(LENGTH)
    
    # 終端文字列までを取得
    byte_data = byte_data.split(b"<END>")[0]
    # 区切り文字で分割して分けて目的のデータを抽出
    byte_img, byte_w, byte_h = byte_data.split(b"<SEP>")
    
    # バイト列のデータを変換
    w = struct.unpack("i", byte_w)[0]
    h = struct.unpack("i", byte_h)[0]
    img = np.frombuffer(byte_img, np.uint8).reshape((h,w,3))
    
    # 画像を表示
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

    mm.close()


if __name__ == "__main__":
    main()
