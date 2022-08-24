from fileinput import close, filename
import pytube as pt
from moviepy.editor import VideoFileClip

def GetVideo(path):
    info = pt.YouTube(path)
    video = info.streams.filter(file_extension="mp4")
    video = info.streams.first()
    NewPath = video.download('HW\9thHW\YouTube\Videos')
    clip = VideoFileClip(NewPath)
    audio = clip.audio
    NewFile = open(f"HW\9thHW\YouTube\MP3\{info.title}.mp3", "w+")
    NewFile.close()
    audio.write_audiofile(f"HW\9thHW\YouTube\MP3\{info.title}.mp3")
    audio.close
    clip.close
    return