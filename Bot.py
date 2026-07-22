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
        text = msg.get("text", "")

        # إذا المستخدم دز /start
        if text == "/start":
          user = msg["from"]
          first_name = user.get("first_name", "بدون اسم")
          user_id = user.get("id")
          username = (
              f"@{user.get('username')}" if user.get("username") else "لا يوجد يوزر"
          )

          # 1. رسالة ترحيبية
          send_message(
              chat_id, "أهلاً بك! تفضل هذه هي المقاطع والصور الخاصة بك 🎬🔥"
          )

          # 2. قائمة الملفات (فيديوهات وصور مرتبة حسب ما دزيتها)
          media_list = [
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBa2pgHszkwStiiaFU9R8suI8PEr22AAKfuQAC11H4SrMrUH6Y9N9aPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBbGpgHsz52BPd9a3fmYD_mKx3EdLKAAJWoAACELoBS2nK932kgygMPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBbWpgHszYhhZKxFL3VxTi-nYn3tvHAAKguQAC11H4SvobAAHEtJJ3Dz0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBbmpgHswWtUCQ-maLZsRIwGoc8gklAAJXoAACELoBS6SAyc-OFmLYPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBb2pgHsxJYwMAAWXI-F3_1n9hcQ7k8QACm7kAAtdR-EqyxeyXIQiZHz0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBcGpgHsx-jTnTrXLgVie3rNs7bwABLgACWaAAAhC6AUsJifHPuKh74D0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBcWpgHsyTZ4XqH5npok_KgiUELW0PAAKcuQAC11H4Sv6NEaBZOlbAPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBcmpgHsydKR6AwEDIchAHiDHNR9BzAAJaoAACELoBS8E8I4fpLlRMPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBc2pgHsypCp_w_nwWy9cqPEUXCD6BAAKauQAC11H4Sq6kBiOxzN-JPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBdGpgHszrHn2kWnKRy3YZewy5sIyeAAJeoAACELoBSygE2JBQ5ZCVPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBdWpgHsxoyV2K43BM26DKjq3ohAXFAAJwuQAC11H4Sj_m7bEmNJ1OPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBdmpgHswFYpcWZp93HALMbwrMrX8yAAJWG2sbELoBS5J22ijTkhJMAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBd2pgHszH1zdqdEgl5Ke83Fdee1bbAAJYG2sbELoBSx711lD1HC7gAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBeGpgHsw1hs9q47a5qnFCgQ3d9XJdAAKaHWsb11H4Si5Pr6EdvfCbAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBeWpgHsyqjyTBNkWb9-4P3LYbSmNhAAJZG2sbELoBS9082CqiyaQFAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBempgHsytXQ9Zg55QpTovLlbmsdYNAAJXG2sbELoBSyKtKU7Gl-8ZAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBe2pgHsweHHaP4J75jNLaPUJ5BDIHAAJuuQAC11H4SlQBtJzKnJaiPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBfGpgHswX3WSdAnMrLsfLms46hlsAA1sbaxsQugFLnjJJmvhRWcQBAAMCAAN5AAM9BA"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBfWpgHswhWcExSnGgq0tsIPgBMRY_AAKZHWsb11H4SgwvZnRLw8buAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBfmpgHsy5BOZg6MM1owABK4mdYJluzAACXBtrGxC6AUvOtURCUHxWRAEAAwIAA3kAAz0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBk2pgHt4nvdBdEhAZB5_u1o8aN0SyAALanwACELoBS9kGZYwzf2cyPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBlGpgHt4h8UnwzF74lhjXZ4uoARDKAAJYoAACELoBS1ypsfWnTLupPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBlWpgHt4J-LFybeDcqd5q8MUmJ8IGAAJ1uQAC11H4Sj_MeiCNw-ZvPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBlmpgHt7FKJjDiw2-RxRv4W4WlkyjAAJboAACELoBS36LjjszoFM-PQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBl2pgHt6bMdU-76RfX-doKjiVEkBtAAJ5uQAC11H4SryQYsZPhymVPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBmGpgHt6lcBQh8uqRR2wAAf1rPy4bXgACYaAAAhC6AUu_wK1flKKd6T0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBmWpgHt7ZOOJj1M2rgg--3KMtxdIiAAJ0uQAC11H4Suzt6h-_DFrgPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBmmpgHt4FWGlAQMxp71W3hJxtuCacAAJkoAACELoBS7kMi9ZAMh5nPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBm2pgHt5sVKAUjNvRpdzjfp8MecAMAAJvuQAC11H4Su6N4UsD-hiOPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBnGpgHt6rLfC2NvE1XGA9e_m7MYBoAAJmoAACELoBS1GLW5heO3AnPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBn2pgHuD651i1XfIfZ_GqWbl574IkAAKWHWsb11H4SpJnGqja6aftAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBoGpgHuA10bjF6LHZLozh-WCwOy1OAAKTHWsb11H4SpQR5z8AASNgVgEAAwIAA3kAAz0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBoWpgHuAcCXuWmuobyYRaBvCQfUKPAAJtuQAC11H4SmYR9ijtKNw7PQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBompgHuDd8FGTq2NR4smwcfnImdhDAAJcoAACELoBS1YT0J5URQLgPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBo2pgHuDh9E-FApDcxiv2RcE69vMyAAJruQAC11H4SqaDAAH2dC_Y8T0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBpGpgHuAgAz1-al9vCq86vx_EIuO6AAJioAACELoBS6DqQ0kbN5utPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBpWpgHuCfCrhWC5PmqAeMvyeF0Y0EAAKVHWsb11H4SrYNJgMPNstJAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBpmpgHuBgZH8IoyAxHiFElNahhi67AAJdG2sbELoBS8bYG8VuCh91AQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBqGpgHuASSbeN4EIPs15uI1sz2KSTAAJeG2sbELoBS6tjOucWBdXeAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBsWpgHuQNZ6u0G8MFN2NArqm1Af-NAAKRHWsb11H4SvjTlRxwFa0NAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBsmpgHuQ7x_mTEsD-SHRdDnJ9PsAdAAJaG2sbELoBS7bsiH9HdUdLAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBs2pgHuTHG8GiftY89NcX-hzjVaNVAAKQHWsb11H4SiosWzzvieIwAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBtGpgHuRQLizVXcWcyq3EeNMNiIoIAAJfoAACELoBS4BrR8IshWriPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBtWpgHuSoGiLPQUkBY3VOOS9K0wGOAAJouQAC11H4ShMzNbQ2rbJSPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBtmpgHuShBa3xq5Os_THobJ35IlwNAAJloAACELoBS14heMcQs-LbPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBt2pgHuTgpVHbGYevC_yoVqRz9CYjAAJmuQAC11H4SkeLHrBrnW8CPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBuGpgHuTnXgg6tQYvJK_0YzG3aYE-AAJfG2sbELoBS_kP0jVN8DoYAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "photo",
                  "id": (
                      "AgACAgIAAxkBAAIBuWpgHuRyKAN_h5La4iY1Zk3h46c3AAKNHWsb11H4SisOuiJqucpHAQADAgADeQADPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBumpgHuSgmN2VwvfAOCNT3_DKb8A_AAJpoAACELoBS2A9uAwHPUM6PQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBu2pgHuR0LgABKu0AAcXcbWgkvbLqPzQAAmS5AALXUfhKVZSiosJ3EwABPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBvGpgHuSPShJNa_qlfAxOM6lOrBlwAAJdoAACELoBS4wsqmdf15UKPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBvWpgHuQkngeBqqdWp8oth9-qrwV7AAJiuQAC11H4Ssw-66fpOnYUPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBvmpgHuQBgbti8eUDM2YQIYG6SK9jAAJjoAACELoBS_8HJpm4DyXAPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBv2pgHuQmX4VW8IMtuWHC4K4dAAFvXwACX7kAAtdR-Eol3UCT7I9kXT0E"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBwGpgHuQ7p-HkMvRcQNHjWtpvZtt9AAJnoAACELoBS0uSwQnce1vUPQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBwWpgHuRu7LnBeOzz710a1Vqh25-3AAJeuQAC11H4Sn6_eL6lsMS0PQQ"
                  ),
              },
              {
                  "type": "video",
                  "id": (
                      "BAACAgIAAxkBAAIBwmpgHuQNBegYgKuZJGPVxQcAAfdnYQACaKAAAhC6AUtEEqs9f3CX7z0E"
                  ),
              },
          ]

          # إرسال الملفات واحد ورا اللخ بانتظام
          for item in media_list:
            if item["type"] == "video":
              send_video(chat_id, item["id"])
            elif item["type"] == "photo":
              send_photo(chat_id, item["id"])
            time.sleep(0.6)  # فاصل زمني حتى ما يصير ضغط وتوصل كلها مرتبة

          # 3. إشعار للأدمن
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
