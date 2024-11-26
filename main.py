import os
import CRUD as CRUD
if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt" : os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERUSAHAAN")
    print("=========================")

    # Check database itu ada atau tidak
    CRUD.init_console()
    while (True):   

        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt" : os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERUSAHAAN")
        print("=========================")


        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukan Opsi : ")

        match user_option:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()

        is_done = input("Apakah selesai (y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break

    print("Program Berakhir!!")