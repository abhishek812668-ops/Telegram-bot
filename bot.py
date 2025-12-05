from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import time
import threading
import os

# ==============================
# 🔹 BOT CONFIG
# ==============================
TOKEN = "8573280925:AAHlT2QIZTvFbFyV4YgGR56cuz_-4ld-Yy4"
CHAT_ID = -1002659872445  # Apna group chat ID
BASE_PATH = r"C:\Users\proje.PC\Downloads\Telegram Desktop"

# ==============================
# 🔹 MESSAGES WITH IMAGES
# ==============================
MESSAGES = [
    (
        "19:40",
        """👍👍👍👍👍👍👍👍👍

👉 Win Up To ₹9999 Daily on WR777! 🎉

🌟 Spin the lucky wheel every day and win exciting cash rewards — up to ₹9999 in a single spin! 🌟

✅ Daily chances 🎯
✅ Multiple prize levels 🎁
✅ Big rewards, instant wins 🪙

💎 Why everyone loves WR777:
✅ 100% Safe 🔓 
✅ Fast Deposit/Withdrawal ⚡️
✅ 24/7 Online Support ⏰

🚩 Start spinning for BIG rewards! 💌

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-01_21-37-31.jpg")
    ),

    (
        "19:41",
        """🎉GET ₹500 FREE on 🚩🚩🚩‼️

Spin the Lucky Wheel and win exciting cash rewards instantly!

🎰 Feeling Lucky?
Join WR777 today and enjoy 1️⃣ Free Spin — win up to ₹500 on the spot!
Every spin gives you a chance to grab cash, coins, or bonus rewards!

🔥 How to Get Your Free ₹500:
1️⃣ Register on WR777
2️⃣ Use your FREE SPIN
3️⃣ Win cash instantly
4️⃣ Invite friends to earn more!

✅ Free Spin Rewards
✅ Up to ₹500 Free
✅ 100% Safe & Trusted
✅ Fast Deposit/Withdrawal
✅ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMraTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-10-51.jpg")
    ),

    (
        "19:42",
        """🏦 Bank Delay? Don’t Worry — WR777 Pays You! 💰

WR777 offers up to ₹399 compensation whenever your bank withdrawal is delayed.

💰 Compensation Chart (Based on delay & withdrawal amount):
🛡 ₹100–₹999 → ₹9 / ₹19 / ₹39
🛡 ₹1000–₹4999 → ₹19 / ₹39 / ₹99
🛡 ₹5000–₹50000 → ₹99 / ₹199 / ₹399

☄️ Fast Deposit & Withdrawal
🔒 100% Safe
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-15-53.jpg")
    ),

    (
        "19:43",
        """💰 Get High Bonuses on Your First Deposit! 💰

Make your first deposit on WR777 and receive instant rewards up to ₹5777! 🎁

💰 Bonus Examples:
💱 Deposit ₹100 → Get ₹37
💱 Deposit ₹1000 → Get ₹177
💱 Deposit ₹5000 → Get ₹777
💱 Deposit ₹50000 → Get ₹5777 

✔️ Fast Deposit & Withdrawal 💥
✔️ 100% Safe & Trusted 🆒
✔️ 24/7 Online Support ⏰

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-18-08.jpg")
    ),

    (
        "19:44",
        """🔔 Free Bonus ₹188 — Just Share on Social Media! 🔔

📲 Share WR777 and get a free ₹188 bonus! ✅

⏰ How to Claim:
➡️ Share → Wait 2 hours → Contact Customer Service
➡️ You can claim once every day
➡️ Activity Time: 08:00 - 22:00

💎 100% Safe
🌟 Fast Deposit/Withdrawal
🕒 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-49-14.jpg")
    ),

    (
        "19:45",
        """🔔 Enjoy Bonus on Every Deposit! 💱

Deposit anytime on WR777 and get an instant extra bonus added to your balance — unlimited times!

💰 More deposits = more bonus
⚡️ Fast Deposit & Withdrawal
🔓 100% Safe & Trusted
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-55-08.jpg")
    ),

    (
        "19:46",
        """⭐⭐ Easy UPI Deposit Guide (WR777)

Follow these 4 simple steps to deposit quickly:
1️⃣ Screenshot the QR
2️⃣ Open PhonePe → Tap Scan
3️⃣ Select Upload QR → Choose your screenshot
4️⃣ Complete payment → Copy the UPI Ref No and submit

💯 100% Safe
💎 Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-56-47.jpg")
    ),

    (
        "19:47",
        """👑 Unlock Elite VIP Rewards at WR777! 👑

🎆 Level up your tier and enjoy weekly bonuses, upgrade rewards, and free daily withdrawals — up to ₹59,999 when you reach VIP!

✅ VIP Benefits Include:
➡️ Weekly Bonus up to ₹1,777
➡️ Level Upgrade Bonus up to ₹59,999
➡️ Free Withdrawals: 2–10 times daily
➡️ Exclusive Monday VIP Rewards

🔒 100% Safe
☄️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_21-59-55.jpg")
    ),

    (
        "19:47",
        """🔗 Invite Friends & Earn Up to ₹15,000/Month! ✨

Earn money daily just by sharing your WR777 invite link! 🎁

💸 Rewards:
🟠 You get ₹50 per invite
🟠 Your friend gets ₹20
🟠 Up to 10 invites/day = ₹500 daily

📌 How to Join:
1️⃣ Register on WR777 📲
2️⃣ Share your invite link 😀
3️⃣ Friend registers + deposits ₹100 🎉

Rewards credited instantly

🔒 💯 Safe | ⚡ Fast Withdrawal | ⏰ 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_22-35-12.jpg")
    ),

    (
        "19:48",
        """🔗 Become an Agent & Start Earning with WR777! 💎

🔔 Build your own team and earn commissions from 3 levels of sub-agents — bigger network = bigger income!

💼 Commission Rates:
✅ LV1 Subordinates: 0.30% – 0.70%
✅ LV2 Subordinates: 0.15% – 0.25%
✅ LV3 Subordinates: 0.07% – 0.15%

➡️ Earn daily, weekly, monthly passive income with zero investment!

🔓 100% Safe
⚡️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=UMTJ7PS
""",
        os.path.join(BASE_PATH, "photo_2025-12-02_22-36-17.jpg")
    ),


]

# ==============================
# 🔹 AUTO MESSAGE SENDER
# ==============================
def auto_sender(bot):
    last_sent = {}
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for send_time, msg, photo in MESSAGES:
            if now == send_time and last_sent.get(send_time) != now:
                try:
                    if os.path.exists(photo):
                        with open(photo, "rb") as f:
                            bot.send_photo(chat_id=CHAT_ID, photo=f, caption=msg)
                        print(f"Sent photo at {now}: {photo}")
                    else:
                        print(f"Photo not found, sending text only: {photo}")
                        bot.send_message(chat_id=CHAT_ID, text=msg)
                except Exception as e:
                    print("IMAGE SEND ERROR:", e)
                    bot.send_message(chat_id=CHAT_ID, text=msg)
                last_sent[send_time] = now
        time.sleep(20)

# ==============================
# 🔹 START COMMAND
# ==============================
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is running and scheduled messages are active!")

# ==============================
# 🔹 BOT STARTER
# ==============================
def start_bot():
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))

    threading.Thread(
        target=auto_sender,
        args=(updater.bot,),
        daemon=True
    ).start()

    print("Bot is starting...")
    updater.start_polling()
    updater.idle()

# ==============================
# 🔹 MAIN
# ==============================
if __name__ == "__main__":
    start_bot()

