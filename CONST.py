import os
from dotenv import load_dotenv

load_dotenv()  

# Channels
CHANNEL_join_golden_sage = 1124178305256542349
CHANNEL_minecraft_mod = 1124451026766929980
# Roles
ROLE_ID_golden_sage = 1124077481507422289
ROLE_ID_twitch_sub = 1060053953838059641
ROLE_ID_minecraft_mod = 1124450685644185620
ROLE_ID_admin = 897533247892910151
ROLE_ID_mod = 897533318663389244
# Paid roles
PAID_ROLE = [ROLE_ID_golden_sage, ROLE_ID_twitch_sub]
# Emojis
EMOJI_ADMIN = "Admin"
EMOJI_MOD = "Mod"
EMOJI_GOLDEN_SAGE = "GoldenSage"
EMOJI_FATED_CROWN = "TheFatedCrown"
EMOJI_CRACKS_COOKIE = "CracksCookie"
EMOJI_MOONFROGS_NUKE = "Nuke"

# Users
USER_ID_lockchain = os.getenv("USER_ID_lockchain")
USER_ID_moonFrogs = os.getenv("USER_ID_moonFrogs")
USER_ID_skip = os.getenv("USER_ID_skip")
USER_ID_crack = os.getenv("USER_ID_crack")
# Special Users
SPECIAL_USERS = {USER_ID_moonFrogs: {"emoji": EMOJI_MOONFROGS_NUKE},
                 USER_ID_skip: {"emoji": EMOJI_FATED_CROWN},
                 USER_ID_crack: {"emoji": EMOJI_CRACKS_COOKIE},
                 }
# Forbidden things
FORBIDDEN_FILE_TYPES = {".zip", ".tar", ".rar", ".exe", ".dll", ".so", ".a", ".jar"}

# Meme links / media
IM_IN_DANGER = "https://tenor.com/view/chuckles-im-in-danger-ralph-wiggum-the-simpsons-gif-14149962"
