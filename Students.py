class STUDENT:
    def __init__(self):
        self.lastname = input("Введите фамилию: ")
        self.firstname = input("Введите имя: ")
        self.patronymic = input("Введите отчество: ")
        self.groupClass = input("Введите группу: ")
        self.tablet = list(map(int, input("Введите 5 оценок: ").split()))

    def __repr__(self):
        return f'''
        Фамилия: {self.lastname} 
        Имя: {self.firstname} 
        Отчество: {self.patronymic}
        Группа: {self.groupClass}
        Оценки: {' '.join(list(map(str, self.tablet)))}'''


def counter(students):
    count = 0

    for person in students:
        if (person.tablet.count(2) >= 1):
            print("Оценка `2` есть у человека с фамилией", person.lastname, "и группой:", person.groupClass)
            count += 1

    return count


def main():
    students = [STUDENT() for _ in range(10)]
    students.sort(key=lambda person: person.lastname)
    print(students)

    count = counter(students)

    if count == 0:
        print("Не нашлись студенты с оценкой `2`!")


if __name__ == "__main__":
    main()
