sozluk = {"CRINGE": "Garip ya da utandırıcı bir şey", "LOL": "Komik bir şeye verilen cevap","ROFL":"Bir şakaya karşılık cevap","SHEESH":"onaylamamak","CREEPY":"korkunç","AGGRO":"agresifleşmek/sinirlenmek"}
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in sozluk.keys():
    print(sozluk[kelime])
else:
    print("Böyle bir kelime sözlükte bulunmamaktadır!!!")
