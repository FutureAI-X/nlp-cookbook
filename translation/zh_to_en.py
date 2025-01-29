# Use a pipeline as a high-level helper
# 需要安装：pip install sentencepiece
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")

print(translator("浙江的省会是哪里"))