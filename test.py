from time import sleep
from twitchtube.video import make_video
from twitchtube.utils import get_path
from twitchtube.config import CLIENT_ID, OAUTH_TOKEN, DATA, LANGUAGE, PERIOD, VIDEO_LENGTH, LIMIT



while True:
    make_video(
        data=DATA,
        path=get_path(),
        client_id=CLIENT_ID,  # example client id (fake)
        oauth_token= OAUTH_TOKEN,  # example token (fake)
        video_length=VIDEO_LENGTH , # minutes as float
        resolution=(1080, 1920), # height x width
        frames=60,
        language=LANGUAGE,
        period=PERIOD, 
        delete_clips=False,
        limit= LIMIT,
        
        
    )
    sleep(24 * 60 * 60) # make a video daily


    