from langchain.chains import ConversationChain
from langchain_deepseek import ChatDeepSeek

import os
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, memory, deepseek_api_key):
    model = ChatDeepSeek(model="deepseek-chat", api_key=deepseek_api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]
