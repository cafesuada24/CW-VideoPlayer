from dataclasses import dataclass

from .widgets import *

# @dataclass(frozen=True)
# class Constants:
#     DEFAULT = {
#             'head_bar': ,
#             'footer': ,
#             'browser':,
#
#             }
#     RPANELS = {
#             'check_video': ,
#             }
#

@dataclass(frozen=False)
class Widgets:
    MAIN_LAYOUT = None
    HEAD_BAR = None
    FOOTER = None
    BROWSER = None
    CHECK_VIDEOS_PANEL = None
    CREATE_VIDEO_LIST_PANEL = None
    UPDATE_VIDEO_PANEL = None
