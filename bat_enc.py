import sys
import os

def sno_encrypt_bat(input_path, output_path=None):
    if not os.path.isfile(input_path):
        print("Error: File not found.")
        return
    with open(input_path, "rb") as f:
        data = f.read()
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = base + "_SNO_ENCRYPTED" + ext
    header = bytes([0xFF, 0xFE, 0x0A, 0x0D])
    encrypted = header + data
    with open(output_path, "wb") as f:
        f.write(encrypted)
    print(f"Encrypted BAT created:\n{output_path}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bat_enc.py file.bat")
    else:
        sno_encrypt_bat(sys.argv[1])
