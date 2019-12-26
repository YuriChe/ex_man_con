import datetime
import time

class Loger:

    def __init__(self, path):
        self.path = path
        # self.encoding = encoding

    def __enter__(self):
        self.beg_1 = datetime.datetime.now()
        print(f'Программа началась {self.beg_1}')
        self.file = open(self.path, 'r', encoding='utf8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if exc_type:
        #     self.file.write(f'\n{datetime.datetime.now()}ERROR {exc_type} {exc_val}')
        self.end_1 = datetime.datetime.now()
        self.duration = self.end_1 - self.beg_1
        print(f'Программа завершилась {self.end_1}. Длилась {self.duration}')
        self.file.close()

    def write_st(self, info):
        self.file.write(info)

    def readline(self):
        self.file.readline()

if __name__ == '__main__':
    with Loger('testTime1.txt') as log:
        time.sleep(5)
        for i in range(1000):
            log.write_st(f'{i}\n')