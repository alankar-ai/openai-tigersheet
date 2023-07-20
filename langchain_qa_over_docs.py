import os
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA


def read_api_key_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            api_key = file.read().strip()  # Read the key from the file and remove leading/trailing whitespaces
        return api_key
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Usage example
file_path = "api_key.txt"
knowledge_file = "tigersheet.txt"
api_key = read_api_key_from_file(file_path)

with open(knowledge_file, "r",encoding="utf8") as inp:
  tigersheet = inp.read()

openai.api_key = api_key       # Get this from openai
os.environ["OPENAI_API_KEY"] = api_key


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(tigersheet)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)
qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectorstore)

query = input("Enter Query:")
answer = qa.run(query)
print("Answer:",answer)

