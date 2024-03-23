import os
import warnings
from typing import Dict
import wikipedia as wiki
from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from transformers import  pipeline
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass



############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    model_name = "ixa-ehu/SciBERT-SQuAD-QuAC" # change for different model
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    QA_input = {'question':"",'context':""} # dictionary with question and context as keys

    output = []
    for text in request.text:
        results = wiki.search(text) # we get context through wikipedia search
        page = wiki.page(results[0], auto_suggest=False) # getting the first result
        context = page.content
        QA_input['question'] = text
        QA_input['context'] = context
        res = nlp(QA_input)
        output.append(res['answer'])

    return SchemaUtil.create(SimpleText(), dict(text=output))
