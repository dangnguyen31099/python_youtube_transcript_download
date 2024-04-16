import time
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi

# # videos = scrapetube.get_channel(channel_username="ConsultingSuccessTV")
videos = scrapetube.get_playlist("PLMD8Cy6nrXPNAFJGmWHHnSRfx1rwK_II_")

for video in videos:
    name_file = f"{video["videoId"]} - {video["title"]["runs"][0]["text"]}.txt"
    try:
        transcripts = YouTubeTranscriptApi.get_transcript(
            video_id=video["videoId"], languages=["en"]
        )
        with open("./PLMD8Cy6nrXPNAFJGmWHHnSRfx1rwK_II_/"+ name_file.replace("/", "___"), mode="w") as file:
            for script in transcripts:
                file.write(str(script)+"\n")
        print(name_file)
    except:
        with open("./error/PLMD8Cy6nrXPNAFJGmWHHnSRfx1rwK_II_/"+ name_file.replace("/", "___"), mode="w") as file:
            file.write("")
        print("Loi:" + name_file)

    time.sleep(1)


transcripts = YouTubeTranscriptApi.get_transcript(
    video_id="ebZB8dPrrog", languages=["en"], preserve_formatting=True
)

# transcript_list = YouTubeTranscriptApi.list_transcripts(video_id="ebZB8dPrrog")
# transcript = transcript_list.find_transcript(["en"])
# translated_transcript = transcript.translate("vi")
# print(translated_transcript.fetch())
