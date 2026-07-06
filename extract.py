import fitz

all_text = ' '

doc = fitz.open('sample.pdf')
for i in range(len(doc)):
    text = doc[i].get_text()
    all_text += text
    
with open('extract.txt','w') as file:
        file.write(all_text)