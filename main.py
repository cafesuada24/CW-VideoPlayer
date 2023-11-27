from app.video_player import VideoPlayer
from app.core.videos_db import VideosDB

if __name__ == "__main__":
    videoplayer = VideoPlayer()
    videoplayer.mainloop()
    VideosDB().close()
