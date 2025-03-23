import time
import os
from datetime import datetime
from instagrapi import Client

# Instagram Login Credentials
USERNAME = "<username>"
PASSWORD = "<password>"

# Initialize Instagrapi Client
cl = Client()
cl.login(USERNAME, PASSWORD)

# Directory containing reels
REELS_DIR = "/videos"

# Start from output1.mp4 and continue sequentially
part_number = 1

# Scheduled posting times (24-hour format)
SCHEDULED_TIMES = ["03:00", "09:00", "15:00", "21:00"]

def wait_for_next_schedule():
    """Wait until the next scheduled posting time."""
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in SCHEDULED_TIMES:
            return  # Proceed with posting
        time.sleep(30)  # Check every 30 seconds

while True:
    video_file = f"{REELS_DIR}/output{part_number}.mp4"
    next_file = f"{REELS_DIR}/output{part_number + 1}.mp4"

    # If the current video file does not exist, stop the loop
    if not os.path.exists(video_file):
        print("✅ All available reels have been uploaded.")
        break

    # Check if next file exists
    if os.path.exists(next_file):
        upcoming_line = f"\n\n Upcommming Part {part_number + 1}! "
    else:
        upcoming_line = ""  # No next part, remove the upcoming line

    # Caption with dynamic part number
    CAPTION = f"""Part {part_number} {upcoming_line}"""

    # Wait for the next scheduled time before uploading
    wait_for_next_schedule()

    # Upload Video
    try:
        cl.clip_upload(video_file, CAPTION)
        print(f"✅ Uploaded: {video_file}")
        # Sleep for 60 seconds after posting to prevent duplicates
        time.sleep(60)
    except Exception as e:
        print(f"❌ Failed to upload {video_file}: {e}")

    # Move to the next part
    part_number += 1
