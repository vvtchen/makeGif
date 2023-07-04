import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/arieschen/Downloads/ffmpeg"

from moviepy.editor import *

for fileName in os.listdir("source"):
    if fileName == ".DS_Store":
        continue
    
    filePath = os.path.join("source", fileName)
    try:
        videoClip = VideoFileClip(filePath)
        videoClip = videoClip.fx(vfx.speedx, 1.9)
        videoClip = videoClip.fx(vfx.resize, height=600)
        videoClip.write_gif(fileName[:-4] + ".gif", fps=6, program="ffmpeg")
    except Exception as e:
        print(f"Error processing file {fileName}: {str(e)}")
