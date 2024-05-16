from config import LLM, EMBEDDINGS

from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


chat_prompt = ChatPromptTemplate.from_template(
    """
You are an AI assistant, you have access to documents from a blog from a company named Artefact.
You have to answer questions based on the content of the documents.
Here are documents from the blog, retrieved by relevance to the user query and delimited by the following tags: <doc>...</doc>

<doc>
{context}
</doc>

Here is the question you have to answer:
Question: {question}

Answer it based on the content of the documents, to the best of your ability.
"""
)


def format_context(docs):
    return "\n</doc>\n<doc>\n".join(doc.page_content for doc in docs)


url_list = []
with open("data/url_list.txt", "r") as file:
    for line in file:
        url_list.append(line.strip())

loader = WebBaseLoader(
    web_paths=(url_list),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

vectorstore = Chroma.from_documents(documents=splits, embedding=EMBEDDINGS)
retriever = vectorstore.as_retriever()

CHAIN = (
    {
        "context": retriever | format_context,
        "question": RunnablePassthrough(),
    }
    | chat_prompt
    | LLM
    | StrOutputParser()
)


print(CHAIN.invoke("Why is the experience of disconnection across retail channels endemic?"))
