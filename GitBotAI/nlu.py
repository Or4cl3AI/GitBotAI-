import pickle
import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from models.nlu_model import IntentRecognitionModel, EntityExtractionModel

class NLU:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.intent_model = IntentRecognitionModel()
        self.entity_model = EntityExtractionModel()

    def preprocess_text(self, text):
        words = word_tokenize(text)
        words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
        return ' '.join(words)

    def parse_intent(self, text):
        preprocessed_text = self.preprocess_text(text)
        intent = self.intent_model.predict(preprocessed_text)
        return intent

    def extract_entities(self, text):
        preprocessed_text = self.preprocess_text(text)
        entities = self.entity_model.predict(preprocessed_text)
        return entities

    def process_user_input(self, text):
        intent = self.parse_intent(text)
        entities = self.extract_entities(text)
        return intent, entities