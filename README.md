# 幾A幾B遊戲

## 遊戲規則:
玩家必須猜四個0~9互不重複的數字，並且系統會告訴你幾A幾B，若數字對但位置不對為B，若數字對且位置也對則為A，直到4A0B為勝利。
```
例如: 
系統產生的答案數字為8197，此時如果玩家猜1847則為1A2B，代表玩家猜的1、8、7數字有在答案內，但位置相符的數字只有7是正確的，故為1A(數字及位置都對) 2B(數字對但位置不對)  
又例如答案為3857，你猜7853，即為2A2B。
```

## 運用Python的特點，來寫出功能到位且簡潔的程式碼:
```python
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
```
