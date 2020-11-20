# /storage/emulated/0/Android/data/tv.danmaku.bili/download

# I try to write a code which can comba bilibili video cache,
# function: 
# 1. read cache dir and list cache data which user to save in app
# 2. choose a vidoe to comba and use ffmpeg to do it
import os
import sys
import json
#ji = sys.argv[1]
#path = '/storage/emulated/0/Android/data/tv.danmaku.bili/download/31634578/'+ji+'/16/'
logo ='''
-----------------------------------------
┏━┓┏━┓╻  ╻┏━┓┏━┓╻  ╻
┣━┛┃ ┃┃  ┃┣━┛┃ ┃┃  ┃
╹  ┗━┛┗━╸╹╹  ┗━┛┗━╸╹ by sparrowyang v1.0
-----------------------------------------
'''
video_list = []

video_path = []

def quality(path,js):
    q = ['16','32','64','80']
    q_text = ['_360p','_480p','_720p','_1080p']
    for i in range(0,4):
        if os.path.exists(path+q[i]):
            video_list.append(js['title']+q_text[i])
            video_path.append(path+q[i]+'/')
    

def load_data():
    main_path = '/storage/emulated/0/Android/data/tv.danmaku.bili/download/'
    dirs = os.listdir(main_path)
    for i in dirs:
        #dirss = os.listdir(main_path+i+'/'+'1')
        f = open(main_path+i+'/'+'1/'+'entry.json')
        jsdata = f.readline()
        js = json.loads(jsdata)
        quality(main_path+i+'/'+'1/',js)
        f.close()

def add(i):
    os.system("ffmpeg -i "+video_path[i]+"video.m4s -i "+video_path[i]+"audio.m4s -c:v copy -c:a aac -strict experimental /storage/emulated/0/Download/"+video_list[i]+".mp4")

def info():
    print(logo)
    index = 1
    print('选择一个视频导出：')
    print(0,' : ','取消')
    for i in video_list:
        print(index,' : ',i)
        index+=1
load_data()
info()
out_index = int(input())
if(out_index==0):
    exit()
add(out_index-1)
