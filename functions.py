import math 

def proportional_to_pixel(resolution:list, point:list) -> list:
    return [int(point[0] * resolution[0]), int(point[1] * resolution[1])]

def get_angle_from_3_points(p1:list,p2:list,p3:list,degrees=True) -> float:
    a2 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    b2 = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
    c2 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
    angle = math.acos((a2 + b2 - c2) / (2 * math.sqrt(a2) * math.sqrt(b2)))
    if degrees:
        return radians_to_degrees(angle)
    else:
        return angle
    
def radians_to_degrees(radians:float)->float:
    return math.degrees(radians)
