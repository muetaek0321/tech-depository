import wx
import numpy as np
import cv2


__all__ = ["CreatePanel", "CreateTextLabel", "CreateButton",
           "CreateImagePanel"]

# 定数
DEFAULT_COLOR = (200, 200, 200)
TEXT_STYLE = {"center": wx.TE_CENTER, "left": wx.TE_LEFT, "right": wx.TE_RIGHT}


class CreatePanel(wx.Panel):
    def __init__(self, parent, size=wx.DefaultSize, color=DEFAULT_COLOR):
        super().__init__(parent, wx.ID_ANY, size=size)
        self.SetBackgroundColour(color)
        
        
class CreateTextLabel(wx.StaticText):
    def __init__(self, parent, text, fontsize=10, style="center"):
        super().__init__(parent, wx.ID_ANY, text, style=TEXT_STYLE[style])
        # フォント設定
        font = wx.Font(fontsize, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.SetFont(font)
        
        
class CreateButton(wx.Button):
    def __init__(self, parent, label, size=wx.DefaultSize):
        super().__init__(parent, wx.ID_ANY, label, size=size)
        
        
class CreateImagePanel(wx.Panel):
    def __init__(self, parent, size=wx.DefaultSize, color=DEFAULT_COLOR,
                 init_img=None):
        super().__init__(parent, wx.ID_ANY, size=size)
        self.SetBackgroundColour(color)
        
        # 初期表示の画像を設定
        if init_img is None:
            init_img = np.full((size[1], size[0], 3), 255).astype(np.uint8)
            init_img = cv2.cvtColor(init_img, cv2.COLOR_BGR2RGB)
        self.bitmap = wx.Bitmap.FromBuffer(init_img.shape[1], init_img.shape[0], init_img)
        
        # 描画イベントを作成
        self.Bind(wx.EVT_PAINT, self.on_paint)
        
    def on_paint(self, event=None):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()
        dc.DrawBitmap(self.bitmap, 0, 0, True)
        
    def set_image(self, img):
        """パネルに表示する画像の切り替え
        """
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.bitmap = wx.Bitmap.FromBuffer(img.shape[1], img.shape[0], img)
        self.Refresh(False)
        
