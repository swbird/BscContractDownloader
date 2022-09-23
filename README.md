# BscContractDownloader
在bscscan一次性下载所有合约文件,一个个手动复制粘贴太麻烦了


# 编译成.exe文件然后将所在文件夹添加到环境变量里面
 

pyinstaller -F contractDownloader.py

 
 # 使用方法
 
 contractDownloader --address 0xTheContractAddressWhatUWantToDownload

# 效果图
![image](https://user-images.githubusercontent.com/43195509/192009808-a5d2233f-4af4-4b9e-93f6-ee6256c2c0d1.png)
