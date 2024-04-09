from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')

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
        client = OpenAI(api_key=api_key)        
    
        # temperature=0 did result in much more consistent answers in general, but much less creativity and variety on other responses.  
        # It produced more accurate responses about his age but if he got the answer wrong the first time, he would always get it wrong the rest of the conversation.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature = 0.7,             
            messages=messages)
        response_content = response.choices[0].message.content
        data.append({"role": "assistant", "content": response_content})
        return response_content
    except BaseException as error:
        print(error)
        return error