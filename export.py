import os
from xlutils.copy import copy
import xlrd as ExcelRead


def write_append(file_name):
    values = ["Ann", "woman", 22, "UK"]

    r_xls = ExcelRead.open_workbook(file_name)
    r_sheet = r_xls.sheet_by_index(0)
    rows = r_sheet.nrows
    w_xls = copy(r_xls)
    sheet_write = w_xls.get_sheet(0)

    for i in range(0, len(values)):
        sheet_write.write(rows, i, values[i])

    w_xls.save(file_name + '.out' + os.path.splitext(file_name)[-1]);


if __name__ == "__main__":
    write_append("./test_append.xls")