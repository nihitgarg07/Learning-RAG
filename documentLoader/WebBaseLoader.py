from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template= "Answer the following Question -n \n {ques} from the following {text}",
    input_variables= ['text','ques']
)

parser = StrOutputParser()

url = "https://www.flipkart.com/dell-se-series-60-96-cm-24-inch-full-hd-led-backlit-ips-panel-contrast-1-000-1-tilt-adjustment-1x-hdmi-1xvga-3-years-warranty-tuv-rheinland-3-star-eye-comfort-ultra-thin-bezel-monitor-se2425hm/p/itmdd27b93ff07be?pid=MONG4NSZXZUGZTUC&lid=LSTMONG4NSZXZUGZTUCDYS38D&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_XaOya4ufQcQDq7UM7SH2tzYI6GZt-Sx_TukerB1Z_rAr5UraSwv1pGBq_DR-P3gie665z_6zoDTsFG95bwx5kvUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=1hcw7lpqy80000001756688468508"

loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'ques':'what is the product that we are talking about','text':docs[0].page_content}))
