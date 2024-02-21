# install cmd -> pip install yt_dlp
import yt_dlp as youtube_dl
import time

url = input("Youtube Video Link/Playlist link:")

ydl_opts = {}

start_time = time.time()

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download successful!")
except youtube_dl.DownloadError as e:
    print("Error downloading video:", e)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")
