import asyncio
import edge_tts
import requests
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip
from PIL import Image
from io import BytesIO

# [설정]
PROMO_SCRIPT = "Looking for a new laptop? Don't miss this limited offer! Click the link below."
VOICE = "en-US-ChristopherNeural"
OUTPUT_VIDEO = "shorts_promo.mp4"

async def auto_promo_factory():
    print("🚀 AI 영상 제작 시작...")
    
    # 1. 목소리 생성
    communicate = edge_tts.Communicate(PROMO_SCRIPT, VOICE)
    await communicate.save("voice.mp3")
    
    # 2. 이미지 생성
    prompt = "laptop_advertisement_cinematic"
    image_url = f"https://pollinations.ai/p/{prompt}"
    img_data = requests.get(image_url).content
    with open("ai_generated.jpg", "wb") as f:
        f.write(img_data)
    
    # 3. 합성
    audio = AudioFileClip("voice.mp3")
    clip = ImageClip("ai_generated.jpg").set_duration(audio.duration)
    clip = clip.set_audio(audio)
    
    # 4. 파일 쓰기
    clip.write_videofile(OUTPUT_VIDEO, fps=24, codec="libx264")
    print("🎬 제작 완료!")

if __name__ == "__main__":
    asyncio.run(auto_promo_factory())
