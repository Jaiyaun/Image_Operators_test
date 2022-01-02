# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:watermark.py
@time:2021/11/17
"""

import matplotlib.pyplot as plt

def savefig(plt, filename, watermark_text):
    fig = plt.gcf()
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    fig.text(0.9, 0.05, watermark_text,
             fontsize=40,
             rotation=45,
             color='blue',
             ha='right',
             va='bottom',
             alpha=0.2)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.margins(0, 0)
    fig.savefig(filename, format='png', transparent=True, pad_inches=0)

def addwatermark(plt, watermar_text, x=0.9, y=0.05, angle=45):
    fig = plt.gcf()
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    fig.text(x, y, watermar_text,
             fontsize=40,
             rotation=angle,
             color='gold',
             ha='right',
             va='bottom',
             alpha=0.5
             )
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())