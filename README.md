# YouTube Video Summary

A Model Context Protocol (MCP) server that fetches YouTube video transcripts and generates customizable summaries.

## Features

- **Video ID Extraction**: Extract YouTube video IDs from various URL formats (youtube.com, youtu.be, etc.)
- **Transcript Fetching**: Fetch video transcripts using the YouTube Transcript API
- **Caching**: Cache transcripts locally for faster retrieval
- **Customizable Prompts**: Generate summaries in multiple formats:
  - Quick 30-second summary
  - Detailed 2-3 minute summary
  - Structured notes in markdown format

## Installation

### Requirements
- Python >= 3.12
- `uv` package manager (optional, but recommended)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Youtube-Video-Summary
```

2. Install dependencies:
```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

## Usage

### Running the MCP Server

```bash
uv run main.py
```

The server will start with standard I/O transport for MCP communication.

### Available Tools

- **`get_youtube_video_transcript(url: str)`**: Fetches the transcript for a given YouTube URL

### Available Prompts

- **`quick_summary_prompt(video_url: str)`**: Generates a quick 30-second summary
- **`detailed_summary_prompt(video_url: str)`**: Generates a detailed 2-3 minute summary
- **`structured_notes_prompt(video_url: str)`**: Generates comprehensive structured notes

## Integration with AI Clients

### Claude Desktop

1. Open `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Add the following configuration:
```json
{
  "mcpServers": {
    "Youtube-Video-Summary": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/Shiva/Developer/mcp/mcp-youtube-video-summary",
        "run",
        "main.py"
      ]
    }
  }
}
```
3. Restart Claude Desktop

### VS Code

1. Install the MCP extension for VS Code
2. Add the server configuration to VS Code settings:
```json
{
  "mcp.servers": {
    "Youtube-Video-Summary": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/Shiva/Developer/mcp/mcp-youtube-video-summary",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Project Structure

```
.
├── main.py                          # MCP server entry point
├── prompts.yaml                     # Prompt templates
├── pyproject.toml                   # Project configuration
├── youtube_transcript/
│   ├── __init__.py                 # Package exports
│   ├── video_id.py                 # Video ID extraction
│   ├── transcript.py               # Transcript fetching
│   └── cache.py                    # Local caching
└── README.md                        # This file
```

## Configuration

Edit `prompts.yaml` to customize the summary prompts for different use cases.

## Dependencies

- **fastmcp**: Model Context Protocol framework
- **youtube-transcript-api**: YouTube transcript fetching
- **PyYAML**: YAML configuration parsing

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!