from langchain_community.document_loaders import TextLoader, PyPDFLoader
import os

DATA_PATH = "data"

documents = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DATA_PATH, file))
        documents.extend(loader.load())

print(f"Nombre de pages chargées : {len(documents)}")

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Nombre de chunks : {len(chunks)}")

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

from langchain_community.vectorstores import FAISS

db = FAISS.from_documents(
    chunks,
    embedding_model
)

db.save_local("vector_db")

print("Base vectorielle créée avec succès.")