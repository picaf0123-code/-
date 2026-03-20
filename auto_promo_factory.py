import asyncio, edge_tts, requests, os, random
from moviepy.editor import ImageClip, AudioFileClip

async def smart_repair_factory():
    try:
        print("🔧 지능형 수리공 가동 중... (대기 모드 해제)")
        
        # 1. 목소리 생성 (에러 방지를 위해 랜덤 대사 중 하나 선택)
        scripts = [
            "Don't miss this limited offer! Click the link below.",
            "Check out our amazing new collection today!",
            "Special discount available for a limited time only."
        ]
        script = random.choice(scripts)
        
        communicate = edge_tts.Communicate(script, "en-US-ChristopherNeural")
        await communicate.save("voice.mp3")
        print("✅ 목소리 부품 제작 완료")
        
        # 2. 이미지 조달 (1번 서버 에러 시 2번 예비 서버로 자동 우회)
        try:
            # 매번 다른 이미지를 가져오도록 랜덤 숫자 추가
            img_url = f"https://picsum.photos/1080/1920?random={random.random()}"
            r = requests.get(img_url, timeout=10)
            with open("temp.jpg", "wb") as f: f.write(r.content)
        except:
            print("🚨 1번 이미지 서버 응답 없음! 예비 서버로 즉시 전환합니다.")
            img_url = "https://source.unsplash.com/random/1080x1920/?abstract"
            r = requests.get(img_url)
            with open("temp.jpg", "wb") as f: f.write(r.content)
        print("✅ 이미지 부품 조달 완료")

        # 3. 최종 영상 조립
        audio = AudioFileClip("voice.mp3")
        clip = ImageClip("temp.jpg").set_duration(audio.duration)
        clip = clip.set_audio(audio)
        
        # 파일 저장 (품질과 호환성을 모두 잡은 설정)
        clip.write_videofile("shorts_promo.mp4", fps=24, codec="libx264", audio_codec="aac")
        print("🎬 [수리공 보고] 무사히 영상을 제작하여 보관함에 넣었습니다!")
        
    except Exception as e:
        print(f"🚨 치명적 에러 발생: {e}")
        exit(1) # 기계에 에러 신호를 보내 '재시도 수리공'을 호출함

if __name__ == "__main__":
    asyncio.run(smart_repair_factory())
