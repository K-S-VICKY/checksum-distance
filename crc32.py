import zlib
def main(file_path):
    try:
        with open(file_path, 'rb') as file:
            original_crc = zlib.crc32(file.read()) & 0xFFFFFFFF
            print(f"Original CRC : {original_crc}")
            file.seek(0)
            if zlib.crc32(file.read()) & 0xFFFFFFFF == original_crc:
                print("File is intact")
            else:
                print("File is corrupted")
    except FileNotFoundError:
        print("File Not Found")

main("sample.csv")
