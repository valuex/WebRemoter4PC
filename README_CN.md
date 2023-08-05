# WebRemoter4PC
用于在局域网下遥控电脑，也可以实现**手机跨屏输入**
手机跨屏输入:以借助小艺等手机语音输入法进行跨屏输入，不依赖手机上安装的输入法，任何输入法都可以。
# 使用方法
1. 在`Config.json` 配置用户命令
2. 运行 `GenHTML.py` 生成`index.html`
3. 运行` webserver-cli.py` 启动HTTP服务
4. 用手机或平板访问`http://your_ServerPC_ip:8002/` 
# 目录下文件说明
- webserver-cli.py: 主程序，启动HTTP服务
- GenHTML.py: 从`Config.json`生成 `index.html` 文件
- Config.json: 配置用户命令
- SearchEngine.json: 配置用户搜索引擎
others
- HTML_Head.txt: html snippet for generating head of index.html
- HTML-Inputbox.txt: html snippet for generating inputbox of index.html
# `Config.json`中配置命令
请参考英文说明
