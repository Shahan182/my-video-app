import gradio as gr  

def generate_video(image):  
    return "video.mp4"  # Demo function  

gr.Interface(  
    fn=generate_video,  
    inputs=gr.Image(),  
    outputs=gr.Video(),  
    title="🚀 My Video Generator"  
).launch()  
