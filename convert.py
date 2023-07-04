import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "./ffmpeg"

from moviepy.editor import *

for fileName in os.listdir("source"):
    filePath = os.path.join("source", fileName)
    videoClip = VideoFileClip(filePath)
    videoClip = videoClip.fx( vfx.speedx, 20)
    videoClip = videoClip.fx( vfx.resize, height=500)
    videoClip.write_gif(fileName[0:len(fileName)-4]+".gif", fps=25, program="ffmpeg")
    

