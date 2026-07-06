from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

model = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct", 
    temperature=0.7)


#Embedding Model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
)

#Vector Store
vector_store = Chroma(
    persist_directory="./chroma_langchain_db",
    embedding_function=embeddings
)


while True:
    query = input('User: ')
    if query.lower() =='bye':
        break
    
    results = vector_store.similarity_search(query, k =2)
    context = '\n'.join(i.page_content for i in results)

    prompt = f"""
Answer this question based on the context below.
Context:
{context}

Question:
{query}
        """
    
    response = model.invoke(prompt)
    print('Chatbot: ', response.content)