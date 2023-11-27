""""
Edit to get different output forms.
"""

import pytube

vid_link = None
playlist_instance = pytube.Playlist(url= 'https://youtube.com/playlist?list=PL8LmuzdwmQIMDi2eUWkvvvA4zG58sgVCV&si=_08PiC0xbEgBhZGa')

video_objs = playlist_instance.videos
# pytube.YouTube().streams.get_highest_resolution().download() # This is just to get glimpse of what methods and properties the YT instance has
print(video_objs[0].streams.get_highest_resolution().download())