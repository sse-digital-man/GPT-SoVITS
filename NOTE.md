# 环境配置
关于环境配置参考：[请问如何将本项目作为git submodule供其他项目使用？ · Issue #1082 · RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS/issues/1082)
`conda create -n GSV python=3.10`
`conda install ffmpeg cmake`
`conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia`
`pip install -r requirements.txt`

# 前置工作
1. 需要新建SoVITS_weights和GPT_weights两个文件夹并将对应的模型放入
2. 需要在GPT_SoVITS/pretrained_models中放入对应的模型
3. 修改config.py文件和api.py文件指定模型和参考音频路径、参考音频文字、参考语言
4. 需要新建reference文件夹放入音频
5. 运行api.py文件即可

# 注意事项
使用subprocess还可能会缺失：
1. nvrtc-builtins64_118.dll需要将其放入对应的conda环境中的anaconda3\envs\your_env\Lib\site-packages\torch\lib中
2.本机必须装有ffmpeg

# 运行
WebUI: `python webui.py`
WebAPI:`python api.py`

# Docker
pull image: `docker pull kingkia/gsv-api`
run: `docker run -it --gpus=all --env=is_half=False --volume=D:\GSV\GPT-SoVITS\output:/workspace/output --volume=D:\GSV\GPT-SoVITS\logs:/workspace/logs --volume=D:\GSV\GPT-SoVITS\SoVITS_weights:/workspace/SoVITS_weights --volume=D:\GSV\GPT-SoVITS\GPT_weights:/workspace/GPT_weights --volume=D:\GSV\GPT-SoVITS\reference:/workspace/reference --workdir=/workspace -p 9880:9880 -p 9871:9871 -p 9872:9872 -p 9873:9873 -p 9874:9874 --shm-size="16G" --name gpt-sovits-api -d kingkia/gpt-sovits-api`
> 根据需要修改volume路径，必须写的包括SoVITS_weights、GPT_weights、reference