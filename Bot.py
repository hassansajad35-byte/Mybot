import json
import ssl
import time
import urllib.parse
import urllib.request

# تجاوز فحص شهادات الأمان SSL
ssl._create_default_https_context = ssl._create_unverified_context

TOKEN = "8867161129:AAGUkmjunno2ZNCGB0puWsCa5AghJLiSZAM"
ADMIN_ID = 1750728796

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
    print("خطأ في إرسال الرسالة:", e)


# دالة تحويل الرسائل (Forward) للأدمن
def forward_message(chat_id, from_chat_id, message_id):
  url = BASE_URL + "forwardMessage"
  payload = urllib.parse.urlencode({
      "chat_id": chat_id,
      "from_chat_id": from_chat_id,
      "message_id": message_id,
  }).encode("utf-8")
  try:
    req = urllib.request.Request(url, data=payload)
    urllib.request.urlopen(req)
  except Exception as e:
    print("خطأ في تحويل الرسالة:", e)


# دالة إرسال الفيديو
def send_video(chat_id, video_file_id):
  url = BASE_URL + "sendVideo"
  payload = urllib.parse.urlencode(
      {"chat_id": chat_id, "video": video_file_id}
  ).encode("utf-8")
  try:
    req = urllib.request.Request(url, data=payload)
    urllib.request.urlopen(req)
  except Exception as e:
    print("خطأ في إرسال الفيديو:", e)


# دالة إرسال الصورة
def send_photo(chat_id, photo_file_id):
  url = BASE_URL + "sendPhoto"
  payload = urllib.parse.urlencode(
      {"chat_id": chat_id, "photo": photo_file_id}
  ).encode("utf-8")
  try:
    req = urllib.request.Request(url, data=payload)
    urllib.request.urlopen(req)
  except Exception as e:
    print("خطأ في إرسال الصورة:", e)


def get_updates(offset=None):
  url = BASE_URL + "getUpdates?timeout=30"
  if offset:
    url += f"&offset={offset}"
  try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
      return json.loads(response.read().decode("utf-8"))
  except Exception as e:
    print("خطأ في الاتصال:", e)
    return None


print("البوت يعمل الآن ويوزع المحتوى تلقائياً عند الـ /start...")
last_update_id = None

while True:
  updates = get_updates(last_update_id)
  if updates and updates.get("ok"):
    for update in updates.get("result", []):
      last_update_id = update["update_id"] + 1

      if "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        message_id = msg["message_id"]
        text = msg.get("text", "")

        # إذا المستخدم دز /start
        if text == "/start":
          user = msg["from"]
          first_name = user.get("first_name", "بدون اسم")
          user_id = user.get("id")
          username = (
              f"@{user.get('username')}" if user.get("username") else "لا يوجد يوزر"
          )

          # 1. رسالة ترحيبية للمستخدم
          send_message(
              chat_id, "أهلاً بك! تفضل هذه هي المقاطع والصور الخاصة بك 🎬🔥"
          )

          # (قائمة الملفات مالتك تفضل تبقى هنا مثل ما هي...)
          media_list = [
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBa2pgHszkwStiiaFU9R8suI8PEr22AAKfuQAC11H4SrMrUH6Y9N9aPQQ"
                  ),
              }
              # ... باقي القائمة مالتك ...
          ]

          for item in media_list:
            if item["type"] == "video":
              send_video(chat_id, item["id"])
            elif item["type"] == "photo":
              send_photo(chat_id, item["id"])
            time.sleep(0.6)

          # 2. تحويل رسالة الـ /start مالته إلى الأدمن مباشرة (Forward)
          # هاي راح توصلك رسالة محولة من اسم الشخص وتكدر تضغط عليه وتفتح حسابه مباشرة!
          forward_message(ADMIN_ID, chat_id, message_id)

          # 3. إشعار نصي إضافي بالمعلومات (اختياري)
          admin_msg = (
              f"🚨 **مشترك جديد دخل البوت!**\n\n"
              f"👤 **الاسم:** {first_name}\n"
              f"🆔 **الـ ID:** `{user_id}`\n"
              f"🔗 **اليوزر:** {username}"
          )
          send_message(ADMIN_ID, admin_msg)

  time.sleep(1)
