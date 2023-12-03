def love_coroutine():
    print("I love you! Do you love me?")
    answer = yield
    if answer == "Yes":
        print("I love you too!")
    elif answer == "No":
        print("Why?")
    print(answer, " I'm out of here!")


coroutine = love_coroutine()


next(coroutine)

coroutine.send("Yes")
