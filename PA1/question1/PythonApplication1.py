import math


def calculate_angle(coordinates):
    if coordinates[0] != 0:
        calc_degree=math.degrees(math.atan2(coordinates[1],coordinates[0])) 
        return calc_degree if calc_degree>0 else calc_degree +360
    else:
        return 90 if coordinates[1]>0 else 270




def check_point_loc(coordinates):
    x=coordinates[0]
    y=coordinates[1]
    if(x**2+y**2>1):
        print("outside the unit circle")
    elif (x**2+y**2==1):
        print("on the unit circle")
    elif (x**2+y**2<1):
        print("in the unit circle")




if __name__ == '__main__':
    coordinates = tuple(map(float,input().split()))
    check_point_loc(coordinates)
    print(calculate_angle(coordinates))