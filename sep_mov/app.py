import argparse
import datetime
import moviepy.video.fx.all as vfx
from moviepy.editor import *
import settings

input_path,output_dir,name = settings.get_settings()

def sep(ip):
    # 動画の読み込み
    video = VideoFileClip(ip)
    print("frames: {}".format(video.reader.nframes))
    print("fps: {}".format(video.fps))
    print("duration: {}".format(video.duration))
    print("size: {}".format(video.size))
    # 上半分
    upper = video.fx(vfx.crop, x1=0, y1=0, x2=1920, y2=1080)
    # 下半分
    lower = video.fx(vfx.crop,y1=1080)

    return upper, lower

def save(clips, name):
    upper, lower = clips
    upper.write_videofile(f"game/{name}.mp4")
    lower.write_videofile(f"eye/{name}.mp4")

if __name__ == '__main__':
    save(sep(settings.input_path), settings.name)
    print('--fin--')

