
class Parser:
    date = 0
    date_temp = 0
    count = 0
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0
    first = True
    month = 'm'


    def years(self, file, success = None):
        if success is True:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    for i in split:
                        if i == 'S':
                            self.date = split[1]
                            self.count += 1
                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    for i in split:
                        if i == 'S':
                            self.date= split[2]
                            self.count += 1
                else:
                    self.count += 1

                if self.date != self.date_temp:
                    if not self.first:
                        print('\''+self.date_temp+'\'',':', self.count,',')
                    self.first = False
                    self.date_temp = self.date
                    self.count = 0

        if success is False:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    for i in split:
                        if i == 'F':
                            self.date = split[1]
                            self.count += 1
                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    for i in split:
                        if i == 'F':
                            self.date = split[2]
                            self.count += 1
                else:
                    self.count += 1

                if self.date != self.date_temp:
                    if not self.first:
                        print('\'' + self.date_temp + '\'', ':', self.count, ',')
                    self.first = False
                    self.date_temp = self.date
                    self.count = 0

        if success is None:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    self.date = split[1]
                    self.count += 1
                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    self.date = split[2]
                    self.count += 1
                else:
                    self.count += 1

                if self.date != self.date_temp:
                    if not self.first:
                        print('\'' + self.date_temp + '\'', ':', self.count, ',')
                    self.first = False
                    self.date_temp = self.date
                    self.count = 0

    def months(self, file, success = None):
        if success is None:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    self.month = split[2]
                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    self.month = split[3]

                if self.month == 'Jan':
                    self.Jan += 1
                elif self.month == 'Feb':
                    self.Feb += 1
                elif self.month == 'Mar':
                    self.Mar += 1
                elif self.month == 'Apr':
                    self.Apr += 1
                elif self.month == 'May':
                    self.May += 1
                elif self.month == 'Jun':
                    self.Jun += 1
                elif self.month == 'Jul':
                    self.Jul += 1
                elif self.month == 'Aug':
                    self.Aug += 1
                elif self.month == 'Sep':
                    self.Sep += 1
                elif self.month == 'Oct':
                    self.Oct += 1
                elif self.month == 'Nov':
                    self.Nov += 1
                elif self.month == 'Dec':
                    self.Dec += 1

        elif success is True:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    temp = True
                    if split[len(split)-2] == "S":
                        self.month = split[2]
                        temp = False
                    if temp:
                        self.month = "x"
                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    temp = True
                    if split[len(split)-2] == "S":
                        self.month = split[3]
                        temp = False
                    if temp:
                        self.month = "x"

                if self.month == 'Jan':
                    self.Jan += 1
                elif self.month == 'Feb':
                    self.Feb += 1
                elif self.month == 'Mar':
                    self.Mar += 1
                elif self.month == 'Apr':
                    self.Apr += 1
                elif self.month == 'May':
                    self.May += 1
                elif self.month == 'Jun':
                    self.Jun += 1
                elif self.month == 'Jul':
                    self.Jul += 1
                elif self.month == 'Aug':
                    self.Aug += 1
                elif self.month == 'Sep':
                    self.Sep += 1
                elif self.month == 'Oct':
                    self.Oct += 1
                elif self.month == 'Nov':
                    self.Nov += 1
                elif self.month == 'Dec':
                    self.Dec += 1

        elif success is False:
            for line in file:
                split = line.split()
                if split[1].isdigit() and len(split[1]) == 4 and len(split) > 9:
                    temp = True
                    if split[len(split)-2] == "F":
                        self.month = split[2]
                        temp = False
                    if temp:
                        self.month = "x"

                elif split[2].isdigit() and len(split[2]) == 4 and len(split) > 9:
                    temp = True
                    if split[len(split)-2] == "F":
                        self.month = split[3]
                        temp = False
                    if temp:
                        self.month = "x"

                if self.month == 'Jan':
                    self.Jan += 1
                elif self.month == 'Feb':
                    self.Feb += 1
                elif self.month == 'Mar':
                    self.Mar += 1
                elif self.month == 'Apr':
                    self.Apr += 1
                elif self.month == 'May':
                    self.May += 1
                elif self.month == 'Jun':
                    self.Jun += 1
                elif self.month == 'Jul':
                    self.Jul += 1
                elif self.month == 'Aug':
                    self.Aug += 1
                elif self.month == 'Sep':
                    self.Sep += 1
                elif self.month == 'Oct':
                    self.Oct += 1
                elif self.month == 'Nov':
                    self.Nov += 1
                elif self.month == 'Dec':
                    self.Dec += 1

        print('\''+'Jan'+'\'',':', self.Jan,',')
        print('\''+'Feb'+'\'',':', self.Feb,',')
        print('\''+'Mar'+'\'',':', self.Mar,',')
        print('\''+'Apr'+'\'',':', self.Apr,',')
        print('\''+'May'+'\'',':', self.May,',')
        print('\''+'Jun'+'\'',':', self.Jun,',')
        print('\''+'Jul'+'\'',':', self.Jul,',')
        print('\''+'Aug'+'\'',':', self.Aug,',')
        print('\''+'Sep'+'\'',':', self.Sep,',')
        print('\''+'Oct'+'\'',':', self.Oct,',')
        print('\''+'Nov'+'\'',':', self.Nov,',')
        print('\''+'Dec'+'\'',':', self.Dec,',')

    def group_by(self, file, method, success = None):
        if method == 'year':
            self.years(file, success)
        if method == 'months':
            self.months(file, success)

print('Seclect Year(Y) or Month(M)')
select = input('')
if select == 'Y':
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year')
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year', success = True)
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year', success = False)
elif select == 'y':
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year')
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year', success = True)
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'year', success = False)
elif select == 'M':
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months')
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months', success = True)
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months', success = False)
elif select == 'm':
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months')
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months', success = True)
    Parser().group_by(open('C:\Task1\launchlog.txt'), 'months', success = False)
else:
    print('Wrong button, try again')