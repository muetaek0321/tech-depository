from mmap import mmap
import struct

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 定数
LENGTH = 6008


def main() -> None:
    # mmapの準備
    mm = mmap(-1, LENGTH, "test_memory")

    # 共有メモリからバイト列を読み込み
    byte_data = mm.read(LENGTH)

    # バイト列から目的のデータを抽出
    byte_img = byte_data[:6000] 
    byte_w = byte_data[6000:6004] 
    byte_h = byte_data[6004:6008] 
    
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
