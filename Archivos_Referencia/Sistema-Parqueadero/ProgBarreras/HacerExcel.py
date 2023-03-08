import xlwt

#----------------------------------------------------------------------
def main():

	libro = xlwt.Workbook()
	libro1 = libro.add_sheet("Prueba")

	cols = ["A", "B", "C", "D", "E"]
	txt = "Fila %s, Columna %s"

	for num in range(5):
		row = libro1.row(num)
		for index, col in enumerate(cols):
			value = txt % (num+1, col)
			row.write(index, value)

	libro.save("prueba.xls")

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
