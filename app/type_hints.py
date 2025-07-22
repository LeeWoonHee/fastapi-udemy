# udemy ep9

text: str = "value"
pert: int = 90
temp: float = 37.5

number: int | float = 12

digits : list[int] = [1,2,3,4,5]

table_5 : tuple[int,int,int,int,int] = (5,10,15,20,25)

city_temp : tuple[str,float] = ('city' : 20.5)

def root(num: int | float, exp: float | None = .5) -> float:
    return pow(num, exp)


root_25 = root(25)
