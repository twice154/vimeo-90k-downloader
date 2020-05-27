import subprocess

original_video_list = open("original_video_list.txt", 'r')
original_video_list_list = []
while True:
    video_url = original_video_list.readline()
    if not video_url:
        break
    original_video_list_list.append(video_url[:-1])
original_video_list.close()

for i in original_video_list_list:
    args = "youtube-dl -i -f 'best' " + i
    subprocess.call(args, shell=True)
