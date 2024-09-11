from openai import OpenAI
import os

def get_response(messages):
    client = OpenAI(
        # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        api_key=os.getenv("DASHSCOPE_API_KEY"), 
        # 填写DashScope服务的base_url
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-max",
        messages=messages,
        stream=True,
        # 可选，配置以后会在流式输出的最后一行展示token使用信息
        # stream_options={"include_usage": True}
        )
    for chunk in completion:
        yield chunk.choices[0].delta.content

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
# 您可以自定义设置对话轮数，当前为3
while(1):
    assistant_output = ''
    user_input = input("Me: ")
    if(user_input == 'quit'):
        break
    # 将用户问题信息添加到messages列表中
    messages.append({'role': 'user', 'content': user_input})
    
    print(f'Tars: ', end='')
    for content in get_response(messages):        
        print(f'{content}', end='')
        assistant_output += content
    # 将大模型的回复信息添加到messages列表中
    messages.append({'role': 'assistant', 'content': assistant_output})
    
    print('\n')