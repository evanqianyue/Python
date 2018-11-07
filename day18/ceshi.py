# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 @ Author     ：Evan
 @ Date       ：2018/11/6 15:02
 @ Version    : 1.0
 @ Description：
 @ Modified By：
"""

import re

str='''<div class="content">
<span>


刚发生的真事  不黑 不编<br/>我们公司每周一到六上班 只有礼拜天休息  早上10点上班 今天本来是要上班的   早上我还没醒呢  有同事回宿舍告诉我  今天停电不上班了   明天上班   一下我的瞌睡就醒了    发现手机没电了   去办公室拿了充电器就回来了   但是办公室人还有好多   回来有人告诉我  没通知今天不上班     你们觉得我是睡呢  还是去上班去   好纠结

</span>'''

content = re.findall(r'<div class="content">\n<span>(.*?)</span>', str, re.S)
print(content)