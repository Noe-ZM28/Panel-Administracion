import xlwt

distancias=[757, 41, 75, 343, 26, 247, 32, 61, 68, 49, 97, 22, 278]
print(distancias)

fichero_distancias = xlwt.Workbook()
datos = fichero_distancias.add_sheet("datos")

for i in range(len(distancias)):
    datos.write(i, 0, distancias[i])

fichero_distancias.save("ruta.xls")
