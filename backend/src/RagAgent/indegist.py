from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import *
from langchain_community.document_loaders import CSVLoader
import os
#embedding creation
embdata = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

csvfile_name="climate.csv"


if not os.path.exists(csvfile_name):
    print(f"csv file doesnot exist{csvfile_name} ")
else:
    print(f"path exist in it")

pageloade=CSVLoader(csvfile_name)
try:
    page_data=pageloade.load()
    print(f"length of the file csv data:{len(page_data)}")
except Exception as e:
    print("error occuring in the loading of the file thing")


chuncking_data=RecursiveCharacterTextSplitter(
chunk_size=600,
chunk_overlap=200
)
page_split=chuncking_data.split_documents(page_data)

vectorstore = Chroma.from_documents(
    documents=page_split,
    embedding=embdata,
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION_NAME
)

vectorstore.persist()
print("vector data base created successfully")
