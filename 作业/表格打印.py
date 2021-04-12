# 编写一个名为printTable()的函数，它接受字符串的列表的列表，将它显示在组
# 织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table_list):

    colWidths = []
    for i in tableData:
        list_width = []             #新建列表存储小列表每个字符元素的宽度
        for n in i:                 
         list_width.append(len(n))  #遍历小列表存储得出每个字符宽度并添加lis_widths列表中
        list_width.sort(reverse=True) #lis_widths列表按降序排列
        colWidths.append(list_width[0]) #取出lis_widths最大值添加到colWidths列表存储
    # print(colWidths)
    for a in range(len(tableData[0])):
        for b in range(len(tableData)):
            print(tableData[b][a].rjust(colWidths[b]),' ',end='') 
        print('')

printTable(tableData)


        
            
















# print(colWidths)
# print('hello'.rjust(5))


