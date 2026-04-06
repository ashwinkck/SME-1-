#1 Importing tools
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#2 loading the pdf Doc's
loader1 = PyPDFLoader(r"C:\Users\ashwi\Desktop\medicaps\session4\ai-product-builder\data\startups.pdf")
loader2 = PyPDFLoader(r"C:\Users\ashwi\Desktop\medicaps\session4\ai-product-builder\data\tech_trends.pdf")

doc1 = loader1.load()
doc2 = loader2.load()

documents = doc1 + doc2

#3 Splitting Documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000, 
    chunk_overlap = 200,
)
splits = text_splitter.split_documents(documents)

#4 Creating the Embedding model

embedding_model = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
)

#5 Creating the Vector DB
vector_db = Chroma.from_documents(
    documents=splits,
    embedding = embedding_model,
    persist_directory="vector_db"
)

#6 Creating a Retriever
retriever = vector_db.as_retriever(search_kwargs={"k":3})