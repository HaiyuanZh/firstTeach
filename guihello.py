#!/usr/bin/env python3
# encoding: utf-8
"""
@author: 润玉
@time: 2020/10/7 12:15 PM
@desc:
"""

import tkinter as tk
import tkinter.font as tkFont

if __name__ == '__main__':
    window1 = tk.Tk()

    window1.title('你打我啊')
    window1.geometry('600x400+500+100')

    tk.Label(window1, text='这是一个标签', font=tkFont.Font(size=50)).pack()

    tk.Button(window1, text='点击我', font=tkFont.Font(size=30), command=window1.destroy).pack()

    tk.mainloop()

