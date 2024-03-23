
## Documentation
The chatbot, that answers science based questions, comprises a simple pre-trained transformer(Scibert in this case). 
The model can be found here(https://huggingface.co/ixa-ehu/SciBERT-SQuAD-QuAC).
The model has been pre-trained on SQUAD2(Stanford Question Answering Dataset) as well as QuAC(Question Answering in Context. The model takes question and context pair
as input. For the chatbot to function, we use wikipedia as the source for context related to the question. This allows 
the model to get accurate response for the question at hand.

