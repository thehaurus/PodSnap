from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(youtube_url):
    """Extract the video ID from a YouTube URL."""
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', youtube_url)
    if video_id_match:
        return video_id_match.group(1)
    return None

def get_transcript(youtube_url):
    """Extract transcript with timestamps from a YouTube video."""
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return {"error": "Invalid YouTube URL"}
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        return {"error": f"Failed to extract transcript: {str(e)}"}
