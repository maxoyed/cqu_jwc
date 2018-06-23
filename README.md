# cqu_jwc
重庆大学教务处登录模块
1. 自动登录教务网
2. 封装了带session的GET和POST请求，方便开发者使用
3. 所有请求均加入了失败重试机制
4. 获取当前登录用户姓名

## 安装

```commandline
pip install cqujwc
```

或者
```commandline

sudo pip install cqujwc
```

## 使用

```python
from cqujwc import Student
student = Student('学号', '密码')
```

## 说明

实例化`Student`对象时可选参数`server`(默认为0):

```text
0: jxgl.cqu.edu.cn
1: 202.202.1.41
2: 202.202.1.176:8080
3: 222.198.128.126
```
## 利用当前session发起GET和POST请求

### GET
```python
student.get(url, params=None, headers=None)
```

参数说明

参数名 | 说明 |备注
:---:|:---:|:---:
url | GET请求去掉server字段的url | 例如，若要请求`http://202.202.1.176:8080/MAINFRM.aspx`，只需在实例化student对象时将`server`设置为2，然后调用`student.get('/MAINFRM.aspx')`即可
params | GET请求参数 | 和requests.get()的params参数一致
headers | 请求头 | 默认只有UA

### POST
```python
student.post(url, data=None, headers=None)
```

参数说明

参数名 | 说明 |备注
:---:|:---:|:---:
url | POST请求去掉server字段的url | 同上
data | POST请求参数 | 和requests.post()的data参数一致
headers | 请求头 | 默认只有UA

## 获取当前登录用户姓名

```python
student.get_current_name()
```

## 开发计划
[ - ] session管理

[ - ] 四台服务器同时登录

[ - ] 自动获取并设置代理服务器 
