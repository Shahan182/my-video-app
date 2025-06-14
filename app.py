import gradio as gr  
def generate_video(image):  
    return "video.mp4"  # Demo code  
gr.Interface(generate_video, inputs="image", outputs="video").launch()  
