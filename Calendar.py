# Python program to display calendar
class calendar:
    run = True
    print('\t\t****Welcome In Magic world****')
    while run:
        try:
            import calendar
            year = int(input('enter the year: '))
            month = int(input('enter the month'))
            print(calendar.month(year,month))
            run = False
            print('GoodBye!!')
        except:
            print('Enter only Integer')
if __name__ == "__main__":
  obj = calendar()
