from ..singleton import SingletonMeta
from ..widgets.head_bar import HeadBar
from ..widgets.video_browser import VideoBrowser
from ..widgets.footer import Footer
from ..widgets.create_video_list import CreateVideoListPanel
from ..widgets.check_videos import CheckVideosPanel
from ..widgets.update_videos import UpdateVideoPanel

class Widgets(metaclass=SingletonMeta):
    def __init__(self, main_frame):
        self.__head_bar = HeadBar(main_frame)
        self.__footer = Footer(main_frame)
        self.__browser = VideoBrowser(main_frame)
        self.__panels = (
                CheckVideosPanel(main_frame),
                CreateVideoListPanel(main_frame),
                UpdateVideoPanel(main_frame)
                )

    @property
    def HEAD_BAR(self):
        return self.__head_bar
    
    @property
    def FOOTER(self):
        return self.__footer

    @property
    def BROWSER(self):
        return self.__browser

    @property
    def CHECK_VIDEOS_PANEL(self):
        return self.__panels[0]
    
    @property
    def CREATE_VIDEO_LIST_PANEL(self):
        return self.__panels[1]
    
    @property
    def UPDATE_VIDEO_PANEL(self):
        return self.__panels[2]

