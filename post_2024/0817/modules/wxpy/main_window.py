import wx


__all__ = ["CreateInitWindow", "DEFAULT_COLOR"]

DEFAULT_COLOR = (200, 200, 200)

class CreateInitWindow(wx.Frame):
    def __init__(self, title, size, color=DEFAULT_COLOR) -> None:
        super().__init__(None, wx.ID_ANY, title, size=size)
        self.SetBackgroundColour(color)
        
        # ウィンドウを閉じる
        self.Bind(wx.EVT_CLOSE, self.click_close_button)
        
    def click_close_button(self, event=None) -> None:
        """
        ウィンドウ上部の閉じるボタン（×ボタン）を押したときの処理
        ウィンドウを閉じる機能のみの実装
        """
        print("アプリを終了します")
        self.Destroy()

        