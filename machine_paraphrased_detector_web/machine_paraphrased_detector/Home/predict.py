import pickle
import fasttext
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

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
        similarity = 0
        if y_pred[0] == 1:
            similarity = self.compute_similarity(avg_array)
        return y_pred[0], similarity
    
    def compute_similarity(self, avg_array_input):
        highest_similarity = 0
        directory_path_paraphrased = '/Users/williamnehemia/Documents/Skripsi/TugasAkhir/WordEmbeddingModel/Data/Data_parafrasa'

        files_paraphrased = os.listdir(directory_path_paraphrased)
        list_files_paraphrased = []

        # Ambil daftar nama file
        for file in files_paraphrased:
            if '.DS_Store' not in file:
                list_files_paraphrased.append(file)
                
        
        for file in list_files_paraphrased:
            with open('/Users/williamnehemia/Documents/Skripsi/TugasAkhir/WordEmbeddingModel/Data/Data_parafrasa/' + file, 'r') as fileNow:
                content = fileNow.read()
                array_words = self.change_text_to_array_of_words(content)
                avg_array_curr = self.change_text_to_array_number(array_words)
                similarity_curr = cosine_similarity(avg_array_input, avg_array_curr)

                if similarity_curr[0][0] > highest_similarity:
                    highest_similarity = similarity_curr[0][0]
        
        return highest_similarity
