import os
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 1. SETUP MODEL & EMBEDDINGS
model = ChatOllama(model="llama3.2:3b")
embeddings = OllamaEmbeddings(model="llama3.2:3b")

# 2. LOAD YOUR EXISTING DATABASE
db_path = "./chroma_db" 

if not os.path.exists(db_path):
    print(f"❌ Error: Folder '{db_path}' not found!")
    exit()

vector_db = Chroma(persist_directory=db_path, embedding_function=embeddings)

# 3. SETUP PROMPT (Wichtig: Wir nutzen 'question', das ist der Standard-Key)
template = """Answer the question based only on the context below.
Context: {context}
Question: {question}
Answer:"""
rag_prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# 4. CHAT FUNCTION (With Debug/Visual Check)
def start_terminal_chat(vector_db):
    # We take the top 5 most relevant parts from the PDF
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    
    chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",
        retriever=retriever,
        input_key="query", 
        return_source_documents=True, # Important: This enables the source check
        chain_type_kwargs={"prompt": rag_prompt}
    )

    print("\n" + "="*40)
    print("✅ MEDICAL CHAT READY (Terminal Mode)")
    print("Type your question and press Enter.")
    print("Type 'exit' to quit.")
    print("="*40)

    while True:
        user_input = input("\nYOUR QUESTION: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        print("AI is searching and thinking...")
        try:
            # Get response and the found text chunks
            response = chain.invoke({"query": user_input})
            
            # --- DEBUG VISUALIZATION START ---
            # Hier zeigen wir kurz an, was die KI gefunden hat
            print("\n🔍 [DEBUG] SEARCH RESULTS (CHUNKS FOUND):")
            print("-" * 30)
            for i, doc in enumerate(response["source_documents"]):
                # Show first 80 characters of each chunk
                preview = doc.page_content[:80].replace('\n', ' ')
                print(f"Chunk {i+1}: {preview}...")
            print("-" * 30)
            # --- DEBUG VISUALIZATION END ---

            print("\n🤖 AI RESPONSE:")
            print(response["result"])
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_terminal_chat(vector_db)