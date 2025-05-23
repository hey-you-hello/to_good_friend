
import requests
import argparse

import os
from tqdm import tqdm
import zipfile
import logging


FORMAT = ' %(asctime)s %(filename)s %(levelname)s:%(message)s'
i=1
logging.basicConfig(level=logging.INFO, format=FORMAT)
kkkkkkkk=logging.info
def l(*args):
    global i
    kkkkkkkk(f'{i} {args[0]}')
    i+=1
logging.info=l
p = argparse.ArgumentParser()
p.add_argument('s')  
args = p.parse_args()
logging.info('確認資源包完整?')
def unzip_file(zip_path, extract_to='.'):
    """
    解壓縮 zip 檔案到指定資料夾。
    
    :param zip_path: zip 檔案的路徑
    :param extract_to: 解壓縮後要放的資料夾，預設是目前目錄
    """
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"{zip_path} 不是合法的 zip 檔案")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        logging.info(f" 解壓縮完成：{zip_path} → {extract_to}")
def download(url,local_filename):
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    total = int(r.headers.get('content-length', 0))
    with open(local_filename, 'wb') as f, tqdm(
        desc="載入",
        total=total,
        unit='B',
        unit_scale=True,
        unit_divisor=1024
    ) as bar:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
if not os.path.isdir('我存的東西別碰!/model'):
    logging.info('沒有??')
    download('https://brawlstar-theta.vercel.app/formyfriend/model.zip','我存的東西別碰!\model.zip')
    unzip_file('我存的東西別碰!/model.zip','我存的東西別碰!')
else:
    logging.info('完整')
logging.info('確認有無擴充資料')
dataa = requests.get('https://brawlstar-theta.vercel.app/formyfriend/擴充資料').text.split('\n')
data=[]
for k in dataa:
    if k!='':
        data.append(k)

def cbool(x):
    return bool(int(x))
logging.info('確認擴充資源紀錄檔案存在')
if not os.path.isfile('我存的東西別碰!/version.txt'):
    with open('我存的東西別碰!/version.txt', 'w', encoding='utf-8') as f:
        logging.info('不存在??')
        f.write('0\n0')
else:
    logging.info('存在')
with open('我存的東西別碰!/version.txt', 'r', encoding='utf-8') as f:
    
    version = f.readlines()
    logging.info(f'紀錄擴充版本為{[n.strip() for n in version]}')
path = [n.split()[0] for n in data ] 
logging.info(f'目前擴充版本為{[n.split()[2].strip() for n in data]}')
need_update=[n.split()[2]!=v.strip() for n,v in zip(data,version) ] 

if len(data)==0 or (all([os.path.isfile(n) for n in path]) and not any(need_update)):
    logging.info('沒有新的擴充QAQ')
else:
    logging.info('有擴充耶:D')
    for i,n in enumerate(data):
        if cbool(n.split()[2]):
            logging.info(f'下載擴充包...{i}')
            download(n.split()[1],n.split()[0])
    
    with open('我存的東西別碰!/version.txt', 'w', encoding='utf-8') as f:
        logging.info('寫入新版!')
        for n in data :
            f.write( n.split()[2]+'\n')

logging.info('完成，主程式開始')
SAVE_FILE = "我存的東西別碰!\save.pkl"
def 介面():
    print('現在我有兩個功能! 1.長文閱讀 2.給詹晉瑜的留言!\n選一個吧!')
    process=int(input())
    os.system(f'我存的東西別碰!\{process}.exe 5')
if __name__=='__main__':
    
    介面()
    
   

    

