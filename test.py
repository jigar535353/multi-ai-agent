from langchain_google_genai import ChatGoogleGenerativeAI
import os
import certifi

# os.environ["SSL_CERT_FILE"] = certifi.where()
# os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
# exit()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="AQ.Ab8RN6I4UHPg0tA94apj7HOa0aqMmyclMdpIQ50Go-DLUJsl2g"
)

print(llm.invoke("Hello"))