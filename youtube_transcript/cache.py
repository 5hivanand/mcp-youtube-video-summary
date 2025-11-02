import typing
import os

def get(video_id: str) -> typing.Optional[str]:
    """
    Retrieves the cached transcript of a YouTube video by its ID, if it exists.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        Optional[str]: The cached transcript text, or None if not found.
    """
    try:
        cache_file = os.path.join("/tmp", f"{video_id}.srt")
        fstat = os.stat(cache_file)
        if fstat.st_size > 0:
            with open(cache_file, "r") as f:
                return f.read()
    except FileNotFoundError:
        return None
    
def set(video_id: str, transcript: str) -> None:
    """
    Caches the transcript of a YouTube video by its ID.

    Args:
        video_id (str): The YouTube video ID.
        transcript (str): The transcript text to cache.
    """
    cache_file = os.path.join("/tmp", f"{video_id}.srt")
    with open(cache_file, "w") as f:
        f.write(transcript) 