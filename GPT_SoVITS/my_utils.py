import ffmpeg
import numpy as np
import os

def load_audio(file, sr):
    try:
        # https://github.com/openai/whisper/blob/main/whisper/audio.py#L26
        # This launches a subprocess to decode audio while down-mixing and resampling as necessary.
        # Requires the ffmpeg CLI and `ffmpeg-python` package to be installed.
        file = (
            file.strip(" ").strip('"').strip("\n").strip('"').strip(" ")
        )  # 防止小白拷路径头尾带了空格和"和回车'
        # print("filename:", file)
        # filepath =  os.path.join(os.getcwd(), file)
        # print("filepath:", filepath)
        # if os.path.exists(filepath):
        #     print("文件存在")
        # else:
        #     print("文件不存在")
        out, _ = (
            ffmpeg.input(file, threads=0)
            .output("-", format="f32le", acodec="pcm_f32le", ac=1, ar=sr)
            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
        )

    except Exception as e:
        # raise RuntimeError(f"Failed to load audio: {e}")
        raise e

    return np.frombuffer(out, np.float32).flatten()
