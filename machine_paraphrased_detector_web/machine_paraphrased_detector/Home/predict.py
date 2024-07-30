# import library
import pickle
import fasttext
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from gensim.models import Word2Vec

class Predict:
    # constructor
    def __init__(self, text):
        self.text = text
        self.model = Word2Vec.load("/Users/williamnehemia/Documents/Skripsi/TugasAkhir/machine_paraphrased_detector_web/word2vec_sg_62.model")

    
    # method untuk ubah text menjadi array of words
    def change_text_to_array_of_words(self, text):
        # ubah teks menjadi huruf kecil
        text = text.lower()

        # hanya mengambil huruf dari teks
        text = re.sub(r'[^a-zA-Z]', ' ', text)

        # mengembalikan array of words (tokenisasi)
        return text.split()

    # method untuk ubah array of words menjadi vector
    def change_text_to_array_number(self, array_of_words):
        # ubah kata menjadi angka
        converted_words = []
        for word in array_of_words:
            try:
                wv = self.model.wv[word]
                converted_words.append(wv)
            except:
                zeros_array = [0 for x in range(0,40)]
                converted_words.append(zeros_array)
                
        
        # ubah ke numpy array
        converted_words = np.array(converted_words)

        # melakukan rata-rata dari vektor kata
        avg_array = np.mean(converted_words, axis=0)

        # mengembalikan rata-rata dari vektor kata
        return avg_array
    
    # method untuk melakukan prediksi
    def predict(self):
        # mengubah teks menjadi array of words
        array_words = self.change_text_to_array_of_words(self.text)

        # mengubah array of words menjadi vektor
        avg_array = self.change_text_to_array_number(array_words)
        
        # memuat model klasifikasi
        classification_model = pickle.load(open('/Users/williamnehemia/Documents/Skripsi/TugasAkhir/machine_paraphrased_detector_web/classification_model_2_pkl','rb'))

        # melakukan prediksi
        y_pred = classification_model.predict([avg_array])

        # variabel untuk menyimpan kesamaan antara 2 teks
        similarity = 0

        # variabel untuk menyimpan nama file yang menjadi kesamaan tertinggi dengan masukkan esai
        file_name = ""

        # jika hasil prediksi menyatakan bahwa teks adalah hasil machine paraphrased essay 
        if y_pred[0] == 1:
            # menghitung kesamaan tertinggi antara input teks dengan dokumen yang ada di basis data dan mendapatkan nama file nya
            similarity, file_name = self.compute_similarity(avg_array)
        
        # mengembalikan hasil prediksi dan kesamaan tertinggi dan nama file nya antara input teks dengan dokumen yang ada di basis data
        return y_pred[0], similarity, file_name
    
    # method untuk menghitung kesamaan antara dua teks / dokumen
    def compute_similarity(self, avg_array_input):
        # variabel untuk menyimpan kesamaan tertinggi antara input teks dengan dokumen yang ada di basis data
        highest_similarity = 0

        # variabel untuk menyimpan nama file yang memiliki kesamaan tertinggi antara input teks dengan dokumen yang ada di basis data
        highest_similarity_file = ""

        # mengambil direktori data dokumen hasil machine paraphrased essay
        directory_path_paraphrased = '/Users/williamnehemia/Documents/Skripsi/TugasAkhir/machine_paraphrased_detector_web/Database_paraphrased_essay'

        # mengambil daftar dokumen pada direktori data dokumen hasil machine paraphrased essay
        files_paraphrased = os.listdir(directory_path_paraphrased)

        # list untuk menyimpan nama dokumen
        list_files_paraphrased = []

        # Ambil daftar nama file
        for file in files_paraphrased:
            if '.DS_Store' not in file:
                list_files_paraphrased.append(file)
                
        # looping untuk mencari kesamaan tertinggi antara input teks dengan dokumen yang ada di basis data
        for file in list_files_paraphrased:
            with open('/Users/williamnehemia/Documents/Skripsi/TugasAkhir/machine_paraphrased_detector_web/Database_paraphrased_essay/' + file, 'r') as fileNow:
                # membaca dokumen
                content = fileNow.read()

                # mengubah teks menjadi array of words
                array_words = self.change_text_to_array_of_words(content)

                # mengubah array of words menjadi vektor
                avg_array_curr = self.change_text_to_array_number(array_words)

                # menghitung kesamaan antara dua teks
                similarity_curr = cosine_similarity([avg_array_input], [avg_array_curr])

                # jika skor kesamaan pada dokumen sekarang lebih tinggi dari pada nilai kesamaan tertinggi sementara
                if similarity_curr[0][0] > highest_similarity:
                    # mengganti kesamaan tertinggi dengan kesamaan pada dokumen sekarang
                    highest_similarity = similarity_curr[0][0]

                    # mengganti nama file yang memiliki kesamaan tertinggi sekarang
                    highest_similarity_file = file

        # melakukan pembulatan nilai kesamaan dengan 3 digit dibelakang koma
        highest_similarity = round(highest_similarity, 3)

        # mengembalikan nilai kesamaan tertinggi dan nama file antara input teks dengan dokumen yang ada di basis data
        return highest_similarity, highest_similarity_file
