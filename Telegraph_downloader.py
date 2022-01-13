import os
import time
import requests
from tkinter import *
from tkinter import messagebox
from threading import Thread
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master=master
        self.createWidget()
        self.grid()
    
    def createWidget(self):
        self.download_label = Label(self, text="Url", height=1, takefocus=True).grid(row=0, column=0)
        self.url = Text(self, width=50, height=25, relief=SOLID, borderwidth=1)
        self.url.grid(row=1, column=0, rowspan=8)    # line 1-8

        self.log_label = Label(self, text="Log")
        self.log_label.grid(row=9, column=0)
        self.log = Text(self, width=90, height=18, relief=SOLID, borderwidth=1)
        self.log.grid(row=10, column=0, columnspan=2)
        notice = '''Telegraph下载器 v0.5 alpha
Author: xzajyjs
e-mail: xuziang16@gmail.com
个人主页: https://xzajyjs.cn

使用说明:
Url栏支持同时输入多个url, url之间请用换行符隔开;
Path栏仅支持输入单行路径，建议输入绝对路径;
输入的路径必须已经存在\n\n\n
'''
        self.log.insert(0.0, chars=notice)

        self.save_path_label = Label(self, text="Path", height=1).grid(row=0, column=1)
        self.save_path = Text(self, width=50,height=25, relief=SOLID, borderwidth=1)
        self.save_path.grid(row=1, column=1, rowspan=8)

        self.run = Button(self, text="Run!",width=6, bg="gray", command=self.thread)
        self.run.grid(row=9, column=1)
    def thread(self):
        t1 = Thread(target=self.get_info, daemon=True)
        t1.start()

    def get_info(self):
        try:
            start_time = time.time()
            path = self.save_path.get(0.0, END).strip('\n')
            print(f"path={path}")
            url_list = []
            url_list = self.url.get(0.0, END).split('\n')
            url_list = list(filter(None, url_list))

            print(f"url_list={url_list}")
            if path[-1:] != '/':
                path = path + "/"
            for url in url_list:
                pic_list = []
                self.log.insert(END, chars=f"开始处理 {url}\n")
                self.log.see(END)

                web = Chrome()
                web.get(url)
                title = web.title   # windows要切割 
                print(f"title={title}")
                os.mkdir(path=path+title)
                self.new_path = path+title+"/"
                

                self.log.insert(END, chars=f"图片会保存到 {self.new_path}\n")
                self.log.see(END)

                figure_list = web.find_elements(By.XPATH, '//*[@id="_tl_editor"]/div[1]/figure')

                for figure in figure_list:
                    src = figure.find_element(By.TAG_NAME, "img").get_attribute("src")
                    pic_list.append(src)

                web.close()
                with ThreadPoolExecutor(20) as t:
                    for each_pic_url in pic_list:
                        file_name = each_pic_url.rsplit("/",1)[1]
                        file_save_path = self.new_path+file_name
                        t.submit(self.download, each_pic_url=each_pic_url, save_path=file_save_path, pic_list=pic_list)
            end_time = time.time()
            messagebox.showinfo(title='完毕', message='所有图片下载完毕')
            self.log.insert(END, chars=f'共处理{len(url_list)}条数据，耗时{str(end_time-start_time)[:6]}s')

        except:
            messagebox.showerror(title='Error', message='发生意外错误')

    def download(self, each_pic_url, save_path, pic_list):
        with open(save_path,"wb") as f:
            f.write(requests.get(each_pic_url).content)
        self.log.insert(END, chars=f"{(self.new_path.rsplit('/',2)[1])[:15]}... => 进度:({pic_list.index(each_pic_url)+1}/{len(pic_list)})\n")
        self.log.see(END)
        

if __name__=="__main__":
    root = Tk()
    root.geometry('722x648+450+100')
    root.title('Telegraph图册下载器v0.5 --by xzajyjs')
    Application(master=root)
    root.mainloop()
