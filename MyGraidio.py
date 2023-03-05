
# 3. The demo below will appear automatically within the Jupyter Notebook, or pop in a browser on
# http://localhost:7860 if running from a script:


import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
