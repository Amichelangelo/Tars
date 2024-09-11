from openai import OpenAI
import os

def get_response():
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-max",
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': '你是谁？'}],
        stream=True,
        # 可选，配置以后会在流式输出的最后一行展示token使用信息
        # stream_options={"include_usage": True}
        )
    for chunk in completion:
        print(chunk.choices[0].delta.content, end="")

if __name__ == '__main__':
    get_response()