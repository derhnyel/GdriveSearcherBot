import os

BOT_TOKEN = os.envrion.get("BOT_TOKEN", "bot_token")
API_ID = int(os.envrion.get("API_ID", 12345678))
API_HASH = os.envrion.get("API_HASH", "hash")
RESULTS_COUNT = int(os.envrion.get("RESULTS_COUNT", 4)  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001485393652 -1005456463651").split()))

DRIVE_NAME = [
    "Root",  # folder 1 name
    "Cartoon",  # folder 2 name
    "Course",  # folder 3 name
    "Movies",  # ....
    "Series",  # ......
    "Others"  # and soo onnnn folder n names
]

DRIVE_ID = [
    "1B9A3QqQqF31IuW2om3Qhr-wkiVLloxw8",  # folder 1 id
    "12wNJTjNnR-CNBOTnLHqe-1vqFvCRLecn",  # folder 2 id
    "11nZcObsJJHojHYg43dBS0_eVvJrSD7Nf",  # and so onn... folder n id
    "10_hTMK8HE8k144wOTth_3x1hC2kZL-LR",
    "1-oTctBpyFcydDNiptLL09Enwte0dClCq",
    "1B9A3QqQqF31IuW2om3Qhr-wkiVLloxw8"
]

INDEX_URL = [
    "https://dl.null.tech/0:",  # folder 1 index link
    "https://dl.null.tech/0:/Cartoon",  # folder 2 index link
    "https://dl.null.tech/0:/Course",  # and soo on folder n link
    "https://dl.null.tech/0:/MOVIES",
    "https://dl.null.tech/0:/Series",
    "https://dl.null.tech/0:/Roms"
]
