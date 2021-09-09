# tkinterのインポート
import os
import tkinter as tk
import datetime

from pynput import keyboard
from PIL import ImageGrab
from tkinter import filedialog


# 保存するディレクトリを選択
def set_file():
    idir = 'C:\\'
    save_place = tk.filedialog.askdirectory(initialdir=idir)
    # 既存のパスを削除
    text_box.delete(0, tk.END)
    # パスをラベル中に表示
    text_box.insert(tk.END, save_place)

    # ステータスバーの更新
    statusbar["text"] = "Ready !"


# 実際にスクリーンショットを撮影する関数
def make_screenshot():
    # フルスクリーンの取得
    time = datetime.datetime.now()
    format_time = time.strftime('%Y_%m_%d_%H_%M_%S_%f')
    screenshot = ImageGrab.grab()
    # screenshot.save('test2.jpg')
    dir_path = text_box.get()
    file_path = os.path.join(dir_path, format_time + '.jpg')
    screenshot.save(file_path)

    # ステータスバーの更新
    statusbar["text"] = 'Success! ' + format_time + '.jpg'


def start_capture():
    # イベントの設定
    # Collect events until released
    with keyboard.Listener(
            on_press=press,
            on_release=release) as listener:
        listener.join()

    listener = keyboard.Listener(
        on_press=press,
        on_release=release)
    listener.start()


def press(key):
    # キーボード入力のイベント検知
    if key == keyboard.Key.print_screen:
        ex_run_func()


def release(key):
    if key == keyboard.Key.esc:  # escが押された場合
        return False


def ex_run_func(event):
    try:
        make_screenshot()
    except:
        # ステータスバーにエラーメッセージ
        statusbar["text"] = "Error!! ファイルを選択してください"


# GUI の作成
# ウインドウの作成
window = tk.Tk()
# ウインドウのサイズ設定
window.geometry("420x100")
# ウインドウタイトル
window.title("screenShot_application")
# # Runボタン設置
# run_button = tk.Button(window, text="Run", command=ex_run_func)
# run_button.place(x=160, y=40)
# Setボタン設置
set_button = tk.Button(window, text="Choose File", command=set_file)
set_button.place(x=300, y=7)

# テキストボックスの設置
text_box = tk.Entry(width=40)
text_box.place(x=10, y=10)

# ステータスバーの作成 bd=枠の太さ, relief=線の書式(SUNKEN:親要素よりも沈んで表示,RAISED: 親要素よりも盛り上がって表示), anchor= コンテンツの配置場所に余白があるばい右:E 左:Wのどちらによせるか
statusbar = tk.Label(window, text="No Data!!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)  # side=BOTTOMでウインドウの底、fill=Xだと(width)

# イベントの設定
window.bind("<KeyPress>", ex_run_func)

# ウインドウ状態の維持
window.mainloop()

# # イベントの定義
# # Collect events until released
# with keyboard.Listener(
#         on_press=press,
#         on_release=release) as listener:
#     listener.join()
#
# listener = keyboard.Listener(
#     on_press=press,
#     on_release=release)
# listener.start()
