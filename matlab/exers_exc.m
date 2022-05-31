function main()
inT = readtable('fileExcel.xlsx')
ruc_string = 'Руководитель'
isp_string = 'Исполнитель'
roles = ["Роли"; "Руководитель"; "Исполнитель"]
rucs = ""
isps = ""
for i = 1 : height(inT)
    if (strcmp(inT{i, 2}, ruc_string))
        rucs = rucs + inT{i, 1} + ", "
    else
        isps = isps + inT{i, 1} + ", "
end
people = ["Люди"; rucs; isps]
outT = table(roles, people)
writetable(outT, 'result.xls') 
end