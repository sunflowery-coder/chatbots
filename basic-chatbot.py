import gradio

def chatbot(input_text):
    if input_text.lower() == 'hello':
        return 'hello, how can I help you'
    elif input_text.lower() == 'how are you?':
        return 'I am good. How are you today?'
    elif input_text.lower() == 'bye bye':
        return 'have a great day'
    else :
        return 'I am sorry, I dont understand'

demo = gradio.Interface(fn=chatbot, inputs='text', outputs='text')
demo.launch()