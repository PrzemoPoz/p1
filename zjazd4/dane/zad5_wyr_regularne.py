import re


with open("input.txt") as f:
    text=f.read()
    pattern_kod = re.compile("\d{2}-\d{3}")
    print(f'''Kody: ({len(pattern_kod.findall(text))}) {pattern_kod.findall(text)}''')

    pattern_mejl = re.compile("[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    print(f'''E-maile: ({len(pattern_mejl.findall(text))}){pattern_mejl.findall(text)}''')

    pattern_data = re.compile("\d{2} [A-Za-z]{3} \d{4}")
    print(f'''Daty: ({len(pattern_data.findall(text))}) {pattern_data.findall(text)}''')

    #\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b
