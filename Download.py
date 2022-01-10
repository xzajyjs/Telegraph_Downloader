from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import time

path = input("Input save path: ")
url_list = []

def download(url,new_path,index,size):
    print(f"{(new_path.rsplit('/',2)[1])[:15]}... => Process:({index+1}/{size})")
    file_name = url.rsplit("/",1)[1]
    with open(new_path+file_name,"wb") as f:
        f.write(requests.get(url).content)
        

def main(url):
    global path

    pic_list = []
    if path[-1:] != '/':
        path = path + "/"
    print(f"Starting to process {url}")

    web = Chrome()
    web.get(url)
    title = web.title
    os.mkdir(path=path+title)
    new_path = path+title+"/"
    print(f"Pics will save to {new_path}")

    figure_list = web.find_elements(By.XPATH, '//*[@id="_tl_editor"]/div[1]/figure')
    for figure in figure_list:
        src = figure.find_element(By.TAG_NAME, "img").get_attribute("src")
        pic_list.append(src)
    web.close()

    with ThreadPoolExecutor(20) as t:
        for each_pic_url in pic_list:
            t.submit(download,url=each_pic_url,new_path=new_path,index=pic_list.index(each_pic_url),size=len(pic_list))
            

if __name__=="__main__":
    read_file = input("Input url '.txt' Absolute path: ")
    start_time = time.time()
    with open(read_file,"r") as f:
        for line in f:
            url_list.append(line.strip('\n'))
    with ThreadPoolExecutor(5) as t:
        for each_url in url_list:
            t.submit(main,url=each_url)

    print(f"Total dealt with {len(url_list)} resources, consuming {time.time()-start_time}s")