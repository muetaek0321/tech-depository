import configparser
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

from utils import get_ai_input, q_learning, make_q_table


def judge(play_area, inputter):
    """
    ゲーム終了及び勝者を判定する

    ゲームの状況をあらわすリストと直前の入力者を受け取り、
    ゲームが終了していれば勝者と終了判定を返す
    """
    end_flg = 0
    winner = 'NOBODY'
    first_list = [0, 3, 6, 0, 1, 2, 0, 2]
    second_list = [1, 4, 7, 3, 4, 5, 4, 4]
    third_list = [2, 5, 8, 6, 7, 8, 8, 6]
    for first, second, third in zip(first_list, second_list, third_list):
        if play_area[first] == play_area[second] \
        and play_area[first] == play_area[third]:
            winner = inputter
            end_flg = 1
            break
    choosable_area = [str(area) for area in play_area if type(area) is int]
    if len(choosable_area) == 0:
        end_flg = 1
    return winner, end_flg


def randomAI_vs_QLAI(first_inputter, q_table, params, epsilon=0):
    """
    AI(ランダム)とAI(Q学習)のゲームを実行する関数

    先手(1:AI(ランダム)、2:AI(Q学習))とQテーブルを受け取り、
    ゲームが終了するまで実行する
    """
    inputter1 = 'Random AI'
    inputter2 = 'QL AI'

    # Q学習退避用
    ql_input_list = []
    play_area_list = []

    play_area = list(range(1, 10))
    #show_play(play_area)
    inputter_count = first_inputter
    end_flg = 0
    ql_flg = 0
    reward = 0
    while True:
        # Q学習退避用
        play_area_tmp = play_area.copy()
        play_area_list.append(play_area_tmp)
        # Q学習実行フラグ
        ql_flg = 0
        # AI(Q学習)の手番
        if (inputter_count % 2) == 0:
            # QL AI入力
            play_area, ql_ai_input = get_ai_input(play_area, 
                                                  first_inputter,
                                                  mode=1, 
                                                  q_table=q_table, 
                                                  epsilon=epsilon)
            winner, end_flg = judge(play_area, inputter2)
            # Q学習退避用
            ql_input_list.append(ql_ai_input)            
            # 勝利した場合
            if winner == inputter2:
                reward = 1
                ql_flg = 1
            play_area_before = play_area_list[-1]
            ql_ai_input_before = ql_input_list[-1]
        # AI(ランダム)の手番
        elif (inputter_count % 2) == 1:
            play_area, random_ai_input = get_ai_input(play_area, 
                                                      first_inputter+1, 
                                                      mode=0)
            winner, end_flg = judge(play_area, inputter1)
            # AI(ランダム)が先手の場合の初手以外は学習
            if inputter_count != 1:
                ql_flg = 1
        # Q学習実行
        if ql_flg == 1:
            ql_ai_input_before = ql_input_list[-1]
            q_table = q_learning(play_area_before, ql_ai_input_before,
                                 reward, play_area, q_table, end_flg, params)
        if end_flg:
            break
        inputter_count += 1
        
    # print('{} win!!!'.format(winner))
    return winner, q_table


def main() -> None:
    """三目並べの学習スクリプト
    """
    # 初期化されたQテーブルを作成
    q_table = make_q_table()
    
    # コンフィグファイルの読み込み
    cfg = configparser.ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    hp = cfg["TRAINING"]
    
    # ハイパーパラメータの設定
    eta = float(hp["eta"]) # 学習率
    gamma = float(hp["gamma"]) # 時間割引率
    initial_epsilon = float(hp["initial_epsilon"]) # ε-greedy法の初期値
    
    # 学習回数の設定
    episode = int(hp["episode"])
    
    # ランダム vs QL(学習) で学習を実行
    winner_list = []
    for i in tqdm(range(episode), desc="train"):
        epsilon = initial_epsilon * (episode-i) / episode
        winner, _ = randomAI_vs_QLAI(1, q_table, params=(gamma, eta), epsilon=epsilon)
        winner_list.append(winner)
        
    print('勝ち回数')
    print('Random AI:{}'.format(winner_list.count('Random AI')))
    print('QL AI    :{}'.format(winner_list.count('QL AI')))
    print('NOBODY   :{}'.format(winner_list.count('NOBODY')))
    print('QLの勝率 :{}'.format(winner_list.count('QL AI') / len(winner_list)))
    
    # ログの出力
    log_dir_path = Path(f"./logs/train_{episode}")
    log_dir_path.mkdir(parents=True, exist_ok=True)
    
    # 「勝ち回数」の記録をテキストに保存
    with open(log_dir_path.joinpath("winner_log.txt"), mode='w', encoding="utf-8") as f:
        f.write('Random AI:{}\n'.format(winner_list.count('Random AI')))
        f.write('QL AI    :{}\n'.format(winner_list.count('QL AI')))
        f.write('NOBODY   :{}\n'.format(winner_list.count('NOBODY')))
        f.write('QLの勝率 :{}\n'.format(winner_list.count('QL AI') / len(winner_list)))
        
    # 100戦ごとの勝率を計算しグラフにプロット
    win_rate_per_100 = [winner_list[i*100:(i+1)*100].count('QL AI') / 100
                        for i in range((episode//100)-1)]
    plt.plot(win_rate_per_100)
    plt.savefig(log_dir_path.joinpath("win_rate_per_100.png"))
    
    # 学習済みのQテーブルを保存
    weight_dir = Path("./weights")
    weight_dir.mkdir(exist_ok=True)
    df = pd.DataFrame(q_table)
    df.to_csv(weight_dir.joinpath(f"weight_{episode}.csv"), index=False, header=False)
    

if __name__ == "__main__":
    main()
