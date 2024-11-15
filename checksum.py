def main(file_path):
    try:
        with open(file_path, 'rb') as file:
            checksum = sum(file.read()) % 256
            print(f"Original Checksum : {checksum}")
            file.seek(0)
            if sum(file.read()) % 256 == checksum:
                print("File is Intact")
            else:
                print("File is corrupted")
    except FileNotFoundError:
        print("File Not Found")

main("sample.csv")