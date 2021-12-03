# from rgb_yuv import rgb_to_yuv
import os

# f5 to run
if __name__ == '__main__':

    option=0
while not option==5:

    print("1. Convert videos into VP8, VP9, h265 i AV1")
    print("2. Compare two video codecs")
    print("3. Streaming a video in an IP address")
    print("4. Streaming a video in an IP address choosen")
    print("5. Exit \n")
    option = int(input("Option: "))

    if option == 1:
        print("#Convert videos into VP8, VP9, h265 i AV1 \n")
        print("1. 720p")
        print("2. 480p")
        print("3. 360x240p")
        print("4. 160x120p")
        video_int = int(input("Video: "))
        if video_int==1:
            video = "video_720.mp4"
        elif video_int==2:
            video = "video_480.mp4"
        elif video_int==3:
            video = "video_360x240.mp4"
        elif video_int==4:
            video = "video_160x120.mp4"

        print("1. VP8")
        print("2. VP9")
        print("3. h265")
        print("4. AV1")
        encoder = int(input("Convert to: "))
        if encoder==1:
            os.system('ffmpeg -i ' + video + ' -c:v libvpx -b:v 1M -c:a libvorbis video_vp8.webm')
        elif encoder==2:
            os.system('ffmpeg -i ' + video + ' -c:v libvpx -b:v 2M -c:a libvorbis video_vp9.webm')
        elif encoder==3:
            os.system('ffmpeg -i ' + video + ' -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k video_h265.mp4 ')
        elif encoder==4:
            os.system('ffmpeg -i ' + video + ' -c:v libaom-av1 -crf 30 -b:v 0 video_av1.mkv')

    if option == 2:
        print("#Compare two video codecs")
        print("1. VP8")
        print("2. VP9")
        print("3. h265")
        print("4. AV1")
        encoder1_int = int(input("Codec 1: "))
        if encoder1_int==1:
            encoder1 = "video_vp8.webm"
        elif encoder1_int==2:
            encoder1 = "video_vp9.webm"
        elif encoder1_int==3:
            encoder1 = "video_h265.mp4"
        elif encoder1_int==4:
            encoder1 = "video_av1.mkv"

        print("1. VP8")
        print("2. VP9")
        print("3. h265")
        print("4. AV1")
        encoder2_int = int(input("Codec 2: "))
        if encoder2_int==1:
            encoder2 = "video_vp8.webm"
        elif encoder2_int==2:
            encoder2 = "video_vp9.webm"
        elif encoder2_int==3:
            encoder2 = "video_h265.mp4"
        elif encoder2_int==4:
            encoder2 = "video_av1.mkv"

        os.system('ffmpeg \
                    -i '+ encoder1 + ' \
                    -i '+ encoder2 + ' \
                    -filter_complex " \
                        [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
                        [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
                        [a0][a1]xstack=inputs=2:layout=0_0|0_h0[out] \
                        " \
                        -map "[out]" \
                        -c:v libx264 -t 30 -f matroska comparision_videos.mkv')
    if option == 3:
        print("#Streaming a video in an IP address")
        os.system('gnome-terminal -x sh -c "ffmpeg -i video_720.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000; bash"')
        os.system('ffplay udp://127.0.0.1:23000')

    if option == 4:
        print("#Streaming a video in an IP address choosen")
        ip = raw_input("Choose an IP (Example: 127.0.0.1:23000): ")
        os.system('gnome-terminal -x sh -c "ffmpeg -i video_720.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://'+ip+'; bash"')
        os.system('ffplay udp://'+ip)
