import asyncio, edge_tts, requests, os, sys, random
from moviepy.editor import ImageClip, AudioFileClip

async def talk_with_user(text):
    print(f"\n💬 명령 수신: {text}")
    
    # 1. 한국어 음성 생성
    communicate = edge_tts.Communicate(text, "ko-KR-SunHiNeural")
    await communicate.save("voice.mp3")
    
    # 2. 이미지 가져오기
    img_url = f"https://picsum.photos/1080/1920?sig={random.randint(1, 9999)}"
    r = requests.get(img_url)
    with open("temp.jpg", "wb") as f: f.write(r.content)

    # 3. 조립 (파일명: ai_result.mp4)
    audio = AudioFileClip("voice.mp3")
    clip = ImageClip("temp.jpg").set_duration(audio.duration).set_audio(audio)
    clip.write_videofile("ai_result.mp4", fps=24, codec="libx264", logger=None)
    print(f"✅ 영상 제작 끝! 이제 결과물을 확인하세요.")

if __name__ == "__main__":
    user_msg = sys.argv[1] if len(sys.argv) > 1 else "명령 대기 중"
    asyncio.run(talk_with_user(user_msg))
