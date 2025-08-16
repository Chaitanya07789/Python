# string[start:end:step] by default step is 1 if not given

text = "python programming"
reverse_text = ""
for i in text:
    reverse_text =  i + reverse_text

print(reverse_text)

print(text[::-1])

print(text[::2])

print(text[1:6])

print(text[7:-5])

print(text[-11:8])



