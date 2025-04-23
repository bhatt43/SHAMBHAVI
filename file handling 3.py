name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

with open(f"{name}.vcf", 'w') as file:
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")
    file.write(f"N:{name}\n")
    file.write(f"TEL:{phone}\n")
    file.write(f"EMAIL:{email}\n")
    file.write("END:VCARD\n")

print(f"vCard '{name}.vcf' created.")
