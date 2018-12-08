# import csv
#
#
# def check(x):
#     '''Проверка чисел'''
#     if x[0].isdigit():
#         price = int(x.replace(' ', ''))
#     else:
#         price = x
#     return price
#
#
# def _amount(x, y):
#     """Среднее арифметрическое чисел"""
#     amount = x / y
#     return amount
#
#
# def main():
#     raion = str(input())
#     List_new = []
#     FILENAME = "file.csv"
#     with open(FILENAME, "r") as file:
#         reader = csv.reader(file)
#         ##    for row in reader:
#         ##        print(row[0])
#
#         ##    print(*reader)
#
#         ##    for row in reader:
#         ##        prn = row[0].split(';')
#         ##        if len(prn[0])<7 :
#         ##            prn[0] +='    '
#         ##        print('* '+prn[0]+'\t',  5+int(prn[13].replace(' ','')) if prn[13][0].isdigit() else prn[13]  )
#         for row in reader:
#             prn = row[0].split(';')
#             List_new.append(prn)
#         for row in List_new:
#             print(row)
#
#         # for row in List_new:
#         #     if len(row[0]) < 7:
#         #         row[0] += '    '
#         #     print('* ' + row[0] + '\t', 5 + int(row[13].replace(' ', '')) if row[13][0].isdigit() else row[13])
#
#         for row in List_new:
#             if len(row[0]) < 12:
#                 row[0] += '    '
#             price = check(row[13])
#             square = check(row[8])
#             # if row[13][0].isdigit():
#             #     price = int(row[13].replace(' ', ''))
#             # else:
#             #     price = row[13]
#             print('* ', row[0], price, square)
#
#         for r in List_new:
#             if raion == r[0]:
#                 print(r[0])
#             else:
#                 print(r[1])
#             # if raion == r[0]:
#             #     price_square = r[1] / r[2]
#             #     print(price_square)
#
#
# if __name__=='__main__':
#     main()







import csv


def check(x):
    '''Проверка чисел'''
    if x[0].isdigit():
        price = int(x.replace(' ', ''))
    else:
        price = x
    return price


def _amount(x, y):
    """Среднее арифметрическое чисел"""
    amount = x / y
    return amount


def main():
##    raion = input()
    raion = input()
    List_new = []
    FILENAME = "file.csv"
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        ##    for row in reader:
        ##        print(row[0])

        ##    print(*reader)

        ##    for row in reader:
        ##        prn = row[0].split(';')
        ##        if len(prn[0])<7 :
        ##            prn[0] +='    '
        ##        print('* '+prn[0]+'\t',  5+int(prn[13].replace(' ','')) if prn[13][0].isdigit() else prn[13]  )
        for row in reader:
            prn = row[0].split(';')
            List_new.append(prn)
        for row in List_new:
            print(row)

        print('-----------------------------')

        for row in List_new:
            if row[0] == str(raion):
                print(row)

        print('-----------------------------')

        # for row in List_new:
        #     if len(row[0]) < 7:
        #         row[0] += '    '
        #     print('* ' + row[0] + '\t', 5 + int(row[13].replace(' ', '')) if row[13][0].isdigit() else row[13])

        for row in List_new:
            if len(row[0]) < 5:
                row[0] += '      '
            price = check(row[13])
            square = check(row[8])
            # if row[13][0].isdigit():
            #     price = int(row[13].replace(' ', ''))
            # else:
            #     price = row[13]
            print('* ', row[0]+'\t', str(price)+'\t', square)

        print('-----------------------------')
        D = 0
        for r in List_new:
            if r[0] == str(raion):
                price_square = int(r[13]) / int(r[8])
                D += 1
                print(r[0], price_square)
        print('Количество найденых квартир: ', D)


if __name__=='__main__':
    main()