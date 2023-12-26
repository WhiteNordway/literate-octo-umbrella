def max_of_list(lst):
   return max(lst)


if __name__ == "__main__":
   quantity = int(input("Введите число элементов массива: "))
   lst = input("Введите элементы массива через пробел: ").split()
   if len(lst) > quantity:
      lst = lst[:quantity]
   print(f"{max_of_list(lst) = }")
