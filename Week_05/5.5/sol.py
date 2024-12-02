# Week 5 - Unit 5: Exercise

def stopping_distance(spd: float) -> float:

    def reaction_path(spd: float):
        return spd * 0.3

    def brake_distance(spd: float):
        return (spd / 10) ** 2

    return reaction_path(spd) + brake_distance(spd)
    

speed = float(input("Enter speed in km/h: "))
print(f'Stopping Distance: {stopping_distance(speed)} m')