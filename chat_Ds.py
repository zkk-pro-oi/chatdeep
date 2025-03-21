import os

from langchain.chains import ConversationChain
from langchain_deepseek import ChatDeepSeek

from langchain.memory import ConversationBufferMemory
def get_chat_response(prompt,memory,openai_api_key):
    model = ChatDeepSeek(model="deepseek-chat",openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model,memory=memory)

    response = chain.invoke({"input":prompt})
    return response["response"]

memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("牛顿提出过哪些知名的定律",memory,os.getenv("DEEPSEEK_API_KEY")))
# print(get_chat_response("我上一个问题是什么",memory,os.getenv("DEEPSEEK_API_KEY")))