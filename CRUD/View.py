from . import Operasi

def delete_console():
    read_console()
    while (True):
        print("Silahkan pilih buku yang akan di delete : ")
        no_buku = int(input("Nomer Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin didelete
            print("Silahkan pilih data yang ingin anda delete")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == 'y' or is_done == 'Y':
                Operasi.delete(no_buku)
                break 
        else:
            print("Nomer tidak valid, silahkan masukan lagi!!")
    print("Data berhasil di hapus")


def update_console():
    read_console()
    while (True):
        no_buku = int(input("Nomer Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomer tidak valid, silahkan masukan lagi!!")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        # data yang ingin diupdate
        print("Silahkan pilih data yang ingin anda rubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode 
        user_option = input("Pilih data [1/2/3] : ")
        print("\n"+"="*100)
        match user_option:
            case "1" : judul = input("Masukan Judul\t: ")
            case "2" : penulis = input("Masukan Penulis\t: ")
            case "3" : 
                while(True):
                    try:
                        tahun = int(input("Tahun\t : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka dan panjangnya harus 4, silahkan masukan tahun lagi (yyyy)")
                    except:
                        print("Tahun harus angka dan panjangnya harus 4, silahkan masukan tahun lagi (yyyy)")
            case _: print("Index tidak coucokk") 
         
        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        is_done = input("Apakah update sesuai (y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka dan panjangnya harus 4, silahkan masukan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka dan panjangnya harus 4, silahkan masukan tahun lagi (yyyy)")

    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()


def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data Read
    for index, data in enumerate(data_file):
        data_break = data.split(",")    
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
    # Footer
    print("="*100+"\n")
