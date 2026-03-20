import asyncio, edge_tts, requests, os, sys, random
from moviepy.editor import ImageClip, AudioFileClip

# [AI 두뇌] 영상 제작 핵심 함수
async def create_ai_video(text):
    print(f"\n🤖 AI 수리공: '{text}' 명령을 접수했습니다. 작업 시작!")
    
    try:
        # 1. 한국어 음성 생성 (선희 목소리)
        voice_file = "voice.mp3"
        communicate = edge_tts.Communicate(text, "ko-KR-SunHiNeural")
        await communicate.save(voice_file)
        
        # 2. 랜덤 배경 이미지 가져오기 (고화질 세로형)
        img_file = "temp_bg.jpg"
        img_url = f"https://picsum.photos/1080/1920?sig={random.randint(1, 9999)}"
        r = requests.get(img_url, timeout=15)
        with open(img_file, "wb") as f:
            f.write(r.content)

        # 3. 목소리에 맞춰 영상 조립
        audio = AudioFileClip(voice_file)
        clip = ImageClip(img_file).set_duration(audio.duration).set_audio(audio)
        
        output_name = "ai_result.mp4"
        clip.write_videofile(output_name, fps=24, codec="libx264", logger=None)
        
        print(f"✅ AI 수리공: 영상 제작 완료! 파일명: {output_name}")
        
    except Exception
