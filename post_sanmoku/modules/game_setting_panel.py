import wx

from .wxpy import DEFAULT_COLOR
from .wxpy import CreatePanel, CreateTextLabel, CreateButton


class SettingPanel(CreatePanel):
    def __init__(
        self, 
        parent: wx.Frame | wx.Panel, 
        size: tuple[int, int],
        color: tuple[int, int, int]
    ) -> None:
        """コンストラクタ
        
        Args:
            parent (wx.Frame,wx.Panel): 親要素
            size (tuple): パネルのサイズ
            color (tuple): パネルの背景色
        """
        super().__init__(parent, size, color)
        self.parent = parent
        
        # ウィジェット設定
        self.select_pnl = SelectPlayerPanel(self, (380, 80), DEFAULT_COLOR)
        self.start_btn = CreateButton(self, "開始", (60, 45))
        self.start_btn.Bind(wx.EVT_BUTTON, self.click_start_btn)
        
        # レイアウト設定
        layout = wx.FlexGridSizer(rows=1, cols=2, gap=(0, 0))
        layout.Add(self.select_pnl, flag=wx.ALIGN_CENTER)
        layout.Add(self.start_btn, flag=wx.ALIGN_CENTER)
        layout.AddGrowableRow(0)
        layout.AddGrowableCol(0)
        layout.AddGrowableCol(1)
        self.SetSizer(layout)
        
    def click_start_btn(
        self, 
        event: wx.Event = None
    ) -> None:
        """開始ボタンを押したときのイベント
        
        Args:
            event (wx.Event): イベントオブジェクト
        """
        player1 = [
            self.select_pnl.p1_user_radio_btn.GetValue(),
            self.select_pnl.p1_random_radio_btn.GetValue(),
            self.select_pnl.p1_minimax_radio_btn.GetValue(),
            self.select_pnl.p1_qlearning_radio_btn.GetValue()
        ]
        player2 = [
            self.select_pnl.p2_user_radio_btn.GetValue(),
            self.select_pnl.p2_random_radio_btn.GetValue(),
            self.select_pnl.p2_minimax_radio_btn.GetValue(),
            self.select_pnl.p2_qlearning_radio_btn.GetValue()
        ]
        
        # ゲーム画面表示する
        self.parent.play_pnl.Enable()
        self.parent.play_pnl.reset_state()

class SelectPlayerPanel(CreatePanel):
    def __init__(self, parent, size, color):
        super().__init__(parent, size, color)
        
        # ウィジェット設定
        fontsize = 11
        player1_lbl = CreateTextLabel(self, "PLAYER1:", fontsize)
        player2_lbl = CreateTextLabel(self, "PLAYER2:", fontsize)
        user_lbl = CreateTextLabel(self, "user", fontsize)
        random_lbl = CreateTextLabel(self, "random", fontsize)
        minimax_lbl = CreateTextLabel(self, "minimax", fontsize)
        qlearning_lbl = CreateTextLabel(self, "q-learning", fontsize)
        
        self.p1_user_radio_btn = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.p1_random_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        self.p1_minimax_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        self.p1_qlearning_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        
        self.p2_user_radio_btn = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.p2_random_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        self.p2_minimax_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        self.p2_qlearning_radio_btn = wx.RadioButton(self, wx.ID_ANY, "")
        
        # レイアウト設定
        layout = wx.GridSizer(rows=3, cols=5, gap=(0, 0))
        layout.Add(CreatePanel(self), flag=wx.ALIGN_CENTER)
        layout.Add(user_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(random_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(minimax_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(qlearning_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(player1_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(self.p1_user_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p1_random_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p1_minimax_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p1_qlearning_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(player2_lbl, flag=wx.ALIGN_CENTER)
        layout.Add(self.p2_user_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p2_random_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p2_minimax_radio_btn, flag=wx.ALIGN_CENTER)
        layout.Add(self.p2_qlearning_radio_btn, flag=wx.ALIGN_CENTER)
        self.SetSizer(layout)