import random

# 產生並回傳四個互不相同的數字
def generate_ran_ans():
    ans = random.sample("1234567890", 4)  # 隨機取出4個不同的數值放入ans list中
    return "".join(ans)  # 將ans從list轉為字串

# 判斷答案與猜值, 並回傳兩個參數: 1.是否4A全對 2.幾A幾B
def get_result(ans, guess):
    A = len([1 for i in range(4) if ans[i] == guess[i]])  # for迴圈判斷ans[i]是否等於guess[i], 如果是就在list內新增1, 再取得該list的長度即為幾A
    B = 4 - A - len(set(ans) - set(guess))  # 先用4減掉A的數量, 再減掉ans與guess互相沒有相同的數字, 取其數量即為幾B。提示: set減掉set會將互相有相同的值排除

    return True if A == 4 else False, f"{A}A{B}B"

# 請玩家輸入猜值, 並且若符合規則即回傳該值, 否則重新輸入
def input_guess_num():
    while True:
        num = input("請輸入你的猜值:")
        num_set = set(num)  # 利用set將num中重複多餘的字排除, 確保每個字都是獨一無二的

        if len(num_set) != 4 or len(num_set) != len(num):  # 利用num_set的結果來判斷是否為4個數字且互不重複
            print("猜值必須為4個互不重複的數字!")
            continue

        return num

# 開啟新遊戲, Debug預設為False
def new_game(Debug=False):
    guess_count = 0
    ans_num = generate_ran_ans()
    print(ans_num) if Debug else None  # 若打開Debug則會直接顯示答案, 否則什麼都不做

    while True:
        guess_count += 1
        guess_num = input_guess_num()
        correct, result = get_result(ans_num, guess_num)
        print(result)  # 顯示幾A幾B
        if correct:
            print(f"恭喜答對! 你總共猜了 {guess_count} 次")
            break

# 詢問玩家是否進行下一場遊戲
def check_next_game():
    flag = input("想再玩一次嗎? (y/n)")
    return True if flag == "y" or flag == "Y" else False  # 若輸入小寫或打寫的"Y"回傳True, 否則為False

# Main程式進入點
if __name__ == '__main__':
    while True:
        new_game(Debug=True)
        if not check_next_game():
            break
