import whisper
import os

model = whisper.load_model("medium.en")
file = "DuaLipa.mp4"
file_name = file.split(".")[0]

if not os.path.exists(file_name):
    os.mkdir(file_name)

result = model.transcribe(file)
print(result["text"])
writer =  whisper.utils.get_writer("all","./"+file_name)
writer(result,"text")