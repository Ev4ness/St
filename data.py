from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Mulai Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Kembali", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Update", url="https://t.me/SpotifyStreamMusic")],
        [
            InlineKeyboardButton("Bantuan", callback_data="help"),
            InlineKeyboardButton("Info Bot", callback_data="about")
        ],
        [InlineKeyboardButton("Developer", url="https://t.me/Usern4meDoesNotExist404")],
    ]

    START = """
Hallo {}
nama saya adalah {}
jika Anda tidak mempercayai bot ini!
──────────────────────
1) berhenti membaca pesan ini
2) hapus obrolan ini dan blokir bot
──────────────────────
kamu dapat menggunakan saya untuk menghasilkan sesi string Pyrogram dan Telethon. gunakan tombol di bawah ini untuk memulai!
    """

    HELP = """
**📝 Semua Printah** 

/about - Tentang Bot
/help - Bantuan
/start - Mulai Bot
/generate - Ambil Session 
/cancel - Batalkan Proses
/restart - Mulai Ulang Bot
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @StarkProgrammer
    """
