"""
[难度: ⭐⭐⭐]
[所属知识点: POST 请求与 data]
[预计完成时间: 15 分钟]

题目描述:
    使用 requests.post() 向 http://httpbin.org/post
    发送表单数据 {"username": "test", "password": "123"},
    httpbin 会原样返回请求内容。从响应 JSON 中提取
    form 字段并打印,验证数据是否被正确提交。

示例:
    >>> data = {'username':'test','password':'123'}
    >>> resp = requests.post(url, data=data)
    >>> print(resp.json()['form'])
    {'username': 'test', 'password': '123'}
"""

# ======================
# 学员代码区(以 pass 作为占位符)
# ======================
import requests

url = 'http://httpbin.org/post'
# 要提交的表单数据
form_data = {
    'username': 'test',
    'password': '123'
}
response = requests.post(url, data=form_data)
# 从响应 JSON 中提取 form 字段
result = response.json()
print('form 字段内容:', result.get('form'))
print('状态码:', response.status_code)

# ======================
# 测试区(教师可复制到终端验证)
# ======================
if __name__ == '__main__':
    # 测试 1: form 字段包含提交的 username
    d = {'username': 'test', 'password': '123'}
    r = requests.post('http://httpbin.org/post', data=d)
    form = r.json().get('form', {})
    assert form.get('username') == 'test', \
        f"username 不匹配: {form}"
    assert form.get('password') == '123', \
        f"password 不匹配: {form}"
    print('测试 1 通过:form =', form)

    # 测试 2: 另一组数据也能正确回显
    d2 = {'username': 'alice', 'password': 'abc'}
    r2 = requests.post(
        'http://httpbin.org/post', data=d2
    )
    form2 = r2.json().get('form', {})
    assert form2 == d2, f"期望 {d2}, 实际 {form2}"
    print('测试 2 通过:form =', form2)
