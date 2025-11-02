from youtube_transcript import get_video_id_from_url, get_transcript_from_id
from fastmcp import FastMCP
import yaml

mcp = FastMCP(name="YouTube Video Transcript Fetcher")

with open("prompts.yaml") as f:
    prompts = yaml.safe_load(f)


@mcp.tool
def get_youtube_video_transcript(url: str) -> str:
    """Fetches the transcript of a YouTube video given its URL.
        Args:
            url (str): The URL of the YouTube video.
        Returns:
            str: The transcript of the video in SRT format if available.
        Raises:
            ValueError: If the URL is invalid or the transcript is not available.
    """
    video_id = get_video_id_from_url(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")
    transcript = get_transcript_from_id(video_id)
    if not transcript:
        raise ValueError("Transcript not available for this video")
    return transcript

@mcp.prompt
def quick_summary_prompt(video_url: str) -> str:
    """Generates a quick summary prompt for a YouTube video given its URL."""
    prompt = prompts["quick_summary_prompt"].format(video_url=video_url)
    return prompt

@mcp.prompt
def detailed_summary_prompt(video_url: str) -> str:
    """Generates a detailed summary prompt for a YouTube video given its URL."""
    prompt = prompts["detailed_summary_prompt"].format(video_url=video_url)
    return prompt

@mcp.prompt
def structured_notes_prompt(video_url: str) -> str:
    """Generates a structured notes prompt for a YouTube video given its URL."""
    prompt = prompts["structured_notes_prompt"].format(video_url=video_url)
    return prompt

def main():
    # mcp.run()
    # Configure transport when running
    mcp.run(
        transport="stdio"    # Use standard I/O transport
    )
    

if __name__ == "__main__":
    main()
