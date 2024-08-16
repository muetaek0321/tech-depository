import wx
import numpy as np
import cv2

from .wxpy.widgets import DEFAULT_COLOR, CreateImagePanel


class PlayPanel(CreateImagePanel):
    def __init__(
        self, 
        parent: wx.Frame | wx.Panel, 
        size: tuple[int, int]
    ) -> None:
        """コンストラクタ
        
        Args:
            parent (wx.Frame,wx.Panel): 親要素
            size (tuple): パネルのサイズ
        """
        super().__init__(parent, size, DEFAULT_COLOR)
        self.parent = parent
        self.size = size
        
        self.board = [[""]*3 for _ in range(3)]
        self.turn = "O"
        
        # OとXの画像を読み込み
        self.maru_img = cv2.imread("./images/maru.png", cv2.IMREAD_UNCHANGED)
        self.batsu_img = cv2.imread("./images/batsu.png", cv2.IMREAD_UNCHANGED)
        
        # 3x3のマス目の画像を作成
        self.create_init_board_image()
        # 作成した画像を表示しておく
        self.set_image(self.board_img)
        
        # クリックイベントを作成
        self.Bind(wx.EVT_LEFT_DOWN, self.click_board)
        
    def create_init_board_image(
        self
    ) -> None:
        """ゲーム開始前の状態の画像を作成
        """
        self.board_img = np.full((self.size[1], self.size[0], 3), 255).astype(np.uint8)
        cv2.line(self.board_img, (0, 160), (self.size[0], 160), (0, 0, 0), 2)
        cv2.line(self.board_img, (0, 320), (self.size[0], 320), (0, 0, 0), 2)
        cv2.line(self.board_img, (160, 0), (160, self.size[0]), (0, 0, 0), 2)
        cv2.line(self.board_img, (320, 0), (320, self.size[0]), (0, 0, 0), 2)

    def update_board(
        self, 
        board_x: int, 
        board_y: int,
    ) -> None:
        """boardの配列と画像の更新
        
        Args:
            board_x (int): 盤面のX方向の位置 
            board_y (int): 盤面のY方向の位置 
        """
        # board配列の更新
        self.board[board_y][board_x] = self.turn
        
        # board画像の更新と画面表示の更新
        x1, y1, x2, y2 = 160*board_x, 160*board_y, 160*board_x+160, 160*board_y+160
        if self.turn == "O":
            turn_img = self.maru_img
        elif self.turn == "X":
            turn_img = self.batsu_img

        self.board_img[y1:y2, x1:x2] = self.board_img[y1:y2, x1:x2] * (1 - turn_img[:, :, 3:] / 255) + \
                                       turn_img[:, :, :3] * (turn_img[:, :, 3:] / 255)
        self.set_image(self.board_img)
        
        # 勝敗を確認
        judge = self.check_winner()
        if judge == "":
            # ターンプレイヤーの交代
            if self.turn == "O":
                self.turn = "X"
            elif self.turn == "X":
                self.turn = "O"
            self.parent.SetStatusText(f"\"{self.turn}\"のターンです。")
        elif judge == "draw":
            # 引き分けを表示して終了
            self.parent.SetStatusText(f"引き分けです。")
        else:
            # 勝者を表示して終了
            self.parent.SetStatusText(f"\"{judge}\"の勝利です！")
            self.Disable()        
        
    def check_winner(
        self
    ) -> None:
        """勝敗の確認
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":  # Check rows
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":  # Check columns
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":  # Check main diagonal
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":  # Check other diagonal
            return self.board[0][2]
        
        # 引き分け判定
        for row in self.board:
            if "" in row:
                return ""
        
        return "draw"
    
    def reset_state(
        self
    ) -> None:
        """状態をリセット
        """
        self.board = [[""]*3 for _ in range(3)]
        self.turn = "O"
        self.parent.SetStatusText(f"\"{self.turn}\"のターンです。")
        self.create_init_board_image()
        self.set_image(self.board_img)

    def click_board(
        self, 
        event: wx.Event = None
    ) -> None:
        """ボード領域をクリックした時のイベント
        
        Args:
            event (wx.Event): イベントオブジェクト
        """
        # クリックした位置の座標を取得
        x, y = event.GetPosition()
        
        # 位置座標からボードの座標を取得
        ## (0, 0)
        if (0 <= x < 160) and (0 <= y < 160):
            board_x, board_y = 0, 0  
        ## (0, 1)
        elif (0 <= x < 160) and (160 <= y < 320):
            board_x, board_y = 0, 1
        ## (0, 2)
        elif (0 <= x < 160) and (320 <= y < 480):
            board_x, board_y = 0, 2
        ## (1, 0)
        elif (160 <= x < 320) and (0 <= y < 160):
            board_x, board_y = 1, 0
        ## (1, 1)
        elif (160 <= x < 320) and (160 <= y < 320):
            board_x, board_y = 1, 1
        ## (1, 2)
        elif (160 <= x < 320) and (320 <= y < 480):
            board_x, board_y = 1, 2
        ## (2, 0)
        elif (320 <= x < 480) and (0 <= y < 160):
            board_x, board_y = 2, 0
        ## (2, 1)
        elif (320 <= x < 480) and (160 <= y < 320):
            board_x, board_y = 2, 1
        ## (2, 2)
        elif (320 <= x < 480) and (320 <= y < 480):
            board_x, board_y = 2, 2
            
        # 入力可能なboard座標か確認
        if self.board[board_y][board_x] == "":
             # ボードの更新
            self.update_board(board_x, board_y)   
        
        