camel = input()
snake = ""

for i in camel:

    if i.isupper():
        snake = snake + "_"
    snake = snake + i
    
print(snake.lower())
