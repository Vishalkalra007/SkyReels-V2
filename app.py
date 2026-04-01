import gradio as gr

def test_fn(text):
    return f"Echo: {text}"

demo = gr.Interface(fn=test_fn, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()