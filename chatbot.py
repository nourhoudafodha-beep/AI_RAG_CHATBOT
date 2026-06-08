from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embedding_model,
    allow_dangerous_deserialization=True
)

question = input("Question : ")

docs = db.similarity_search(question, k=3)

for doc in docs:
    print("----------------")
    print(doc.page_content)