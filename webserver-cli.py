# -*- coding: UTF-8 -*- 
from http.server import SimpleHTTPRequestHandler
import socket, os, socketserver
from pyautogui import hotkey
from base64 import b64decode
from urllib.parse import urlparse,unquote
import json

PORT = 8002
def get_cmd_list(filename):
    file=open(filename,'r',encoding='utf-8')
    dic=json.load(file)
    file.close()
    return dic
CMDList=get_cmd_list('Config.json')
EngineList=get_cmd_list('SearchEngine.json')

def default_search(SearchKw):
    DefaultEngine= EngineList["Default"] 
    SearchCMD=DefaultEngine.replace("{SearchKw}",SearchKw)
    os.startfile(SearchCMD)
def ip_address_helper():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        return "IP Error!"
class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = unquote(self.rfile.read(content_length)).strip()
        post_data = post_data.replace("。","")
        print(unquote(post_data))
        keys = [key.split('=')[1] for key in post_data.split('&')]
        CMDContent=''.join(keys[1])
        if self.path in['/', '/index.html']:
            if "JsonURL" in keys[0]:
                if "http" in CMDContent:
                    os.startfile(CMDContent)
                elif "搜索" in CMDContent:
                    self.SearchKeywords(CMDContent)
                else:
                    self.search_CDM("JsonURL", CMDContent)
            elif "SendKeys" in keys[0]:
                CMDContent=unquote(CMDContent)
                KeySeq=CMDContent.split('||')  
                for iKey in KeySeq:
                    keys = iKey.lower().split('+') #in the format of list['ctrl','w']
                    hotkey(*keys)  # convert list into string sequence
            elif "OSCMD" in keys[0]:
                try:
                    os.startfile(CMDContent)
                except:
                    self.search_CDM("OSCMD", CMDContent)
                else:
                    print("OSCMD" + CMDContent + "excuted")
            else:
                print(post_data + "Command not defined")

        self.do_GET()
    def search_CDM(self,InCMDType,keyword):
        CMDExcuted=0
        for iDic in  CMDList:
            CMDUniqueName=iDic['CMDUniqueName']
            CMDContent=iDic['CMDContent']
            CMDNickName=iDic['CMDNickName']  
            CmdType=iDic['CmdType']
            if keyword in CMDUniqueName and InCMDType in CmdType:
                os.startfile(CMDContent)
                CMDExcuted=1
                break
            elif any(keyword in s for s in CMDNickName) and InCMDType in CmdType:
                os.startfile(CMDContent)
                CMDExcuted=1
                break        
        if CMDExcuted==0:
            default_search(keyword)
            # os.startfile("https://www.google.com/search?q="+keyword)
    def do_GET(self):
        query = urlparse(self.path).query
        if query!="":
            key = unquote(query.split('=')[1])  # unquote, decode from url
            # print(key)

        for local_path in ['/', '/index.html', '/favicon.ico', '/ZoomRemoteDir']:
            if self.path == local_path:
                self.send_local(self.path)
                return
        super().do_GET()

    def SearchKeywords(self,keyword):
        SearchKwPos=keyword.find("搜索")
        DefaultEngine= EngineList["Default"] 

        if SearchKwPos==-1:
            SearchKw=keyword
            SearchCMD=DefaultEngine.replace("{SearchKw}",SearchKw)
            os.startfile(SearchCMD)
            return
        else:
            SearchKw=keyword[SearchKwPos+2:]

        FindEngine=0
        for EngineName,Engine in EngineList.items():
            KeyWd4Engine=EngineName+"搜索"
            KeyWd4Engine=KeyWd4Engine.lower()
            if KeyWd4Engine in keyword.lower():
                SearchCMD=Engine.replace("{SearchKw}",SearchKw)
                os.startfile(SearchCMD)
                FindEngine=1
                break
        if FindEngine==0:
                default_search(SearchKw)
                # SearchCMD=DefaultEngine.replace("{SearchKw}",SearchKw)
                # os.startfile(SearchCMD)

    def send_local(self, path):
        if path == '/favicon.png':
            if os.path.exists('favicon.png'):
                super().do_GET()
            else:
                print('No favicon.png in the folder')
        else:
            if os.path.exists('index.html'):
                super().do_GET()
            else:
                print('No index.html in the folder')

    def send_simple_response(self, content, ctype):
        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

def main():
    print(f"Starting HTTP server on {ip_address_helper()}:{PORT}...", end=' ')
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("Done!")
        httpd.serve_forever()

if __name__ == '__main__':
    main()
