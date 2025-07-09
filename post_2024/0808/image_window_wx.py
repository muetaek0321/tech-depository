import wx
import cv2
import numpy as np

from utils import imread_jpn


# 定数
DEFAULT_COLOR = (200, 200, 200)


class CreateImagePanel(wx.Panel):
    """画像表示パネル"""
    
    def __init__(
        self, 
        parent: wx.Frame | wx.Panel, 
        size: tuple[int, int] = wx.DefaultSize, 
        color: tuple[int, int, int] = DEFAULT_COLOR,
        init_img: np.ndarray = None
    ) -> None:
        """コンストラクタ
        
        Args:
            parent (wx.Frame, wx.Panel): 親要素
            size (tuple): パネルのサイズ
            color (tuple): パネルの背景色
            init_img (np.ndarray): 初期設定画像
        """
        super().__init__(parent, wx.ID_ANY, size=size)
        self.SetBackgroundColour(color)
        
        # 初期表示の画像を設定
        if init_img is None:
            init_img = np.full((*size, 3), 255).astype(np.uint8)
        init_img = cv2.cvtColor(init_img, cv2.COLOR_BGR2RGB)
        self.bitmap = wx.Bitmap.FromBuffer(init_img.shape[1], init_img.shape[0], init_img)
        
        # 描画イベントを作成
        self.Bind(wx.EVT_PAINT, self.on_paint)
        
    def on_paint(
        self,
        event: wx.Event = None
    ) -> None:
        """描画イベント
        
        Args:
            event (wx.Event): イベントオブジェクト
        """
        dc = wx.BufferedPaintDC(self)
        dc.Clear()
        dc.DrawBitmap(self.bitmap, 0, 0, True)
        
    def set_image(
        self, 
        img: np.ndarray
    ) -> None:
        """パネルに表示する画像の切り替え
        
        Args:
            img (np.ndarray): 表示する画像
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.bitmap = wx.Bitmap.FromBuffer(img.shape[1], img.shape[0], img)
        self.Refresh(False)
        

class ImageShowWindow(wx.Frame):
    """画像を表示するウィンドウ"""
    
    def __init__(
        self,
        title: str,
        img: np.ndarray,
        size: tuple[int, int]
    ) -> None:
        """コンストラクタ
        
        Args:
            title (str): ウィンドウタイトル
            img (np.ndarray): OpenCV形式の画像データ
            size (tuple): ウィンドウサイズ
        """
        super().__init__(None, wx.ID_ANY, title=title, size=size)
        
        img_pnl = CreateImagePanel(self, size, init_img=img)
        layout = wx.BoxSizer()
        layout.Add(img_pnl)
        self.SetSizer(layout)
        
        # ウィンドウを閉じる
        self.Bind(wx.EVT_CLOSE, self.click_close_button)
        
        self.Show()
        self.Refresh()
        
    def click_close_button(
        self, 
        event = None
    ) -> None:
        """ウィンドウ上部の閉じるボタン（×ボタン）を押したときの処理
        
        Args:
            event (wx.Event): イベントオブジェクト
        """
        self.Destroy()
        

def image_window(
    title: str,
    img: np.ndarray
) -> None:
    """日本語のタイトルを表示可能な画像表示ウィンドウ
    
    Args:
        title (str): ウィンドウタイトル
        img (np.ndarray): OpenCV形式の画像データ
    """
    app = wx.App()
    height, width = img.shape[:2]
    ImageShowWindow(title, img, size=(width, height))    
    app.MainLoop()


if __name__ == "__main__":
    print("日本語タイトルの画像ウィンドウを表示します")
    # タイトル（日本語文字列）
    title = "テスト"
    
    # 表示する画像を読み込み（OpenCV）
    img = imread_jpn("./サンプル画像.jpg")
    
    image_window(title, img)
    
    print("終了します")