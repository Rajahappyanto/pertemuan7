## **penjelasan tugas pertemuan 7**

#### Buat program sederhada dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

pertama masukkan int, lalu di ikuti dengan perintah if elif dan else, sertakan pula tanda < (lebih keci dari) untuk memberikan perintah. lebih jelasnya seperti pada foto

![scs1]foto/scs1.png

#### Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.


'''

   if a<b and a<c:
        if b<c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b<a and b<c:
        if a<c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a<b:
            print(c, a, b)
        else:
            print(c, b, a)

'''

 seperti contoh diatas, perintah akan if elif dan else akan di deklarasikan seperti yang terdapat pada contoh, untuk lebih lengkapnya seperti gambar di bawah ini


![scs2]foto/scs2.png


#### Buat program dengan perulangan bertingkat (nested) 


kali ini saya menggunakan for dan range sintaxnya seperti ini:

'''
 for i in range(0, 10):
	for j in range(0, 10):
	  print(i+j, end='')
	print()

'''
sebagai contoh pemamparan seperti pada gambar

![scs3]foto/scs3.png


#### Tampilkan n bilangan acak yang lebih kecil dari 0.5. nilai n diisi pada saat runtime

dalam kasus kali ini saya menggunakan perintah seperti di bawah ini

'''
 import random

a = int(input('Masukkan jumlah n : '))
for i in range(a):
    n = random.random()
    print(n)

'''
sebagai contoh saya sertakan gambar di bawah ini


![scs4]foto/scs4.png



## atas perhatiannya saya ucapkan terimakasih, apabila banyak penjelasan saya yang kurang dapat untuk di pahami saya minta maaf.