import wx

from modules.wxpy import CreateInitWindow, DEFAULT_COLOR
from modules.game_setting_panel import SettingPanel
from modules.game_play_panel import PlayPanel

class MainWindow(CreateInitWindow):
    def __init__(self) -> None:
        super().__init__(title="三目並べ対戦GUI", size=(500, 625))

        # ステータスバーを表示する
        self.CreateStatusBar()
        self.SetStatusText("対戦相手を設定し、開始してください！")
        
        self.setting_pnl = SettingPanel(self, (480, 80), DEFAULT_COLOR)
        self.play_pnl = PlayPanel(self, (480, 480))
        self.play_pnl.Disable()
        
        # レイアウト設定
        layout = wx.FlexGridSizer(rows=2, cols=1, gap=(0, 0))
        layout.Add(self.setting_pnl, flag=wx.ALIGN_CENTER)
        layout.Add(self.play_pnl, flag=wx.ALIGN_CENTER)
        layout.AddGrowableCol(0)
        self.SetSizer(layout)
        
        self.Show()
        

if __name__ == "__main__":
    app = wx.App()
    main_win = MainWindow()
    app.MainLoop()
    