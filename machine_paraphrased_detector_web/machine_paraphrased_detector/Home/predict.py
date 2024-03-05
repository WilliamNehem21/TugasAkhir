import pickle
import fasttext
import re
import numpy as np

class Predict:
    def __init__(self, text):
        self.text = text
        self.model = fasttext.load_model("/Users/williamnehemia/Documents/Skripsi/Fastext_model/SetelahPembagianData/model_cbow_fasttext_10.bin")
    
    # method untuk ubah text menjadi array of words
    def change_text_to_array_of_words(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        return text.split()

    # method untuk ubah dokumen ke array
    def change_text_to_array_number(self, array_of_words):
        # ubah kata menjadi angka
        converted_words = []
        for word in array_of_words:
            wv = self.model.get_word_vector(word)
            converted_words.append(wv)
        
        # ubah ke numpy array
        converted_words = np.array(converted_words)
        avg_array = np.mean(converted_words, axis=0)
        return avg_array
    
    def predict(self):
        array_words = self.change_text_to_array_of_words(self.text)
        avg_array = self.change_text_to_array_number(array_words)
        
        classification_model = pickle.load(open('/Users/williamnehemia/Documents/Skripsi/TugasAkhir/ClassificationModel/LogisticRegression/model_lr_testing.sav','rb'))
        y_pred = classification_model.predict([avg_array])
        print(y_pred)
        return y_pred
