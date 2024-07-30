// untuk memeriksa konten input text dan mengaktifkan atau menonaktifkan tombol submit
let triggerButton = document.getElementById('check_button'); // mengambil tag tombol Check
let modal = document.getElementById('exampleModalCenter'); // mengambil tag modal
let warning = document.getElementById('alert_message'); // mengambil tag warning input teks

// method untuk melakukan tahapan preprocess input
function preProcessInput(text_input){
    // ubah teks ke huruf kecil
    let text = text_input.toLowerCase();

    // hanya mengambil huruf
    text = text.replace(/[^a-zA-Z]/g, ' ');

    // hilangkan spasi berlebih
    text = text.trim();
   
    // mengembalikan teks yang telah dilakukan tahap preprocess
    return text
}

// method untuk memeriksa input yang dimasukkan oleh user
function checkTextContent() {
    try {
        // mengambil tag dari kotak input
        let element = document.getElementById('text_input');

        // mengambil isi dari kotak input
        let textContent = element.value;
        
        // melakukan tahap preprocess input
        textContent = preProcessInput(textContent);
        
        // mengambil tag tombol Check
        let button = document.getElementById('check_button');

        // jika panjang input teks lebih dari 0 karakter
        if (textContent.length > 0){

            // mengaktifkan tombol Check
            button.disabled = false;

            // menghilangkan warning input teks
            warning.hidden = true;
            
        }else { // jika panjang input teks adalah 0 karakter

            // menonaktifkan tombol Check
            button.disabled = true;

            // menampilkan warning input teks
            warning.hidden = false;
            
        }
    } catch (error) {
        
    }
    
    
    
}


// melakukan pengecekan setiap 2 detik dari input yang dimasukkan oleh user
let intervalId = setInterval(checkTextContent, 2); 


// event listener tombol Check
try {
    triggerButton.addEventListener('click', function() {
        // menampilkan pop up bahwa input parafrasa esai sedang diproses selama 3 detik
        clearTimeout(modal.dataset.hideInterval);
        let hideInterval = setTimeout(function() {
                
        }, 3000);

        // Menyimpan ID batas waktu dalam atribut data
        modal.dataset.hideInterval = hideInterval;
        
        
    });
} catch (error) {
    
}

        
    
        




