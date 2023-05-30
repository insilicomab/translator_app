import tkinter
from tkinter import filedialog, ttk

from googletrans import Translator


# 翻訳関数の作成
def convert():
    languages = {
        "日本語": "ja",
        "英語": "en",
        "中国語": "zh-ch",
        "フランス語": "fr",
        "ドイツ語": "de",
        "ヒンディー語": "hi",
    }

    before_text = input_box.get("1.0", "end-1c")
    before_language = input_pulldown.get()
    after_language = output_pulldown.get()
    print(f"翻訳する文章: {before_text}")
    print(f"翻訳する言語: {before_language}")
    print(f"翻訳後の言語: {after_language}")

    after_text = translator.translate(
        before_text, src=languages[before_language], dest=languages[after_language]
    )
    output_box.insert("1.0", after_text.text)


def save():
    file_name = filedialog.asksaveasfilename(
        title="名前をつけて保存",
        filetypes=[("Text", ".txt"), ("PNG", ".png")],
        initialdir="./",
        defaultextension=".txt",
    )
    with open(file_name, "w") as f:
        f.write(output_box.get("1.0", "end-1c"))


if __name__ == "__main__":
    # 翻訳用のインスタンスを作成
    translator = Translator()

    # ウィンドウの作成
    root = tkinter.Tk()
    root.title("翻訳アプリ")
    root.iconbitmap("translator.ico")
    root.geometry("655x480")
    root.resizable(False, False)

    # 色&フォントの設定
    normal_font = ("Arial", 10)
    bold_font = ("Arial", 10, "bold")
    bg_color = "#87CEFA"
    button_color = "#4682B4"
    root.config(bg=bg_color)

    """
    プルダウンの作成
    """
    language_list = ["日本語", "英語", "中国語", "フランス語", "ドイツ語", "ヒンディー語"]

    input_pulldown = ttk.Combobox(
        root, values=language_list, font=normal_font, justify="center"
    )  # インプットプルダウン
    to_label = tkinter.Label(root, text="to", font=normal_font, bg=bg_color)  # 「to」ラベル
    output_pulldown = ttk.Combobox(
        root, values=language_list, font=normal_font, justify="center"
    )  # アウトプットプルダウン

    # 左：インプットプルダウン、中央：「to」、右：アウトプットプルダウン
    input_pulldown.grid(row=0, column=0, padx=10, pady=10)
    to_label.grid(row=0, column=1, padx=10, pady=10)
    output_pulldown.grid(row=0, column=2, padx=10, pady=10)

    input_pulldown.set("日本語")  # インプットプルダウンの初期値
    output_pulldown.set("英語")  # アウトプットプルダウンの初期値

    """
    入力＆出力欄の作成
    """
    input_box = tkinter.Text(root, font=normal_font, width=40, height=20, borderwidth=3)
    equal_sign = tkinter.Label(root, text="=", font=normal_font, bg=bg_color)
    output_box = tkinter.Text(
        root, font=normal_font, width=40, height=20, borderwidth=3
    )

    # 左：入力欄、中央：「=」、右：出力欄
    input_box.grid(row=1, column=0, padx=10, pady=10)
    equal_sign.grid(row=1, column=1)
    output_box.grid(row=1, column=2, padx=10, pady=10)

    input_box.insert("1.0", "翻訳したい文章を入力")  # 1.0: 1行目の0文字目から

    """
    ボタンの作成
    """
    convert_button = tkinter.Button(
        root, text="翻訳", font=bold_font, fg="white", bg=button_color, command=convert
    )
    save_button = tkinter.Button(
        root,
        text="保存",
        font=bold_font,
        fg="white",
        bg=button_color,  # command=save
    )

    convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)
    save_button.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10), ipadx=50)

    # ウィンドウのループ処理
    root.mainloop()
