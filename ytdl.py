import sys
import subprocess

def main():
    
    user = input("URL? ")
  

    try:
        subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", "~/ADHD/music/%(uploader)s/%(title)s.%(ext)s","--audio-quality", "0", "--embed-thumbnail", "--embed-metadata", "--parse-metadata", "%(uploader)s:%(meta_artist)s", "--parse-metadata", "%(title)s:%(meta_album)s" , user ], check=True)
        print("Download successful! YIPEE!! :) ")

    except FileNotFoundError:
        print("Please make sure you have yt-dlp installed :) ")

    except subprocess.CalledProcessError:
        print("Download failed, check your URL maybe :0? ")
    
    

if __name__ == "__main__":
    main()