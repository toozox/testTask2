import sys
from scipy import interpolate, optimize


def main(fname):
    with open(fname, "r") as f:
        inputData = [s.strip().split(' ') for s in f.readlines()]
    # эта проверка нужна на всякий случай, вдруг между числами несколько пробелов
    validatedInputData = list()
    for i in range(len(inputData)):
        validatedInputData.append(list())
        for j in range(len(inputData[i])):
            if inputData[i][j]:
                validatedInputData[i].append(int(inputData[i][j]))

    x = list()
    y = list()
    x.append(0)
    y.append(0)
    for line in validatedInputData:
        x.append(line[0])
        y.append(line[1])
    # получаем функцию
    f = interpolate.interp1d(x, y, kind="quadratic", fill_value="extrapolate")
    # находим корень
    res = optimize.root(f, x[-1], method='hybr')
    if res.success:
        print(f"Камень улетел примерно на {float(res.x):.2f} м.")
    else:
        print("Не удалось найти решение")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Необходимо ввести входной файл. Например:\n  \
                    python testTask2.py in.txt")
        sys.exit()
    fname = sys.argv[1]
    try:
        main(fname)
    except FileNotFoundError:
        print(f"Файл {fname} не найден")
    except Exception:
        print("Что-то пошло не так")
