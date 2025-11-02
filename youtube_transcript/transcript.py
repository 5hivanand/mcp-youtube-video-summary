import typing
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from . import cache

ytt_api = YouTubeTranscriptApi()
formatter = SRTFormatter()

def fetch(video_id: str) -> typing.Optional[str]:
    """
    Fetches the transcript of a YouTube video by its ID.

    Args:
        video_id (str): The YouTube video ID.
    
    Returns:
        Optional[str]: The transcript text, or None if not available.
    """
    try:
        data = cache.get(video_id)
        if data is not None:
            return data
            
        t = ytt_api.fetch(video_id)
        srt = formatter.format_transcript(t)
        cache.set(video_id, srt)
        return srt
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None