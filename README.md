# Telegraph_Downloader
Tkinter写的一个小工具，采用多线程技术用来批量下载`telegra.ph`上发布的各种图册。使用简单
![](https://serverless-page-bucket-lv779z7b-1307395653.cos-website.ap-shanghai.myqcloud.com/telegraph_download/Telegraph.png)

国内网络环境复杂,而`telegra.ph`又是需要魔法才能访问的,因此Mac平台需要开全局代理。但windows平台的所谓全局代理时没有用的，必须使用类似`natapp`等的流量转发工具才能正常运行。

---
## 使用方式
```
pip install -r requirements.txt
python Telegraph_downloader.py
```
> 由于Windows平台缩放、分辨率导致的窗口不一致问题，v0.5版本后将不再更新打包版本。  