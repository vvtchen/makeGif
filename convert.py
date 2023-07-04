import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/arieschen/Downloads/ffmpeg"

from moviepy.editor import *

for fileName in os.listdir("source"):
    filePath = os.path.join("source", fileName)
    videoClip = VideoFileClip(filePath)
    videoClip = videoClip.fx( vfx.speedx, 10)
    videoClip = videoClip.fx( vfx.resize, height=900)
    videoClip.write_gif(fileName[0:len(fileName)-4]+".gif", fps=25, program="ffmpeg")
    

