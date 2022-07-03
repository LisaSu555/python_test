
program_status = 1
guess_count = 10
key = 66
print("有一个数在1到100之间（均包含），请猜出来")
while program_status != 0:
    if guess_count < 1:
        print("你没机会了！")
        break
    print("请输入你猜想的数字（输入0结束游戏）")
    guess_you_input = input()
    if 1-guess_you_input.isdigit():
        print("请输入数字，别瞎搞！\n")
        continue
    guess_you = int(guess_you_input)
    if guess_you == 66:
        print("正确，就是 %d" % key)
        break
    elif guess_you == 0:
        print("bye！")
        break
    else:
        guess_count -= 1
        if guess_you > key:
            print("你猜得太大了，请继续猜测，还有%d次机会" % guess_count)
        else:
            print("你猜得太小了，请继续猜测，还有%d次机会" % guess_count)
