import yt_dlp

# 1. ส่วนรับข้อมูล: รับ URL ของวิดีโอจากผู้ใช้งาน
url = input("กรุณาวางลิงก์ YouTube ที่ต้องการดาวน์โหลด: ")

# 2. ส่วนกำหนดค่าการดาวน์โหลด (Options)
# ในที่นี้กำหนดให้โหลดวิดีโอที่คุณภาพดีที่สุด (bestvideo+bestaudio)
ydl_opts = {
    'format': 'best', 
    'outtmpl': '%(title)s.%(ext)s', # ตั้งชื่อไฟล์ตามชื่อวิดีโอใน YouTube
}

# 3. ส่วนการดาวน์โหลด
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("กำลังเริ่มดาวน์โหลด...")
        ydl.download([url])
    print("ดาวน์โหลดเสร็จสมบูรณ์!")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")