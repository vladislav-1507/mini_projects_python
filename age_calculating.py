from functools import singledispatchmethod
from datetime import date
from dateutil.relativedelta import relativedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_sequence(self, birth_date):
        try:
            year, month, day = birth_date
            self.birth_date = date(year, month, day)
        except:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_date).years


birth_dates = ["2020-09-41", "2020-0918", "202009-18", "2020-9-18", "2020-41-09"]

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)

birthinfo1 = BirthInfo("2020-09-18")
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

# Теперь все три атрибута будут иметь тип <class 'datetime.date'>
print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

print(birthinfo1.age)
print(birthinfo2.age)
print(birthinfo3.age)

birthinfo = BirthInfo(date(2023, 12, 25))  # Пример для проверки расчета

print(birthinfo.age)
