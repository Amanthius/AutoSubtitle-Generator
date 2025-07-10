from moviepy  import VideoFileClip
"""创建语音识别客户端"""
from aip import AipSpeech
APP_ID = "xxxxx"
API_KEY = "xxxxxxxxxxxxx"
SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx" 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

video = VideoFileClip("/Users/蓝桉/Desktop/srt字幕配置/大话西游.mp4")

audio = video.audio

audio.write_audiofile("/Users/蓝桉/Desktop/srt字幕配置/大话西游.wav")
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which

# 显式指定 ffmpeg 的路径
AudioSegment.converter = which("ffmpeg")

from pydub import AudioSegment

sound = AudioSegment.from_wav("/Users/蓝桉/Desktop/srt字幕配置/大话西游.wav")
sound = sound.set_frame_rate(16000)
sound = sound.set_channels(1)

from pydub.silence import split_on_silence


# 使用split_on_silence()切分音频，并传入参数sound,min_silence_len = 500,silence_thresh = -50
min_silence_len = 500
silence_thresh = -50
pieces = split_on_silence(sound,min_silence_len,silence_thresh)

count = 0

for i in pieces:
    path = "/Users/蓝桉/Desktop/srt字幕配置/音乐片段"+str(count)+".wav"
    i.export(path,format = "wav")
    count += 1
print(count)
def read_file(filePath):
    with open(filePath,"rb") as fp:
        wavsample = fp.read()
        return wavsample

"""语音识别函数"""
def audio2text(wav):
    rejson = client.asr(wav,"wav",16000,{"dev_pid": 1537})
    if rejson["err_no"] == 0:
        msg = rejson["result"][0]
    else:
        msg = "语音识别错误！"
    return msg


for i in range(count):
    wavsample = read_file("/Users/蓝桉/Desktop/srt字幕配置/音乐片段"+str(i)+".wav")
    text = audio2text(wavsample)
    print(text)
    
    
"""获取时间数据"""
from pydub.silence import detect_nonsilent
timestamp_list = detect_nonsilent(sound,min_silence_len, silence_thresh)

"""获取srt字幕文件标准时间格式"""
def getTime(t):
    spart,mspart = divmod(t,1000)
    mpart,spart = divmod(spart,60)
    hpart,mpart = divmod(mpart,60)
    mspart=str(mspart).zfill(3)
    spart=str(spart).zfill(2)
    mpart=str(mpart).zfill(2)
    hpart=str(hpart).zfill(2)
    stype = hpart+":"+mpart+":"+spart+","+mspart
    return stype

"""生成标准字幕"""
def getsrt(sn,start_time,end_time,text):
    srt_text = str(sn)+"\n"+start_time+" --> "+end_time+"\n"+text+"\n"+"\n"
    return srt_text

"""写入srt字幕文件"""
def writesrt(srtpath,srt):
    with open(srtpath,"a") as fp:
        fp.write(srt)

count = 0
for i in timestamp_list:
    wavsample = read_file("/Users/蓝桉/Desktop/srt字幕配置/音乐片段"+str(count)+".wav")
    text = audio2text(wavsample)
    symbol = ["，","。","！","？"]
    for j in symbol:
        text = text.replace(j," ")
    srttext = getsrt(count,getTime(i[0]),getTime(i[1]),text)
    path = "/Users/蓝桉/Desktop/srt字幕配置/大话西游.srt"
    writesrt(path,srttext)
    count +=1

import chardet
def convert_to_utf8(input_file, output_file):
    with open(input_file, 'rb') as f:
        raw_data = f.read()
        encoding = chardet.detect(raw_data)['encoding']
    
    print(f"检测到字幕文件编码为：{encoding}")
    
    with open(input_file, 'r', encoding=encoding) as f:
        text = f.read()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"字幕文件已成功转换为 UTF-8 格式：{output_file}")

convert_to_utf8("/Users/蓝桉/Desktop/srt字幕配置/大话西游.srt", "/Users/蓝桉/Desktop/srt字幕配置/大话西游.srt")
print("srt字幕文件写入成功！")

