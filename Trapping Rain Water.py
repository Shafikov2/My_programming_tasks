def trap(height):
    max_height = 0
    max_height_index = 0
    sum_water = 0

    for i in range(len(height)):
        if height[i] > max_height:
            max_height = height[i]
            max_height_index = i

    temp_height = height[0]  # текущая высота = высоте первого
    for i in range(0, max_height_index):  # идем слева направо до максимума и считаем:
        if height[i] > temp_height:  # если столбик выше чем текущая высота
            temp_height = height[i]  # то текущая высота равна текущему столбику
        else:  # иначе
            sum_water += temp_height - height[i]  # сумма воды равна += текущая высота - высота столбика

    temp_height = height[len(height)-1]

    for i in range(len(height) - 1, max_height_index,-1):
        if height[i] > temp_height:
            temp_height = height[i]
        else:
            sum_water += temp_height - height[i]
    return sum_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))
