import streamlit as st
from app.modules import transcript_extractor, highlight_analyzer, video_processor
from app.config import Config

def main():
    st.set_page_config(page_title="Podcast Highlight Generator", layout="wide")
    
    st.title("🎥 AI-Powered Podcast Highlights")
    st.markdown("### Automatically extract key moments from YouTube podcasts")
    
    with st.sidebar:
        st.header("Settings")
        youtube_url = st.text_input("YouTube URL")
        num_highlights = st.slider("Number of Highlights", 1, 10, 5)
        process_button = st.button("Generate Highlights")
    
    if process_button and youtube_url:
        with st.spinner("Processing..."):
            # Extract video ID
            video_id = transcript_extractor.extract_video_id(youtube_url)
            
            # Get transcript
            transcript = transcript_extractor.get_transcript(video_id)
            
            # Analyze highlights
            highlights = highlight_analyzer.analyze_transcript(
                transcript, 
                Config.OPENAI_API_KEY,
                highlight_count=num_highlights
            )
            
            # Display results
            st.subheader("Generated Highlights")
            for idx, highlight in enumerate(highlights, 1):
                with st.expander(f"Highlight #{idx}: {highlight['title']}"):
                    st.write(f"**Timestamp:** {highlight['start_time']}s - {highlight['end_time']}s")
                    st.write(highlight['description'])
                    
                    if st.button(f"Download Highlight #{idx}", key=f"download_{idx}"):
                        video_path = video_processor.download_and_clip(
                            video_id,
                            highlight,
                            Config.OUTPUT_DIR
                        )
                        st.success(f"Clip saved to: {video_path}")

if __name__ == "__main__":
    main()
