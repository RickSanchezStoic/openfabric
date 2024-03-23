
## Documentation
The chatbot, that answers science based questions, comprises a simple pre-trained transformer(Roberta in this case). 
The model can be found here(https://huggingface.co/deepset/roberta-base-squad2).
The model has been pre-trained on SQUAD2(Stanford Question Answering Dataset). The model takes question and context pair
as input. For the chatbot to function, we use wikipedia as the source for context related to the question. This allows 
the model to get accurate response for the question at hand.

