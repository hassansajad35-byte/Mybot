import json
import ssl
import time
import urllib.parse
import urllib.request

# تجاوز فحص شهادات الأمان SSL
ssl._create_default_https_context = ssl._create_unverified_context

TOKEN = "8867161129:AAGUkmjunno2ZNCGB0puWsCa5AghJLiSZAM"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"


def send_message(chat_id, text):
  url = BASE_URL + "sendMessage"
  payload = urllib.parse.urlencode(
      {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
  ).encode("utf-8")
  try:
    req = urllib.request.Request(url, data=payload)
    urllib.request.urlopen(req)
  except Exception as e:
    print("خطأ:", e)


def get_updates(offset=None):
  url = BASE_URL + "getUpdates?timeout=30"
  if offset:
    url += f"&offset={offset}"
  try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
      return json.loads(response.read().decode("utf-8"))
  except Exception as e:
    return None


print("بوت استخراج المعرفات يعمل...")
last_update_id = None

while True:
  updates = get_updates(last_update_id)
  if updates and updates.get("ok"):
    for update in updates.get("result", []):
      last_update_id = update["update_id"] + 1

      if "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]

        # إذا دزيت فيديو، صورة، أو ملف للبوت
        if "video" in msg or "photo" in msg or "document" in msg:
          file_id = ""
          file_type = ""
          if "video" in msg:
            file_id = msg["video"]["file_id"]
            file_type = "فيديو"
          elif "photo" in msg:
            file_id = msg["photo"][-1]["file_id"]
            file_type = "صورة"
          elif "document" in msg:
            file_id = msg["document"]["file_id"]
            file_type = "ملف"

          # البوت راح يرجع يدزلك المعرف برسالة
          send_message(
              chat_id,
              f"✅ تم استلام ال{file_type} بنجاح!\n\nمعرف الملف (File ID):\n`{file_id}`",
          )

  time.sleep(1)
