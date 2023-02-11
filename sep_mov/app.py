import argparse
import datetime
import moviepy.editor as mp
import settings

input_path,output_dir,name = settings.get_settings()

def sep(ip):
    # 動画の読み込み
    video = mp.VideoFileClip(ip)

    # 上半分
    upper = video.crop(y1=0, y2=1080)

    # 下半分
    lower = video.crop(y1=1080, y2=2160)

    return upper, lower

def save(clips, name, op):
    upper, lower = clips
    upper.write_videofile(f"{op}/game/{name}.mp4")
    lower.write_videofile(f"{op}/eye/{name}.mp4")

if __name__ == '__main__':
    save(sep(settings.input_path), settings.name, settings.output_dir)
    print('--fin--')

