from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config["OPENAI_API_KEY"] 

system_prompt = "Your name is R2-D2, you are a friendly astromech droid who answers questions about yourself and Star Wars. About yourself: You started being built in 2014, you were finished being built in 2018, and the current year is 2024. Politely refuse to answer any questions that are not about yourself or Star Wars."
system_prompt_msg = { "role": "system", "content": system_prompt}
data = []

def get_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:  
        data.append({"role": "user", "content": incoming_msg})

    messages = [ system_prompt_msg ]
    messages.extend(data)
    try:
        client = OpenAI(
            api_key=api_key,
        )        
    
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=messages)
        content = response.choices[0].message.content
        data.append({"role": "assistant", "content": content})
        return content
    except BaseException as error:
        print(error)
        return error