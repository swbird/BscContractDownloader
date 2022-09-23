import json
import argparse
import requests
from web3.auto import w3
import os, sys


_API_KEY = "your bscscan api key"

def getInfo(address=''):
    address = w3.toChecksumAddress(address)
    api = f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={address}&apikey={_API_KEY}'
    resp = requests.get(api)
    if resp.status_code==200:
        print("Find Contract Success.")
    info = resp.json()['result'][0]
    # print(info)
    abi = info['ABI']
    SourceCode:str = info['SourceCode']
    SourceCode = SourceCode[1: len(SourceCode)-1]
    SourceCode = json.loads(SourceCode)
    sources: dict = SourceCode['sources']
    # print(sources)
    count = 0
    dirName = '' # 初始化dirName
    for name, content in sources.items():
        realName = name.split('/')[-1]
        print("find ", realName, '===> downloaded')
        if count == 0:
            dirName = os.getcwd()+'\\'+f"{realName.replace('.sol','')}-{address}-bsc"
            if os.path.exists(dirName):
                print(f"{dirName}-已存在-无需重新创建.")
            else:
                os.mkdir(dirName)
                os.mkdir(dirName+'\\abi')
                with open(dirName+f'\\abi\\abi.json', 'w', encoding='utf-8') as w:
                    w.write(json.dumps(json.loads(abi),ensure_ascii=False))
        with open(f"{dirName}\\{realName}", 'w', encoding='utf-8') as f:
            # print(content)
            f.write(content['content'])
        count += 1





if __name__=='__main__':
    sysArgs = sys.argv
    parser = argparse.ArgumentParser(description='bsc contract file downloader.')
    parser.add_argument('--address', type=str, default="0x0000000000000000000000000000000000000000", help='input bsc contract address')
    args = parser.parse_args()
    print(f"本次抓取的合约地址=>{args.__dict__['address']}")
    getInfo(args.__dict__['address'])
