from .. import CONFIG
from .events import * 

LISTING_HEADING =  CONFIG['display']['columns']['check']['heading']
LISTING_COLUMNS = CONFIG['display']['columns']['check']['id']

class EventHandler:
    @staticmethod
    def eventhandler(_func):
        def _wrapper(*args, **kwargs):
            def _callback(e):
                _func(*args, **kwargs)
            return _callback
        return _wrapper
    
    @staticmethod
    @eventhandler
    def check_video(event: CheckButtonClickEvent, /):
        try:
            video_attr = (
                f'{attr}: {val}'
                for attr, val in zip(
                    LISTING_HEADING,
                    event.videos[event.id].list_all(
                        LISTING_COLUMNS
                    )
                )
            )
            event.output('\n'.join(video_attr))
        except KeyError as e:
            event.output(f'Video number not found: {event.id}')

    @staticmethod
    @eventhandler
    def update_video(event: UpdateButtonClickEvent, /):
        video_id = event.id
        column = event.column
        value = event.value

        if value == '':
            event.output('Value can not be empty')
            return

        try:
            event.videos[video_id][column] = value
        except KeyError as e:
            event.output(f'Video id not found: {e}') 
        except ValueError as e:
            event.output(f'Invalid value "{value}" for "{column}"')
        else:
            event.db.update(video_id, column, value)
            event.output('Updated!')
    
    @staticmethod
    @eventhandler
    def add_to_playlist(event: PlaylistButtonClickEvent, /):
        id = event.id
        status = True
        message = 'Added'
        try:
            video = event.videos[id]
            event.curr_playlist.add(video)
        except KeyError as e:
            message = f'Video id not found {id}'
            status = False
        finally:
            event.output(status, message)


    @staticmethod
    @eventhandler
    def remove_from_playlist(event: PlaylistButtonClickEvent, /):
        id = event.id 
        status = True
        message = 'Removed!'
        try:
            event.curr_playlist.remove(id)
        except KeyError as e:
            message = f'This video has not been added to playlist!'
            status = False
        finally:
            event.output(status, message)

    @staticmethod
    @eventhandler
    def play_playlist(event: PlaylistButtonClickEvent, /):
        message = 'Played!'
        
        if not event.curr_playlist:
            message = 'No video to play'
       
        for video in event.curr_playlist:
            video.increment_play_count()
            event.db.update(video.id, 'play_count', video.get_play_count())

        event.output(True, message)


        
