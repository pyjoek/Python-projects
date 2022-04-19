import time
import vlc

player = vlc.Instance()

media = player.media_new("any.--")

media_player = player.media_player_new()

media_player.set_media(media)

media_player.video_set_scale(0,6)

media_player.play()

time.sleep(5)
