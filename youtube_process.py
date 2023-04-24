from pytube import YouTube as yt
import shutil
import os

class YotubeProcess():
    def __init__(self,directory,youtube_url):
        self.directory = directory
        self.youtube_url = youtube_url
    def download_video(self):
        self.out_file=yt(self.youtube_url).streams.filter(progressive=True,file_extension="mp4").desc().first().download(self.directory)

    def convert_mp3(self,only_mp3=True):    
        base , ext = os.path.splitext(self.out_file)
        new_file = base+".mp3"
        if only_mp3:
            os.rename(self.out_file,new_file)
        else:
            shutil.copy2(self.out_file,new_file)