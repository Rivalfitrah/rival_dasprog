
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

suhu = float(input("Masukkan suhu: "))
satuan = input("Apakah dalam Celsius (C) atau Fahrenheit (F)? ").upper()

if satuan == "C":
    fahrenheit = celsius_to_fahrenheit(suhu)
    print(f"{suhu} derajat Celsius sama dengan {fahrenheit} derajat Fahrenheit")
elif satuan == "F":
    celsius = fahrenheit_to_celsius(suhu)
    print(f"{suhu} derajat Fahrenheit sama dengan {celsius} derajat Celsius")
else:
    print("Masukan tidak valid. Harap masukkan 'C' atau 'F' sebagai satuan suhu.")



