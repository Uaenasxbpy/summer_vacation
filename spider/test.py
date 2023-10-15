import re
def remove_non_chinese_characters(text):
    str = re.sub('[^\u4e00-\u9fa5]+', '', text)
    return str
# 示例字符串
example_text = "Hello! 你好！ This is a test string with Chinese characters. 这是一个含有中文的测试字符串。"
# 保留汉字并去除其他字符
result = remove_non_chinese_characters(example_text)
# 输出结果
print(result)