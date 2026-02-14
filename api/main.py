import gradio as gr


def hello(name: str) -> str:
    return f"Hello, {name or 'World'}!"


ui = gr.Interface(
    fn=hello,
    inputs=gr.Textbox(label="Imię", placeholder="World"),
    outputs=gr.Textbox(label="Wiadomość"),
    title="Hello World",
    description="Prosta aplikacja Gradio."
)


if __name__ == "__main__":
    ui.launch(server_name="0.0.0.0", server_port=7860)