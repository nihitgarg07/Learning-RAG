from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

Loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls= PyPDFLoader # type: ignore
)

docs = Loader.lazy_load()


for document in docs:
    print(document.page_content)
    print(document.metadata)