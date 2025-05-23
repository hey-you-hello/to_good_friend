from os.path import isdir
from tqdm import tqdm
import zipfile
import os

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
        print(f" 解壓縮完成：{zip_path} → {extract_to}")
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
import requests
import os
print('start load.....')
basic_url='https://brawlstar-theta.vercel.app'
if not os.path.isdir('我存的東西別碰!'):
  os.mkdir('我存的東西別碰!')
if not os.path.isfile('我存的東西別碰!/main_exe_version.txt'):
  with open('我存的東西別碰!/main_exe_version.txt','w') as f:
    f.write('0')
with open('我存的東西別碰!/main_exe_version.txt','r') as f:
  version = f.read()
  
  lsest_version=requests.get('https://brawlstar-theta.vercel.app/main_exe_version.txt').text
  if version!=lsest_version or not os.path.isfile('我存的東西別碰!/main.exe'):
    with open('我存的東西別碰!/main_exe_version.txt','w') as f:
      download(basic_url+'/main.exe','我存的東西別碰!/main.exe')
      download(basic_url+'/_internal.zip','我存的東西別碰!/_internal.zip')
      unzip_file('我存的東西別碰!/_internal.zip','我存的東西別碰!')
      os.remove('我存的東西別碰!\_internal.zip')
      f.write(lsest_version)

    
print('load sucess:D')
os.system('我存的東西別碰!\main.exe k ')

