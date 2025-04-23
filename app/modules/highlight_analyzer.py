import openai
from typing import List, Dict, Any

def analyze_transcript(transcript_data: List[Dict[Any, Any]], 
                       api_key: str, 
                       highlight_count: int = 5,
                       min_highlight_duration: int = 15,
                       max_highlight_duration: int = 120):
    """Identify key highlights in the transcript using GPT."""
    openai.api_key = api_key
    
    # Format transcript for GPT input
    formatted_transcript = "\n".join([
        f"[{entry['start']}s - {entry['start'] + entry['duration']}s] {entry['text']}" 
        for entry in transcript_data
    ])
    
    prompt = f"""
    Analyze this podcast transcript and identify the {highlight_count} most insightful moments 
    that would make compelling highlight clips. Each highlight should be between 
    {min_highlight_duration} and {max_highlight_duration} seconds long.
    
    For each highlight, provide:
    1. Start timestamp (in seconds)
    2. End timestamp (in seconds)
    3. Title (catchy, under 60 characters)
    4. Description (1-2 sentences explaining the significance)
    
    Format your response as JSON with keys: "highlights" containing an array of objects 
    with "start_time", "end_time", "title", and "description".
    
    Transcript:
    {formatted_transcript}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert podcast editor."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    # Process and parse the JSON response
    # Additional error handling and parsing logic would be implemented here
    
    return highlights
