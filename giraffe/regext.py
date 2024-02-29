import re

target_str = "My roll number is 25"
res = re.findall(r"\d", target_str)
print(res)

target_string = r"example task to search"
# regex pattern
pattern = "to search"
# \n and \t has a special meaning in Python
# Python will treat them differently
res = re.search(pattern, target_string)
print(res.group())

str_pattern = r"\w"
pattern = re.compile(str_pattern)

res = pattern.match(target_string)
print(res.group())

res = re.search(r"\d", target_str)
print(res.group())

res = re.findall(r"\d", target_str)
print(res)

res = re.split(r"\s", target_str)
print(res)

res = re.sub(r"\s", "-", target_string)
print(res)