# Instagram Reels Scheduler

## Overview
This Python script automates the process of posting Instagram Reels at predefined scheduled times using the `Instagrapi` library. It allows for sequential posting of video files from a specified directory.

## Features
- **Automated Posting**: Uploads reels sequentially.
- **Scheduled Uploads**: Posts videos at specific times.
- **Error Handling**: Prevents duplicate uploads and handles failures gracefully.

## Installation
Ensure Python is installed, then install the required package:

```bash
pip install instagrapi
```

## Usage
1. Store all reels in a designated folder.
2. Ensure reels are named sequentially (`output1.mp4`, `output2.mp4`, etc.).
3. Modify the script with your Instagram **username** and **password**.
4. Adjust the scheduled times if needed.
5. Run the script:

```bash
python uploader.py
```

## Configuration
- The script will post videos in order and wait for the next scheduled time before posting.
- The `SCHEDULED_TIMES` list can be modified to change posting times.
- The script automatically stops once all videos have been uploaded.

## Notes
- Be mindful of Instagram’s policies regarding automation.
- Ensure your account has the necessary permissions to upload reels.

## License
This project is open-source under the MIT License.

---

This script is ideal for content creators looking to automate their Instagram Reels posting efficiently!

