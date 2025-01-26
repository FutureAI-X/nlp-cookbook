from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result_single = classifier("I love this course")
print(result_single)

result_multi = classifier(["I love this course", "I do not like cake"])
print(result_multi)
