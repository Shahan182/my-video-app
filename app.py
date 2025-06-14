import gradio as gr  

def generate_video(image):  
    return "demo.mp4"  # Temporary fix  

gr.Interface(  
    fn=generate_video,  
    inputs=gr.Image(),  
    outputs=gr.Video(),  
    title="VIDEO GENERATOR"  
).launch(server_name="0.0.0.0", server_port=8080)  
