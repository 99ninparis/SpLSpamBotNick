from pyrogram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import DEV, STUFF

START_MARKUP_STR = IKM(
               [
               [
               IKB("💭 Owner 💭", url="t.me/Asynchorous"),
               IKB("✨ Support ✨", url="t.me/The_Hades_World")
               ],
               [
               IKB("🔥 Repo 🔥", url="https://github.com/Timeisnotwaiting/EndSpamBot)
               ]
               ]
               )

START_MARKUP_DEV = IKM(
               [
               [
               IKB("💫 Commands 💫", callback_data="cmds"),
               IKB("💭 Support 💭", url="t.me/The_Hades_World")
               ]
               ]
               )  

async def start(_, m):
    DEV.SUDO_USERS.append(DEV.OWNER_ID)
    x = DEV.SUDO_USERS
    bot_name = "𝙀𝙣𝙙 𝙓 𝙎𝙥𝙖𝙢"
    if m.from_user.id in x:
        txt = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
        await m.reply_photo(STUFF.START_PIC, txt, START_MARKUP_DEV)
        return
    if str(m.chat.id)[0] == "-":
        return
    men = m.from_user.mention
    txt = f"**Hello !! {men}\nNice To Meet You, Well I Am {bot_name}, A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [𝙃𝙖𝙙𝙚𝙨](https://t.me/The_Hades_World)**"
    await m.reply_photo(STUFF.START_PIC, txt, reply_markup=START_MARKUP_STR)
    return

HELP_TEXT = "★ 𝙆𝙀𝙎𝙃𝘼𝙑𝙓𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"
