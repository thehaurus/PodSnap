import subprocess
import os
from typing import Dict

def download_youtube_video(video_id: str, output_path: str) -> str:
    """Download YouTube video using yt-dlp."""
    video_filename = os.path.join(output_path, f"{video_id}.mp4")
    
    command = [
        'yt-dlp',
        f'https://www.youtube.com/watch?v={video_id}',
        '-f', 'best[height<=720]',
        '-o', video_filename
    ]
    
    subprocess.run(command, check=True)
    return video_filename

def create_highlight_clip(video_path: str, 
                         highlight: Dict, 
                         output_dir: str,
                         video_id: str,
                         index: int) -> Dict:
    """Create a highlight clip from the video."""
    # Create sanitized filename from title
    safe_title = "".join([c if c.isalnum() else "_" for c in highlight["title"]])
    output_filename = f"{video_id}_highlight_{index}_{safe_title}.mp4"
    output_path = os.path.join(output_dir, output_filename)
    
    # Use FFmpeg to extract the clip
    command = [
        'ffmpeg',
        '-i', video_path,
        '-ss', str(highlight["start_time"]),
        '-to', str(highlight["end_time"]),
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-preset', 'fast',
        '-y',
        output_path
    ]
    
    subprocess.run(command, check=True)
    
    # Add output path to highlight metadata
    highlight["video_path"] = output_path
    return highlight
