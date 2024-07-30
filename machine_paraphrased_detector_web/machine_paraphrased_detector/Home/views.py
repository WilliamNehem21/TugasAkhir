# import library dan class
from django.shortcuts import render
import time
from .predict import Predict
import re

# method untuk menampilkan request halaman
def index(request):
    # jika request dari pemanggilan method ada POST (ada submit form)
    if (request.method == "POST"):
            
            # melakukan sleep agar dapat menampilkan pop up bahwa input sedang di proses
            time.sleep(3)

            # memanggil method predict untuk menampilkan hasil prediksi
            return predict(request)
    else: # jika request dari pemanggilan method bukan POST (tidak submit form)
        # menampilkan halaman utama
        return render(request, 'Home/base.html')


# method untuk melakukan prediksi dan menampilkan halaman hasil prediksi
def predict(request):
    # mengambil data input dari request
    text = request.POST['text']

    # membuat object dari kelas Predict
    predict_model = Predict(text)

    # melakukan prediksi
    predicted, similarity, file_name = predict_model.predict()

    # jika hasil prediksi menyatakan bahwa input bukan hasil machine paraphrased essay
    if predicted == 0:
        # menampilkan halaman prediksi bahwa input bukan hasil machine paraphrased essay
        return render(request, 'Home/notParaphrased.html')
    else: # jika hasil prediksi menyatakan bahwa input adalah hasil machine paraphrased essay
        # membuat dictionary yang berisi kesamaan input dengan dokumen yang ada di basis data
        context = {
            'similarity' : similarity,
            'file_name' : file_name,
        }
        # menampilkan halaman prediksi bahwa input adalah hasil machine paraphrased essay
        return render(request, 'Home/paraphrased.html', context)
    
