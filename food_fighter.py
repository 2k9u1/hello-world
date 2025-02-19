import csv

# 음식 색깔 분류
food_colors = {}

# CSV 파일에서 음식 색깔 데이터를 로드하는 함수
def load_food_colors():
    try:
        with open('food.csv', mode='r', encoding='utf-8') as food_file, open('color.csv', mode='r', encoding='utf-8') as color_file:
            food_reader = csv.reader(food_file)
            color_reader = csv.reader(color_file)
            for food, color in zip(food_reader, color_reader):
                if color[0] in food_colors:
                    food_colors[color[0]].append(food[0])
                else:
                    food_colors[color[0]] = [food[0]]
    except FileNotFoundError:
        pass

# CSV 파일에 음식 색깔 데이터를 저장하는 함수
def save_food_colors():
    with open('food.csv', mode='w', newline='', encoding='utf-8') as food_file, open('color.csv', mode='w', newline='', encoding='utf-8') as color_file:
        food_writer = csv.writer(food_file)
        color_writer = csv.writer(color_file)
        for color, foods in food_colors.items():
            for food in foods:
                food_writer.writerow([food])
                color_writer.writerow([color])

# 음식 색깔을 출력하는 함수
def get_food_color(food):
    for color, foods in food_colors.items():
        if food in foods:
            return color
    return None

# 새로운 음식을 등록하는 함수
def add_new_food(food, color):
    if color in food_colors:
        food_colors[color].append(food)
    else:
        food_colors[color] = [food]
    save_food_colors()

# 초기화 시 음식 색깔 데이터를 로드
load_food_colors()

# 테스트
food = input("음식을 입력하세요: ")
color = get_food_color(food)

if color:
    print(f"{food}의 색깔은 {color}입니다.")
else:
    print(f"{food}는 목록에 없습니다.")
    add_food = input("새로운 음식을 등록하시겠습니까? (예/아니오): ")
    if add_food.lower() == "예":
        new_color = input("음식의 색깔을 입력하세요: ")
        add_new_food(food, new_color)
        print(f"{food}가 {new_color}으로 등록되었습니다.")
    else:
        print("음식 등록이 취소되었습니다.")