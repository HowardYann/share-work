import mechanize
from bs4 import BeautifulSoup

# 创建浏览器对象
br = mechanize.Browser()
br.set_handle_robots(False)  # 禁用 robots.txt

# 打开表单页面
response = br.open("https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__QGA__xUN1c1WkpKNkYwQ1ZZMDlTRkVCR1VaUFY5QS4u")

# 解析 HTML
soup = BeautifulSoup(response.read(), 'html.parser')

# 找到包含表单内容的 div
div = soup.find("div", {"data-automation-id": "questionItem"})

# 获取表单字段
fields = div.find_all("input", {"type": "text"})  # 找到文本输入框

# 填写表单
data = {
    "email": "your-email@example.com",
    "date": "2024/01/01",
    "text": "Sample Answer Text",
    "dropdown_name": "Option Text",
    "radio_button_name": "radio_value",
    "score_field_name": "3",
}

# 填写字段
for input_field in fields:
    name = input_field.get("name")
    if name in data:
        input_field["value"] = data[name]  # 填充数据

# 提交表单
br.form = div.find("form")  # 选择正确的表单
response = br.submit()

if response.code == 200:
    print("Form submitted successfully.")
else:
    print(f"Failed to submit form. Status code: {response.code}")
