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


print("تم تشغيل البوت بنجاح! جرب دز /start للبوت...")

last_update_id = None

while True:
    updates = get_updates(last_update_id)
    if updates and updates.get("ok"):
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1

            if "message" in update and "text" in update["message"]:
                msg = update["message"]
                text = msg.get("text", "")

                if text == "/start":
                    user = msg["from"]
                    first_name = user.get("first_name", "بدون اسم")
                    user_id = user.get("id")
                    username = (
                        f"@{user.get('username')}"
                        if user.get("username")
                        else "لا يوجد يوزر"
                    )

                    # 1. رد للمستخدم
                    send_message(
                        user_id, "أهلاً بك! تم تسجيل دخولك بنجاح. 👋"
                    )

                    # 2. إشعار للأدمن
                    profile_link = f"tg://user?id={user_id}"
                    admin_msg = (
                        f"🚨 **مشترك جديد دخل البوت!**\n\n"
                        f"👤 **الاسم:** {first_name}\n"
                        f"🆔 **الـ ID:** `{user_id}`\n"
                        f"🔗 **اليوزر:** {username}\n\n"
                        f"👉 [اضغط هنا للدخول لبروفايل الشخص مباشرة]({profile_link})"
                    )
                    send_message(ADMIN_ID, admin_msg)

    time.sleep(1)


    time.sleep(1)
