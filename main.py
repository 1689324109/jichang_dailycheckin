# coding=utf-8
import requests, json, re, os

session = requests.session()
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')
# email = "1689324109@qq.com"
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')
# passwd = "12345678."
# server酱
SCKEY = os.environ.get('SCKEY')
# SCKEY = "1"
# PUSHPLUS
Token = os.environ.get('TOKEN')
# Token = "3a2edd53a98b4c8bb6ed8165af9008b0"
# Token = "1"
def push(content):
    if SCKEY != '1':
        url = "https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(SCKEY, 'ikuuu签到', content)
        requests.post(url)
        print('推送完成')
    elif Token != '1':
        headers = {'Content-Type': 'application/json'}
        json = {"token": Token, 'title': 'ikuuu签到', 'content': content, "template": "json"}
        resp = requests.post('http://www.pushplus.plus/send', json=json, headers=headers).json()
        print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')
    else:
        print('未使用消息推送推送！')

# 会不定时更新域名，记得Sync fork

login_url = 'https://ikuuu.pw/auth/login'
check_url = 'https://ikuuu.pw/user/checkin'
info_url = 'https://ikuuu.pw/user/profile'

header = {
        'origin': 'https://ikuuu.me',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 获取账号名称
    info_html = session.get(url=info_url,headers=header).text
#     info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', info_html, re.S))
#     print(info)
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
    # 进行推送
    push(content)
except:
    content = '签到失败'
    print(content)
    push(content)
