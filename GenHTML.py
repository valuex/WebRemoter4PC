# -*- coding: UTF-8 -*- 
# <form action="/" method="post">
#   <input type="hidden" name="CmdType" value="SendKeys">
#   <input type="hidden" name="InCMD" value="ReOpen">
#   <input type="submit" value="&#x270B ReOpen" class="button">
#   </form>

import json
def get_cmd_list():
    file=open('Config.json','r',encoding='utf-8')
    dic=json.load(file)
    file.close()
    return dic
CMDList=get_cmd_list()
def gen_part_html(filename):
    file=open(filename,'r',encoding='utf-8')
    contents = file.read()
    file.close()
    return contents

def gen_cmd_html():
    CMD_HTML=""
    for iDic in  CMDList:
        print (iDic['ShowName']) 
        CmdType=iDic['CmdType']
        CMDContent=iDic['CMDContent']
        ShowName=iDic['CMDTextIcon']+" "+iDic['ShowName']
        
        iCMD=f"""
            <form action="/" method="post">
            <input type="hidden" name="CmdType" value="{CmdType}">
            <input type="hidden" name="InCMD" value="{CMDContent}">
            <input type="submit" value="{ShowName}" class="button">
            </form>
        """
        CMD_HTML=CMD_HTML+iCMD
    CMD_HTML=f"""
        <div class="container">
        {CMD_HTML}
        </div>
    """    # print(CMD_HTML)
    return CMD_HTML
def main():
    head_html=gen_part_html("HTML_Head.txt")
    inputbox_html=gen_part_html("HTML-Inputbox.txt")
    # print(inputbox_html)
    CMD_HTML=gen_cmd_html()
    All_HTML=f"""
    <html>
    {head_html}
    <body>
    <div>
    {inputbox_html}
    {CMD_HTML}
    </div>
    </body>
    </html>
    """
    with open('Index.html', 'w',encoding='utf8') as f:
        f.write(All_HTML)
        f.close()
if __name__ == '__main__':
    main()
