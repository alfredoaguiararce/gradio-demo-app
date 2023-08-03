import gradio as gr

def saluda(nombre):
  return "hola " + nombre

# The line `demo = gr.Interface(fn=saluda, inputs=gr.Textbox(lines=10, placeholder="Dime tu nombre
# porfa"), outputs="text")` is creating a Gradio interface object called `demo`.
demo = gr.Interface(fn=saluda, inputs=gr.Textbox(lines=10, placeholder="Dime tu nombre porfa"), outputs="text")

demo.launch()