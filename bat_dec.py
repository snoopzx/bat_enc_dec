import sys
import os

HEADER = bytes([0xFF, 0xFE, 0x0A, 0x0D])
def sno_decrypt_bat(input_path, output_path=None):
    if not os.path.isfile(input_path):
        print("Error: File not found.")
        return
    with open(input_path, "rb") as f:
        data = f.read()
    if not data.startswith(HEADER):
        print("Error: (missing FF FE 0A 0D header)")
        return
    original = data[len(HEADER):]
    if not output_path:
        base, ext = os.path.splitext(input_path)
        if base.endswith("_SNO_ENCRYPTED"):
            base = base[:-len("_SNO_ENCRYPTED")]
        output_path = base + "_DECRYPTED" + ext
    with open(output_path, "wb") as f:
        f.write(original)
    print(f"Decrypted BAT created:\n{output_path}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bat_decryptor.py encrypted.bat")
    else:
        sno_decrypt_bat(sys.argv[1])
