# -*- coding: UTF-8 -*- 
from http.server import SimpleHTTPRequestHandler
import socket, os, socketserver
from pyautogui import hotkey
from base64 import b64decode
from urllib.parse import urlparse,unquote
import json

PORT = 8002

def ip_address_helper():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        return "IP Error!"
# def get_cmd_list():
#     file=open('test.json','r',encoding='utf-8')
#     dic=json.load(file)
#     file.close()
#     newDict = {k.upper():v for k,v in dic.items()}  #Convert dictionary  keys to uppercase
#     return newDict
# CMDList=get_cmd_list()

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = unquote(self.rfile.read(content_length)).strip()
        post_data = post_data.replace("。","")
        print(unquote(post_data))
        keys = [key.split('=')[1] for key in post_data.split('&')]
        if self.path in['/', '/index.html']:
            if "OpenURL" in keys[0]:
                WebUrl=keys[1].replace("%3A%2F%2F","://")
                WebUrl=WebUrl.replace("%2F","/")
                os.startfile(WebUrl)
            elif "JsonURL" in keys[0]:
                os.startfile(keys[1])
            elif "SendKeys" in keys[0]:
                CMDContent=unquote(keys[1])
                KeySeq=CMDContent.split('||')  
                for iKey in KeySeq:
                    keys = iKey.lower().split('+') #in the format of list['ctrl','w']
                    hotkey(*keys)  # convert list into string sequence
            elif "OSCMD" in keys[0]:
                os.startfile(keys[1])
            else:
                print(post_data + "Command not defined")

        self.do_GET()

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
        # get_cmd_list()

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
