from typing import Any

# udemy ep9

class City : 
    def __init__(self,name,location):
        self.name = name
        self.location = location

text: str = "value"
pert: int = 90
temp: float = 37.5

number: int | float = 12

digits : list[int] = [1,2,3,4,5]

table_5 : tuple[int,...] = (5,10,15,20,25)
hampshire = City("hamspshire", 202424)
city_temp : tuple[City,float] = (hampshire,20.5)


shipment : dict[str,Any] = {
    "id": 123,
    "weight" : 1.2,
    "content": "wooden table",
    "status": "in transit"
}



def root(num: int | float, exp: float | None = .5) -> float:
    return pow(num, exp)

root_25 = root(25)

