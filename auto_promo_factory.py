import asyncio, edge_tts, requests, os, sys, random
from moviepy.editor import ImageClip, AudioFileClip

async def talk_to_ai_factory():
    # 입력창에서 보낸 메시지를 가져옵니다.
    user_input = sys.argv[1] if len(sys.argv) > 1 else "No input"
    print(f"💬 명령어 수신: {user_input}")

    try:
        # 1. 입력한 말로 목소리 만들기
        communicate = edge_tts.Communicate(user_input, "en-US-ChristopherNeural")
        await communicate.save("voice.mp3")
        
        # 2. 배경 이미지 가져오기
        img_url = f"https://picsum.photos/1080/1920?sig={random.randint(1, 999)}"
        r = requests.get(img_url, timeout=15)
        with open("temp.jpg", "wb") as f: f.write(r.content)

        # 3. 영상 조립
        audio = AudioFileClip("voice.mp3")
        clip = ImageClip("temp.jpg").set_duration(audio.duration)
        clip = clip.set_audio(audio)
        clip.write_videofile("shorts_promo.mp4", fps=24, codec="libx264")
        
    except Exception as e:
        print(f"🚨 에러: {e}")
        exit(1)

if __name__ == "__main__":
    asyncio.run(talk_to_ai_factory())
