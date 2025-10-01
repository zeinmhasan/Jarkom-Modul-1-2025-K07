import sys

# Kamus pemetaan HID ke ASCII
HID_TO_ASCII = {
    0x04: 'a', 0x05: 'b', 0x06: 'c', 0x07: 'd', 0x08: 'e', 0x09: 'f', 0x0A: 'g',
    0x0B: 'h', 0x0C: 'i', 0x0D: 'j', 0x0E: 'k', 0x0F: 'l', 0x10: 'm', 0x11: 'n',
    0x12: 'o', 0x13: 'p', 0x14: 'q', 0x15: 'r', 0x16: 's', 0x17: 't', 0x18: 'u',
    0x19: 'v', 0x1A: 'w', 0x1B: 'x', 0x1C: 'y', 0x1D: 'z',
    0x1E: '1', 0x1F: '2', 0x20: '3', 0x21: '4', 0x22: '5', 0x23: '6', 0x24: '7',
    0x25: '8', 0x26: '9', 0x27: '0',
    0x28: '\n', 0x29: '[ESC]', 0x2A: '[BACKSPACE]', 0x2B: '\t', 0x2C: ' ',
    0x2D: '-', 0x2E: '=', 0x2F: '[', 0x30: ']', 0x31: '\\', 0x33: ';', 0x34: '\'',
    0x35: '`', 0x36: ',', 0x37: '.', 0x38: '/',
    0x59: '1', 0x5A: '2', 0x5B: '3', 0x5C: '4', 0x5D: '5', 0x5E: '6', 0x5F: '7',
    0x60: '8', 0x61: '9', 0x62: '0',
}

SHIFT_HID_TO_ASCII = {
    0x04: 'A', 0x05: 'B', 0x06: 'C', 0x07: 'D', 0x08: 'E', 0x09: 'F', 0x0A: 'G',
    0x0B: 'H', 0x0C: 'I', 0x0D: 'J', 0x0E: 'K', 0x0F: 'L', 0x10: 'M', 0x11: 'N',
    0x12: 'O', 0x13: 'P', 0x14: 'Q', 0x15: 'R', 0x16: 'S', 0x17: 'T', 0x18: 'U',
    0x19: 'V', 0x1A: 'W', 0x1B: 'X', 0x1C: 'Y', 0x1D: 'Z',
    0x1E: '!', 0x1F: '@', 0x20: '#', 0x21: '$', 0x22: '%', 0x23: '^', 0x24: '&',
    0x25: '*', 0x26: '(', 0x27: ')',
    0x2D: '_', 0x2E: '+', 0x2F: '{', 0x30: '}', 0x31: '|', 0x33: ':', 0x34: '"',
    0x35: '~', 0x36: '<', 0x37: '>', 0x38: '?',
}

def decrypt_hid_data(hid_codes):
    result = ""
    for report in hid_codes:
        if len(report) < 3:
            continue
        modifier_byte = report[0]
        keycode = report[2]
        is_shift_pressed = (modifier_byte & 2) or (modifier_byte & 32)
        char = ''
        if keycode == 0:  # Abaikan jika tidak ada tombol yang ditekan (key release)
            continue
        if is_shift_pressed:
            char = SHIFT_HID_TO_ASCII.get(keycode, HID_TO_ASCII.get(keycode, ''))
        else:
            char = HID_TO_ASCII.get(keycode, '')
        result += char
    return result

def parse_hid_data_from_log(file_content):
    """
    Mengekstrak data HID dari log Wireshark dan mengubahnya ke format yang benar.
    """
    hid_codes = []
    for line in file_content.splitlines():
        # Cari baris yang mengandung 'HID Data:'
        if 'HID Data:' in line:
            # Ambil string hex setelah 'HID Data: '
            hex_str = line.split(':')[-1].strip()
            
            try:
                # Ubah string hex (misal: "020018...") menjadi list of integers
                # Contoh: [int('02', 16), int('00', 16), int('18', 16), ...]
                # Menjadi: [2, 0, 24, 0, 0, 0, 0, 0]
                byte_list = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]
                hid_codes.append(byte_list)
            except (ValueError, IndexError):
                # Lewati jika ada baris yang formatnya tidak valid
                continue
    return hid_codes

def main():
    if len(sys.argv) < 2:
        print("Error: Mohon sertakan nama file input.")
        print("Contoh: python3 hid_decoder.py namafile.txt")
        return

    input_filename = sys.argv[1]
    
    try:
        with open(input_filename, 'r') as f:
            log_content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' tidak ditemukan.")
        return

    # Ekstrak data HID dari log
    hid_data_list = parse_hid_data_from_log(log_content)
    
    # Lakukan dekripsi dan cetak hasilnya
    decoded_text = decrypt_hid_data(hid_data_list)
    print(decoded_text, end='')

if __name__ == "__main__":
    main()