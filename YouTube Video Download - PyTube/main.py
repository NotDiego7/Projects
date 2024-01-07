""""
This is for playlists
"""

import pytube, subprocess, time

# vid_link = None
# playlist_instance = pytube.Playlist(url= 'https://youtube.com/playlist?list=PL8LmuzdwmQIMDi2eUWkvvvA4zG58sgVCV&si=_08PiC0xbEgBhZGa')

# video_objs = playlist_instance.videos
# # pytube.YouTube().streams.get_audio_only(subtype= "mp3") # This is just to get glimpse of what methods and properties the YT instance has
# audio_file = r"" + video_objs[1].streams.get_audio_only().download()


# subprocess.run(["powershell.exe", "start", "\"" + audio_file + "\""])

# ---------------------------------------------------------------------------- #
def download_and_play(youtube_link):

    song = pytube.YouTube(url= youtube_link)

    audio_file_path = song.streams.get_audio_only().download(output_path= r"C:\Users\Lopez\Music\Output")

    subprocess.run(["powershell.exe", "start", "\"" + audio_file_path + "\""])

download_and_play('https://music.youtube.com/watch?v=dM_aZOAeLso&si=pK4FMx8QP6kHOQgH') # NOTE: Having to input the link manually is obviously provisional