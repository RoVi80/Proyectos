def fine_calculator(area,speed):

    urban_limit = 50
    expressway_limit = 100
    motorway_limit = 120
    urban_coe = 1
    express_coe = 0.8
    motor_coe = 0.5


    
    if not isinstance(area, str):
        return "Invalid Area Type"

    if not area.islower():
        return "Invalid Area Value"
    if (area != "urban") and (area != "expressway") and (area != "motorway"):
        return "Invalid Area Value"

    if isinstance(speed, int) or isinstance(speed, float):
        if speed < 0:
            return "Invalid Speed Value"
        if area == "urban" and speed < urban_limit:
            return 0
        if area == "expressway" and speed < expressway_limit:
            return 0
        if area == "motorway" and speed < motorway_limit:
            return 0
        
    else:
        return "Invalid Speed Type"
    

    if area == "urban" and speed > urban_limit:
        os = speed - urban_limit
        porcentaje = (os / urban_limit) * 100
        multa = urban_coe * porcentaje ** 2

    if area == "expressway" and speed > expressway_limit:
        os = speed - expressway_limit
        porcentaje = (os / expressway_limit) * 100
        multa = express_coe * porcentaje ** 2

    if area == "motorway" and speed > motorway_limit:
        os = speed - motorway_limit
        porcentaje = (os / motorway_limit) *100
        multa = motor_coe * porcentaje ** 2

    return round(multa)
    
print(fine_calculator("expressway", 119))