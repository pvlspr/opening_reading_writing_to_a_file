list_txt = ['1.txt', '2.txt', '3.txt']


count_str = {}
text_read = {}
result = []


for txt in list_txt:
    with open(txt, encoding='utf8') as file:
        count_str[txt] = file.read().count('\n') + 1

for txt in count_str:
    with open(txt, encoding='utf8') as f:
        text_read[txt] = f.read()

sort_count_str = {}
sort_key_count_str = sorted(count_str, key=count_str.get)

for i in sort_key_count_str:
    sort_count_str[i] = count_str[i]

for num_text in sort_count_str.keys():
    result.append(
        f'{num_text}\n{sort_count_str[num_text]}\n\
                  {text_read[num_text]}'
                  )

with open('solving.txt', 'w', encoding='utf8') as file:
    file.write('\n'.join(result))