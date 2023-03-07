#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import xlwt

fmt = xlwt.easyxf

encabezado = fmt('font: name Arial, color red, bold on;')
centrado = fmt('alignment: horiz centre')

wb = xlwt.Workbook()

full = wb.add_sheet("Tabla del 5")

full.write(0, 0, "Tabla del 5", encabezado)

for x in range(1, 11):
		full.write(x, 0, 5,centrado)
		full.write(x, 1, "x",centrado)
		full.write(x, 2, x,centrado)
		full.write(x, 3, "=",centrado)
		full.write(x, 4, xlwt.Formula('A%s*C%s' % (x+1, x+1)))

wb.save('Tabla_5.xls')
