def get_input_menu():
    print("\n",
          "1 - Обратиться к определенной строке по индексу массива", "\n",
          "2 - Создание нового массива посредством поэлементного сцепления двух массивов", "\n",
          "3 - Слияние двух массивов с исключением повторений", "\n",
          "4 - Вывод элемента массива по индексу + вывод всего массива", "\n"
          )
    x = int(input("Выберите пункт меню: "))
    return x


class ArrayMass:
    m1 = [1, 6, 3, 7, 9, 2, 0, 1]
    m2 = [5, 1, 9, 5, 8, 4, 0, 2]
    mass_fin = []
    len = len(m1)
    print("\n", "Два исходных массива с длиной", len, ":", "\n", m1, "\n", m2, "\n")

    def mass_index(self, action):
        if (action > len(self.m1) - 1) or (action < 0):
            print("\n", "Неверный индекс!", "\n")
        choice = int(input("Выберите одну из двух строк (1 или 2): "))
        if choice == 1:
            print("Наш элемент:", self.m1[action])
        elif choice == 2:
            print("Наш элемент:", self.m2[action])
        else:
            print("Такой строки не существует!")
        return choice

    def multiply_mass(self):
        self.mass_fin = []
        for i in range(self.len):
            self.mass_fin.append(self.m1[i])
            self.mass_fin.append(self.m2[i])
        return self.mass_fin

    def new_mass(self):
        self.mass_fin = []
        mass = self.multiply_mass()
        print(list(set(mass)))

    def all_mass_index(self, action):
        x = self.mass_index(action)
        if x == 1:
            print(self.m1)
        else:
            print(self.m2)


def main():
    x = get_input_menu()
    obj = ArrayMass()

    if x == 1:
        index = int(input("Введите индекс: "))
        obj.mass_index(index)
    elif x == 2:
        mass = obj.multiply_mass()
        print(mass)
    elif x == 3:
        obj.new_mass()
    elif x == 4:
        index = int(input("Введите индекс: "))
        obj.all_mass_index(index)
    else:
        print("\n", "Такого пункта меню не существует!", "\n")


if __name__ == "__main__":
    main()
