import tkinter as tk
from tkinter import ttk

def calc(weight, height):
    return weight / (height**2)

def check(bmi):
    if bmi < 18.5: return '低体重'
    elif bmi < 25.0: return '普通体重'
    elif bmi < 30.0: return '肥満度1'
    elif bmi < 35.0: return '肥満度2'
    elif bmi < 40.0: return '肥満度3'
    else: return '肥満度4'

def judgement():
    try:
        w = float(weight.get())
        h = float(height.get()) / 100
        label_result['text'] = check(calc(w, h))
    except ValueError:
        label_result['text'] = "数字を入力してください"

root = tk.Tk()
root.title('BMI App')
root.geometry('300x180')
root.resizable(False, False)

# ttkスタイルの設定（シンプルでモダンに）
style = ttk.Style(root)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=6)

# ラベルとエントリー
ttk.Label(root, text='体重 (kg)').grid(column=0, row=0, padx=10, pady=10, sticky='E')
weight = ttk.Entry(root, width=10)
weight.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text='身長 (cm)').grid(column=0, row=1, padx=10, pady=10, sticky='E')
height = ttk.Entry(root, width=10)
height.grid(column=1, row=1, padx=10, pady=10)

# 判定ボタン
ttk.Button(root, text='BMI判定', command=judgement).grid(column=0, row=2, columnspan=2, pady=10)

# 結果表示ラベル
label_result = ttk.Label(root, text='体重と身長を入力してください。', foreground='blue')
label_result.grid(column=0, row=3, columnspan=2, pady=10)

root.mainloop()
