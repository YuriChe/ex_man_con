from homeEx_man_cont import Loger
best_avr, best_grade = 0, None

if __name__ == '__main__':
    with Loger('hello.txt') as f:
    # with open('hello.txt') as f:
        while True:
            grade = f.readline().strip()
            if not grade:
                break
            rating = f.readline().strip()
            f.readline()
            int_ratings = []
            int_ratings = [int(i) for i in rating.split(' ')]
            # for item in rating.split(' '):
            #     int_ratings.append(int(item))
            avg = sum(int_ratings) / len(int_ratings)
            if avg > best_avr:
                best_avr = avg
                best_grade = grade

            print(f'{grade}: {rating} == {avg}')
print(f'лучший класс {best_grade}\n'
      f'средняя оценка {best_avr}')