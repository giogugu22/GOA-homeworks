
class Car:
 def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False): 
        self._brand = brand
        self._model = model
        self._production_year = production_year
        self._color = color
        self._horse_power = horse_power
        self._is_sport_car = is_sport_car

 def get_details(self):
        return {
            "brand": self._brand,
            "model": self._model,
            "production_year": self._production_year,
            "color": self._color,
            "horse_power": self._horse_power,
            "is_sport_car": self._is_sport_car,}


def get_color(self):
        return self.__color     
        
        
def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        return False        
        




    


