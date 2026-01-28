from elftools.elf.elffile import ELFFile

with open("hello", "rb") as file:
    elf = ELFFile(file)
    print(elf.header)
    text = elf.get_section_by_name(".text")

    print(text.data())