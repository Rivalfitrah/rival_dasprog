print(15*"=")
print("kalkulator")
print(15*"=" + "\n")

angka_1 = float(input("masukan angka: "))
operator = input("operator ( +, -, *, / ): ")
angka_2 = float(input("masukan angka ke 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya {hasil}")