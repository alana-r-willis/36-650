punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = "Hello in 36-650,& other MSP courses."

new_text = str()

for x in punctuations:
    text=text.replace(x,"")
    
print(text)
    