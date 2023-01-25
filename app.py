from aitextgen import aitextgen
import gradio as gr

# download the small model
ai = aitextgen()

# function that generates text from the model
def generate_text(prompt, max_length=300):
    return ai.generate(prompt=prompt, max_length=max_length, return_as_list=True)[0]

# show the generated text in a gradio interface
demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, label="Insert text or phrase"),
    outputs="text",
)

# launch the interface
demo.launch()
