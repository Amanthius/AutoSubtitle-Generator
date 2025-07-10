# 视频转SRT字幕自动化工具（百度API赋能）

本项目基于 Python，实现了从视频文件自动提取音频、切分音频片段、调用百度语音识别接口进行语音转文字，并自动生成标准 SRT 字幕文件的完整流程。适用于需要为视频自动生成中文字幕的场景。

## 功能特点

- **视频音频提取**：支持对 MP4 等视频文件提取音频为 WAV 格式。
- **音频切分**：基于静音片段自动将长音频切割为多个短音频片段，便于后续处理。
- **语音识别**：调用百度语音识别 API，将音频片段自动转为文字。
- **字幕时间轴自动生成**：自动获取每段音频的起止时间，精确生成 SRT 字幕时间轴。
- **SRT 文件输出**：生成标准格式 SRT 字幕文件，兼容主流视频播放器。
- **编码转换**：自动探测并转换生成的 SRT 文件编码为 UTF-8，确保兼容性。

## 快速开始

### 1. 安装依赖

建议使用 Python 3.7+，安装以下依赖：

```bash
pip install moviepy pydub baidu-aip chardet
```

请确保已安装 [ffmpeg](https://ffmpeg.org/download.html)，并配置至系统环境变量。

### 2. 配置百度语音识别

在代码中填写你自己的百度语音识别 `APP_ID`、`API_KEY`、`SECRET_KEY`。

```python
APP_ID = "你的AppID"
API_KEY = "你的ApiKey"
SECRET_KEY = "你的SecretKey"
```

### 3. 使用方法

1. 将你要处理的视频文件（如 `大话西游.mp4`）放在合适目录，并修改代码中的路径为你的实际路径。
2. 运行主程序，自动完成音频提取、切分、语音识别、字幕生成等流程。
3. 完成后，`大话西游.srt` 字幕文件会生成在指定目录，并自动转换为 UTF-8 编码。

### 4. 部分核心流程说明

- **音频切分参数**：
  - `min_silence_len = 500` ：静音判定的最小长度，单位毫秒。
  - `silence_thresh = -50` ：静音的阈值，单位 dBFS，根据实际音频调整。

- **语音识别**：
  - 使用百度 AIP 语音识别，`dev_pid = 1537` 表示普通话。

- **字幕时间轴与文本同步**：
  - 通过 `pydub.silence.detect_nonsilent` 获取每段音频的起止时间，实现字幕与音频高度同步。

### 5. 注意事项

- 长音频或音频质量较差时，识别准确率可能降低；可适当调整切分参数。
- 百度语音识别接口有每日调用次数限制，请根据实际需求合理规划调用频率。
- 若出现编码错误，确保 ffmpeg、pydub、chardet 等依赖正确安装。

## 目录结构示例

```
/srt字幕配置/
├── 大话西游.mp4
├── 大话西游.wav
├── 音乐片段0.wav
├── 音乐片段1.wav
├── ...
├── 大话西游.srt
```

## 项目适用场景

- 视频自动加字幕
- 语音内容批量转写
- 视频后期批量处理自动化

## 参考与致谢

- [moviepy](https://github.com/Zulko/moviepy)
- [pydub](https://github.com/jiaaro/pydub)
- [Baidu AIP 语音识别](https://ai.baidu.com/tech/speech/asr)
- [chardet](https://github.com/chardet/chardet)

---

如有问题欢迎提 issue 或交流！
