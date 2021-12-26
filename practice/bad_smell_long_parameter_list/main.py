# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    class Unit:
        def __init__(self, field, x_coord, y_coord, is_fly, crawl, speed=1):
            self.field = field
            self.x_coord = x_coord
            self.y_coord = y_coord
            self.speed = speed

            if is_fly and crawl:
                raise ValueError('Рожденный ползать летать не должен!')
            if is_fly: self.speed *= 1.2
            if crawl: self.speed *= 0.5

        def move(self, direction):
            if direction == 'UP':
                new_y = y_coord + self.speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - self.speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - self.speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + self.speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
