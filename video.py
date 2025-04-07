import os
import whisperx

# 参数设置
device = "cuda"
batch_size = 16  # 减少如果GPU内存不足
compute_type = "float16"  # 改为"int8"如果GPU内存不足（可能降低准确性）

# 加载模型
model = whisperx.load_model("large-v2", device, compute_type=compute_type)
diarize_model = whisperx.DiarizationPipeline(use_auth_token="#huggingface Token", device=device)

def format_time(seconds):
    """
    将秒数转换为 SRT 时间格式 HH:MM:SS,mmm。
    """
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def write_srt(segments, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments, start=1):
            start_time = format_time(segment['start'])
            end_time = format_time(segment['end'])
            speaker_label = f"Speaker {segment['speaker']}" if 'speaker' in segment else "Unknown Speaker"
            text = segment['text'].strip()
            
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{speaker_label}: {text}\n\n")

# 处理文件夹中的所有MP4文件
video_folder = "/root/autodl-tmp/.autodl/mp4"

for video_filename in os.listdir(video_folder):
    if video_filename.endswith(".mp4"):
        video_path = os.path.join(video_folder, video_filename)
        
        # print(f"Processing {video_filename}...")
        print(video_path)
        
        # 转录音频
        audio = whisperx.load_audio(video_path)
        result = model.transcribe(audio, batch_size=batch_size)
        # print(result["segments"])  # 转录前的结果
        
        # 对齐输出
        language_code = result["language"]
        model_a, metadata = whisperx.load_align_model(language_code=language_code, device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
        # print(result["segments"])  # 对齐后的结果
        
        # 分配说话者标签
        diarize_segments = diarize_model(audio)
        result = whisperx.assign_word_speakers(diarize_segments, result)
        # print(diarize_segments)
        # print(result["segments"])  # 包含说话者ID的段落
        
        # 生成SRT文件
        srt_filename = os.path.splitext(video_filename)[0] + ".srt"
        srt_path = os.path.join(video_folder, srt_filename)
        write_srt(result["segments"], srt_path)
        # print(f"SRT file has been saved to {srt_path}")

print("All videos have been processed.")
