import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def load_transcript_vectorstore():
    if not os.path.exists("vectorstore/index"):
        return _create_vectorstore()
    return Chroma(persist_directory="vectorstore", embedding_function=OpenAIEmbeddings())

def _create_vectorstore():
    pdf_dir = "data"
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

    docs = []
    for pdf in pdfs:
        loader = PyPDFLoader(os.path.join(pdf_dir, pdf))
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="vectorstore")
    vectorstore.persist()
    return vectorstore
