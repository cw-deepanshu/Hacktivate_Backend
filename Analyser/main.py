
import spacy
import sys
import ast

nlp = spacy.load("en_core_web_lg")
import json
import os

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Concatenate the file name with the directory
file_path = os.path.join(current_dir, 'data.json')

with open(file_path, 'r') as f:
    data = json.load(f)

training_data = []
for example in data['examples']:
  temp_dict = {}
  temp_dict['text'] = example['content']
  temp_dict['entities'] = []
  for annotation in example['annotations']:
    start = annotation['start']
    end = annotation['end']
    label = annotation['tag_name'].upper()
    temp_dict['entities'].append((start, end, label))
  training_data.append(temp_dict)
     
from spacy.tokens import DocBin
from tqdm import tqdm

nlp = spacy.blank("en") # load a new spacy model
doc_bin = DocBin()

from spacy.util import filter_spans

for training_example  in tqdm(training_data): 
    text = training_example['text']
    labels = training_example['entities']
    doc = nlp.make_doc(text) 
    ents = []
    for start, end, label in labels:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    filtered_ents = filter_spans(ents)
    doc.ents = filtered_ents 
    doc_bin.add(doc)

doc_bin.to_disk("train.spacy") 

import os
from pathlib import Path

model_path = Path(__file__).parent / "model-best"
nlp_ner = spacy.load(model_path)
# rel_path = os.path.relpath("model-best")
# nlp_ner = spacy.load(rel_path)

from translation import get_translation

input = ast.literal_eval(sys.argv[1])
# input = ["Hindi","HindiAudio.mp4"]
lang = input[0]
language = "en"
if lang=="Hindi":
    language = "hi"
else:
    language = "en"
translation = get_translation(language,input[1])
print(translation)
doc = nlp_ner(translation)
colors = {"MAKENAME": "#F67DE3", "USERREVIEWS": "#7DF6D9", "MODELNAME": "#a6e22d"}
options = {"ents": ["MAKENAME", "USERREVIEWS", "MODELNAME"], "colors": colors}

spacy.displacy.render(doc, style="ent", options=options)

nlp = spacy.load("en_core_web_lg")
from spacy import displacy
html = displacy.render(doc, style="ent", options=options)
with open("data_vis.html", "w", encoding="utf-8") as f:
    f.write(html)