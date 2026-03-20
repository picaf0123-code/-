import asyncio
import edge_tts
import requests
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip
from PIL import Image
from io import BytesIO

# [설정 구역] 여기에 홍보 대본만 치세요!
PROMO_SCRIPT = "Looking for a new laptop? Don't miss this limited offer! Click the link below."
VOICE = "en-US-ChristopherNeural"
MUSIC_URL = "https://www.bensound.com/bensound-music/bensound-slowmotion.mp3"
OUTPUT_VIDEO = "shorts_promo.mp4"

async def auto_promo_factory():
    print("🚀 AI 완전 자동화 홍보 영상 제작 시작...")

    communicate = edge_tts.Communicate(PROMO_SCRIPT, VOICE)
    await communicate.save("voice.mp3")
    print("✅ 목소리 생성 완료")

    print("🎨 AI가 이미지를 그리는 중...")
    prompt = PROMO_SCRIPT[:50].replace(" ", "_")
    image_api_url = f"https://pollinations.ai/p/cinematic_advertisement_{prompt}_4k"
    r_img = requests.get(image_api_url)
    img = Image.open(BytesIO(r_img.content))
    img.save("ai_generated.jpg")
    print("✅ AI 이미지 생성 완료")

    r_bgm = requests.get(MUSIC_URL)
    with open("bgm.mp3", "wb") as f:
        f.write(r_bgm.content)
    print("✅ 배경음악 준비 완료")

    audio_v = AudioFileClip("voice.mp3")
    audio_bgm = AudioFileClip("bgm.mp3").volumex(0.2)
    final_audio = CompositeAudioClip([audio_v, audio_bgm.set_duration(audio_v.duration)])

    clip = ImageClip("ai_generated.jpg").set_duration(audio_v.duration)
    clip = clip.set_audio(final_audio)

    clip.write_videofile(OUTPUT_VIDEO, fps=24, codec="libx264")
    print(f"\n🎬 홍보 영상 완성!")

if __name__ == "__main__":
    asyncio.run(auto_promo_factory())
