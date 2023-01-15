# WebRemoter4PC
Web Remotor For PC: control your PC by any web browser on your mobile phone, pad, etc.  
You can controll your PC (The PC is called ServerPC) by any terminal (these terminals are named ClientTerminal), like mobile phone, pad, or other PC, only a browser is needed.  
The ClientTerminal shall be in the same local network with the ServerPC.  
Of course, you can controll ServerPC by WAN by setting DDNS, but that is another story.  
Inspired by [**ZoomRemote**](https://github.com/khbroadcasting/ZoomRemote/)  

# Files
- **webserver-cli**.py: main file to start http server
- **GenHTML.py**: generate index.html file from Config.json automatically
- **Config.json**:  setting user commands
- **others**
- HTML_Head.txt: html snippet for generating head of index.html
- HTML-Inputbox.txt: html snippet for generating inputbox of index.html
# Usage
1. config your commands in the Config.json file
2. run GenHTML.py to generate index.html
3. run webserver-cli on your PC to start http server. 
4. then visit http://127.0.0.1 in the browser on your ServerPC
5. or visit http://your_ServerPC_ip:8002/ with your mobile phone or tablet

# How to set the commands in Config.json
one piece of command looks like this:
``` json
    {
        "id": "1",
        "CmdType": "JsonURL",
        "CMDUniqueName": "CCTV1",
        "CMDNickName": {},
        "CMDContent": "https://tv.cctv.com/live/cctv1",
        "ShowInHomePage":"True",
        "ShowName":"CCTV1 综合",
        "CMDTextIcon":"&#x270B"
    }
```
* id: index to indentify the command. Any unique number is OK.
* CmdType: now supports three types
  * JsonURL: http address
  * SendKeys: any hotkeys. 
    * keys are seperated by SPACE, like "ctrl w"
    * multiple hotkeys are seperated by double |, e.g. " "ctrl w || ctrl shift t"
    * your can find these valid key code: https://pyautogui.readthedocs.io/en/latest/keyboard.html
  * OSCMD: the command that can be excuted by cmd.exe or win+r 
* CMDUniqueName: the unique string to indentify the command
* CMDContent: the command will be excuted
* ShowInHomePage: whether this command will be shown in index.html or not
* ShowName: if the command is shown, the text will be presented
* CMDTextIcon: some ascii to be shown as icon for this command
==========
# Voice control
using your phone or pad's voice IME to input the command into the command-box and sumbit. Bingo!
**Python HTTP Server to Remote Control Zoom Videoconferencing**

# Features
* Voice controll is supported. HAH
* Plenty of terminals are supported, all needed is one browser
* One-click, portable.
* Easy to understand help screen for non-technical users.
* Completely customizable.
  * Appearance
  * Functions
  * You can use multiple instance for different controlling purpose

### Screenshots
**Mobile**  
<img src="https://github.com/valuex/WebRemoter4PC/blob/main/Mobile.png" height="100">  
**PC**  
<img src="https://github.com/valuex/WebRemoter4PC/blob/main/PC.png" height="100">



#### Dependencies

1. Python 3
2. pyautogui - get it with `pip install pyautogui`
3. pyautogui depends on `python3-tk` and `python3-dev` - install with apt oryum.
4. `urllib.parse` import urlparse,unquote`
5. `json`
#### Installation

Download  the whole project as a ZiP file from the source above.



Contributing
------------

Contributions are most welcome!  In particular, pull requests:
* Improving HTML/CSS Layout for a more intuitive responsive grid would be appreciated.  I would like to be able to have multiple buttons side-by-side on a row on mobile devices, to then add navigation functionality.
* Refactoring as a module to remove the embedded images and html from the main `webserver.py` to an imported library.
* That allow the PORT to be specified as a command-line argument.
* That provide a better command-line interface and module interface.
* Anything else you can think of.
