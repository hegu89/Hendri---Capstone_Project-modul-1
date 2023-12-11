
import os

daftar_nilai = [                 
     ['1001','Andi', 80 , 100, 100],         
     ['2001','Rani', 70, 80, 90],
     ['3001','Rudi', 70, 80, 90]
]

judul = ['nis','nama','uts','uas','nilai_akhir']
 

def tampil():
    print('Daftar Nilai Siswa\n')
    print('Index\t\t|NIS\t\t|Nama\t\t|UTS\t\t|UAS\t\t|Nilai Akhir' ) 
    for i in range(len(daftar_nilai)) :
        print(f'|{i}\t\t', end = '')
        for j in daftar_nilai[i] : 
              print(f'|{j}\t\t', end = '')
                                                                                                  
        print('')
    print('')                                                                                              
              
def tambah():  
    tampil()
    print('\n') 
    
    # input dan validasi NIS 
    while True : 
        nis_input = input('Masukkan NIS yang ingin ditambah: ')

        # validasi numerik
        if(nis_input.isalpha() ):                                          
             print('silahkan masukkan angka')
            
        # validasi jumlah digit
        elif len(nis_input) != 4 :
            print('silahkan masukkan 4 digit NIS')

        # validasi duplikat NIS
        else :
            temp = 0
            for i in range(len(daftar_nilai)):
                if(daftar_nilai[i][0]==nis_input):
                    temp = 1
                    break

            if temp == 1:
                print('NIS sudah ada, silahkan masukkan NIS lain' )

            # exit while
            else : 
                break

     # input dan validasi nama           
    while True:            
        nama = input('Masukkan Nama  : ') 
        if(any(chr.isdigit() for chr in nama)):
            print('nama tidak boleh mengandung angka')
        else :
            break

    # input dan validasi UTS
    while True:
            uts = input('Masukkan Nilai UTS : ')
            if(uts.isnumeric() ):
                if int(uts) > 100 :
                    print('masukkan angka antara 0 sampai 100')
                else :
                    break    
            else :
                print('tolong input nilai UTS dalam angka')
             
    # input dan validasi UAS         
    while True:
            uas = input('Masukkan Nilai UAS : ')
            if(uas.isnumeric() ):
                if int(uas) > 100 :
                    print('masukkan angka antara 0 sampai 100')
                else :
                    break
            else :
                print('tolong input nilai UAS dalam angka')
                
    # input dan validasi nilai akhir            
    while True:
            nilai_akhir = input('Masukkan nilai akhir : ')
            if(nilai_akhir.isnumeric() ):
                if int(nilai_akhir) > 100 :
                    print('masukkan angka antara 0 sampai 100')
                else :
                    break
            else :
                print('tolong input nilai akhir dalam angka')   

    daftar_nilai.append([nis_input,nama,uts,uas,nilai_akhir])
    
    return daftar_nilai
                     
def hapus():
    tampil()

    # input dan validasi NIS yang ingin dihapus
    while True :
        nis_hapus = input('Masukkan NIS yang ingin dihapus : ')
        
        if len(nis_hapus) != 4 :
            print('silahkan masukkan 4 digit NIS')
        else :
            temp = 0
            for i in range(len(daftar_nilai)):
                if(daftar_nilai[i][0]==nis_hapus):
                    temp = 1
                    break

            if temp == 0:
                print('NIS tidak ditemukan' )
            else : 
                del (daftar_nilai[i])
                break
    return daftar_nilai
    
def update():
    tampil()
    
    # Validasi NIS yang ingin diupdate
    while True :                                  
        nis_update = input('Masukkan NIS yang ingin diupdate :  ')
        
        if len(nis_update) != 4 :
            print('silahkan masukkan 4 digit NIS')
        else :
                temp = 0
                for i in range(len(daftar_nilai)): 
                      if (daftar_nilai[i][0]) == nis_update :
                        temp = 1   
                        break
                      
                if temp == 0:
                        print('NIS tidak ditemukan')   
                else :
                        break

    # Validasi kategori 
    while True :
        kategori_update = input('\nPilihan kategori yang dapat diupdate : \n1.Ketik nis untuk ubah NIS \n2.Ketik nama untuk ubah nama \n3.Ketik uts untuk ubah UTS \n4.Ketik uas untuk ubah UAS \n5.Ketik nilai_akhir untuk ubah nilai akhir \nMasukkan kategori yang ingin diubah: ').lower()
                                                         
        if(kategori_update in judul) :
            break
        else :
            print('kategori yang dimasukkan salah')
   
   # membaca urutan kolom dengan mapping kategori update di list judul
    j = judul.index(kategori_update) 
    
    while True :
        # mengulang input jika validasi gagal
        nilai_pengganti = input('Masukkan value pengganti: ')

        # validasi UTS,UAS,Nilai akhir
        if j >= 2:
            if (nilai_pengganti.isnumeric()) : 
                if int(nilai_pengganti) > 100 :
                    print('masukkan angka antara 0 sampai 100 ')    
                else : 
                    break       
            else :
                print('masukkan angka sebagai value pengganti ')

        # validasi nama
        elif j == 1:
            if(any(chr.isdigit() for chr in nilai_pengganti)):
                print('nama tidak boleh mengandung angka')
            else :
                break

        # kategori selain yang di atas( tidak ada validasi ) 
        else :
            break
   
   # update berdasarkan nilai pengganti
    for i in range(len(daftar_nilai)): 
        if(daftar_nilai[i][0] == nis_update): 
             daftar_nilai[i][j] = nilai_pengganti 
                
    return daftar_nilai
        
while True :

    try :

        print('\t\tSelamat Datang di Data Nilai Siswa\n\n')
        print('''\t\tList Menu :
              1. Menampilkan Daftar Siswa
              2. Menambah Data Siswa
              3. Menghapus Data Siswa
              4. Mengupdate Data Siswa
              5. Keluar dari Program''')
        menu = int(input('Masukkan angka Menu yang ingin dipilih : '))

        if menu == 1 : 
            os.system('cls')
            tampil()

        elif menu == 2 :
            os.system('cls')
            tambah()   
            
        elif menu == 3 :
            os.system('cls')
            hapus()

        elif menu == 4 :
            os.system('cls')
            update()

        elif menu == 5 :
            break

        else :
            print('Pilihan menu hanya ada 1 sampai 5')

    except: 
        print('Masukkan Angka!')

          
























