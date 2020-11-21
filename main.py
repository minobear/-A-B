import random


def generate_ran_ans():
    ans = random.sample("1234567890", 4)
    return "".join(ans)


def get_result(ans, guess):
    A = len([1 for i in range(4) if ans[i] == guess[i]])
    B = 4 - A - len(set(ans) - set(guess))

    return True if A == 4 else False, f"{A}A{B}B"


def input_guess_num():
    while True:
        num = input("請輸入你的猜值:")
        num_set = set(num)

        if len(num_set) != 4 or len(num_set) != len(num):
            print("猜值必須為4個互不重複的數字!")
            continue

        return num


def new_game(Debug=False):
    guess_count = 0
    ans_num = generate_ran_ans()
    print(ans_num) if Debug else None

    while True:
        guess_num = input_guess_num()
        correct, result = get_result(ans_num, guess_num)
        print(result)
        if correct:
            print(f"恭喜答對! 你總共猜了 {guess_count} 次")
            break
        guess_count += 1


def check_next_game():
    flag = input("想再玩一次嗎? (y/n)")
    return True if flag == "y" or flag == "Y" else False


if __name__ == '__main__':
    while True:
        new_game(Debug=True)
        if not check_next_game():
            break
