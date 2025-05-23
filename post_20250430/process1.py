from mmap import mmap
import struct

import cv2


# 定数
LENGTH = 6008
SIZE = (40, 50)
# LENGTH = 589832
# SIZE = (384, 512)


def main() -> None:
    # mmapの準備
    mm = mmap(-1, LENGTH, "test_memory")

    # 画像読み込み+リサイズ
    img = cv2.imread("./img.png")
    img = cv2.resize(img, SIZE)
    h, w = img.shape[:2]

    # 画像と画像の幅・高さをバイト列に変換
    byte_img = img.tobytes()
    byte_w = struct.pack("i", w)
    byte_h = struct.pack("i", h)

    # メモリに書き込み
    mm.write(byte_img + byte_w + byte_h)
    mm.flush()
    mm.seek(0)
    
    # バイト列の長さを確認
    print("Image:", len(byte_img)) # 6000
    print("width:", len(byte_w))   # 4
    print("height:", len(byte_h))  # 4

    input('push enter to exit.')

    mm.close()


if __name__ == "__main__":
    main()
