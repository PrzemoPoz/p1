import re

pattern = re.compile("\d{3}-\d{3}-\d{3}")

text = "122-222-223-231-232-132"
print(pattern.findall(text))
