from langchain_text_splitters import RecursiveCharacterTextSplitter
import pickle
with open('extract.txt','r') as file:
    document = file.read()
    
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(document)

with open('chunks.pkl','wb') as file:
   pickle.dump(texts,file)