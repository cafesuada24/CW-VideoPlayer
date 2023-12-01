"""
Video Player main module
"""
from app.video_player import VideoPlayer
from app.core.videos_db import VideosDB


def main():
    videoplayer = VideoPlayer()
    videoplayer.mainloop()
    VideosDB().close()

if __name__ == "__main__":
    main()    
