
import argparse
import requests
import os 
import time
import jieba
import random
from rich.live import Live
from rich.text import Text
import pickle
SAVE_FILE = "我存的東西別碰!\save.pkl"
class Save:
    def __init__(self):
        self.view_count = 0      
        self.total_time = 0.0    
        self.last_seen = time.time()  
        self.章節=[]
        self.第一次看選單=True
p = argparse.ArgumentParser()
p.add_argument('s')  
args = p.parse_args()
start_time = time.time()

url = 'https://brawlstar-theta.vercel.app/formyfriend/'
response = requests.get(url + '想說的.txt')
li = response.text.strip().split('-')
charter = requests.get(url+'/分節').text.split()
symbols = '←↖↑↗→↘↓↙'
def type_line(line: str, symbols: str = symbols):
    typed = ''
    words = list(jieba.cut(line))
    with Live(refresh_per_second=10) as live:
        for i, word in enumerate(words):
            typed += word
            cursor = symbols[i % len(symbols)]

            text = Text()
            text.append(typed, style="bold cyan")
            if i + 1 != len(words):
                text.append(cursor, style="bold red")

            live.update(text)

            
            r = random.random()
            if r < 0.00001:
                time.sleep(5)
            elif r < 0.01:
                time.sleep(1.0)
            elif r < 0.05:
                time.sleep(0.5)
            else:
                time.sleep(random.uniform(0.05, 0.1))

if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, 'rb') as f:
        save = pickle.load(f)
else:
    save = Save()
if save.view_count %10 == 10:
    type_line(f'你已經看了這個動畫{save.view_count}次了呢…')
    type_line('有特別想看的嗎?')
    input('輸入:')
    type_line('這是不會被記錄的....應該?')
if save.total_time > 600:
    type_line('你已經在這上面浪費了超過10分鐘了!!!!')
if save.第一次看選單:
    type_line('嗨!你看很多次了嗎? 接下來可以快速跳過前面囉!')
    save.第一次看選單=False

while True:
    type_line('有這些章節喔')


    new=set(charter)-set(save.章節)
    for i,n in enumerate(charter):
        type_line(f'{i+1}.{"新! " if n in new else ""}{n}')
    type_line('輸入一個你想看的章節吧!輸入離開來結束!')
        
    try :
        
        i=input(':')
        if i=='離開' :
            break
        c=int(i)

        for n in li[c-1].split('\n'):
            type_line(n)
            
            
    except :
        print(f'輸入數字或者請在範圍內 1~{len(charter)}')
    save.view_count += 1
    used_time = time.time() - start_time
    save.total_time += used_time
    save.last_seen = time.time()
    save.章節=charter
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(save, f)
    type_line('to be continue→→→→→........')
    input()