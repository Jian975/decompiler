class E_Ident:
    #takes in byte array of first 16 bytes of an ELF header
    def __init__(self, byte_array):
        self.EI_MAG0 = byte_array[0]
        self.EI_MAG1 = byte_array[1]
        self.EI_MAG2 = byte_array[2]
        self.EI_MAG3 = byte_array[3]
        self.EI_CLASS = byte_array[4]
        self.EI_DATA = byte_array[5]
        self.EI_VERSION = byte_array[6]
        self.EI_OSABI = byte_array[7]
        self.EI_ABIVERSION = byte_array[8]
    def __str__(self):
        output = ""
        output += "E_Ident:\n"
        output += "\tEI_MAG0: " + str(self.EI_MAG0) + "\n"
        output += "\tEI_MAG1: " + str(self.EI_MAG1) + "\n"
        output += "\tEI_MAG2: " + str(self.EI_MAG2) + "\n"
        output += "\tEI_MAG3: " + str(self.EI_MAG3) + "\n"
        output += "\tEI_CLASS: " + str(self.EI_CLASS) + "\n"
        output += "\tEI_DATA: " + str(self.EI_DATA) + "\n"
        output += "\tEI_VERSION: " + str(self.EI_VERSION) + "\n"
        output += "\tEI_OSABI: " + str(self.EI_OSABI) + "\n"
        output += "\tEI_ABIVERSION: " + str(self.EI_ABIVERSION)  + "\n"
        return output
    

class ELF_Header:
    def __init__(self, byte_array):
        self.e_ident = E_Ident(byte_array[:16])
        self.e_type = byte_array[16:32]
        self.e_machine = byte_array[32:48]
        self.e_version = byte_array[48:80]
    def __str__(self):
        output = ""
        output += "ELF Header:\n"
        output += str(self.e_ident)
        output += "E_TYPE: " + str(self.e_type) + "\n"
        return output

def print_elf_header(filename):
    with open(filename, "rb") as file:
        elf_header = ELF_Header(file.read())
        print(elf_header)

def main():
    print_elf_header("hello")

if __name__ == "__main__":
    main()