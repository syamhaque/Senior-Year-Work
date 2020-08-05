import copy
#Dictionary to hold diagram relations.
relations = {
    "parallel": [],
    "perpendicular": [],
    "equal": [],
    "fraction": [],
    "sum_value": [],
    "similar" : [],
    "congruent": [],
    "tan": []
}

#CONSTANTS
#line segments
SB24 = "sb2_4"
SB1 = "sb1"
SB3 = "sb3"
SA14 = "sa1_4"
SA2 = "sa2"
SA3 = "sa3"
SC34 = "sc3_4"
SC1 = "sc1"
SC2 = "sc2"
LINE_SET = {SB24, SB1, SB3, SA14, SA2, SA3, SC34, SC1, SC2}
#angles
A1 = "a1"
B1 = "b1"
C1 = "c1"
A2 = "a2"
B2 = "b2"
C2 = "c2"
A3 = "a3"
B3 = "b3"
C3 = "c3"
A4 = "a4"
B4 = "b4"
C4 = "c4"
ANGLE_SET = {A1, B1, C1, A2, B2, C2, A3, B3, C3, A4, B4, C4}
#areas
AR1 = "ar1"
AR2 = "ar2"
AR3 = "ar3"
AR4 = "ar4"
AREA_SET = {AR1, AR2, AR3, AR4}
#Shapes
TR1 = "tr1" #outer triangle 
TR2 = "tr2" #inner triangle
#Dictionary Keys
PARALLEL = "parallel"
PERPENDICULAR = "perpendicular"
EQUAL = "equal"
FRACTION = "fraction"
SUM_VALUE = "sum_value"
SIMILAR = "similar"
CONGRUENT = "congruent"
TAN = "tan"
#Null
NULL = "null"

#Helper variables
MAX_PERPENDICULAR = 2 #Only two lines belonging to diff triangles can be perpendicular
is_right_TR1 = False #True if TR1 is a right triangle
is_right_TR2 = False #True if TR2 is a right triangle
perpendicular_count = 0 #How many lines belonging to two diff triangles are perpendicular. (Must be less than MAX_PERPENDICULAR)
RECURSION_LIMIT = 10 #HERE
recursion_count = 0  #HERE

#Adds value to corresponding key in relations dictionary as long as it doesn't already exist.
def add_value(key, value):
    if relations[key].count(value) == 0:
        relations[key].append(value)

#Checks if the relations dictionary contains the value in the array corresponding to key.
def contains(key, value):
    if relations[key].count(value) > 0:
        return True
#Make a triangle equilateral
def make_equilateral(name1):
    if name1 == AR1:
        set_equal(SA14, SB1)
        set_equal(SB1, SC1)
        set_equal(A1, B1)
        set_equal(B1, C1)
        set_sum_value(A1, B1, 120)
        set_sum_value(B1, C1, 120)
    elif name1 == AR2:
        set_equal(SA2, SB24)
        set_equal(SB24, SC2)
        set_equal(A2, B2)
        set_equal(B2, C2)
        set_sum_value(A2, B2, 120)
        set_sum_value(B2, C2, 120)
    elif name1 == AR3:
        set_equal(SA3, SB3)
        set_equal(SB3, SC34)
        set_equal(A3, B3)
        set_equal(B3, C3)
        set_sum_value(A3, B3, 120)
        set_sum_value(B3, C3, 120)
    elif name1 == AR4 or name1 == TR2:
        set_equal(SA14, SB24)
        set_equal(SB24, SC34)
        set_equal(A4, B4)
        set_equal(B4, C4)
        set_sum_value(A4, B4, 120)
        set_sum_value(B4, C4, 120)
    elif name1 == TR1:
        set_equal(A2, B3)
        set_equal(B3, C1)
        set_sum_value(A2, B3, 120)
        set_sum_value(B3, C1, 120)

#Make parallelogram made up of 2 areas
def make_parallelogram(name1, name2):
    if name1 == AR1 and name2 == AR4:
        set_equal(C1, A4)
        set_equal(SC1, SC34)
        set_equal(SB1, SB24)
    elif name1 == AR2 and name2 == AR4:
        set_equal(A2, B4)
        set_equal(SC2, SC34)
        set_equal(SA2, SA14)
    elif name1 == AR3 and name2 == AR4:
        set_equal(B3, C4)
        set_equal(SB3, SB24)
        set_equal(SA3, SA14)

def set_parallel(name1, name2):
    if (name1 == SA14 and (name2 == SA2 or name2 == SA3) or
        (name1 == SA2 or name1 == SA3) and name2 == SA14):
            add_value(PARALLEL, [SA14, SA2])
            add_value(PARALLEL, [SA14, SA3])
    elif (name1 == SB24 and (name2 == SB1 or name2 == SB3) or
        (name1 == SB1 or name1 == SB3) and name2 == SB24):
            add_value(PARALLEL, [SB24, SB1])
            add_value(PARALLEL, [SB24, SB3])
    elif (name1 == SC34 and (name2 == SC1 or name2 == SC2) or
        (name1 == SC1 or name1 == SC2) and name2 == SC34):
            add_value(PARALLEL, [SC34, SC1])
            add_value(PARALLEL, [SC34, SC2])
    else :
        add_value(PARALLEL, [NULL])
    #If all 3 inner triangle sides are parallel to outer triangle sides, make triforce.
    if (contains(PARALLEL, [SA14, SA2]) and 
        contains(PARALLEL, [SB24, SB1]) and 
        contains(PARALLEL, [SC34, SC1])):
            #make line segments equilateral
            make_equilateral(AR1)
            make_equilateral(AR2)
            make_equilateral(AR3)
            make_equilateral(AR4)
            make_equilateral(TR1)
            set_equal(SA2, SA3)
            set_equal(SB3, SB1)
            set_equal(SC1, SC2)
            #make the areas equal.
            set_equal(AR1, AR2)
            set_equal(AR2, AR3)
            set_equal(AR3, AR4)
            #make the triangle similar
            add_value(SIMILAR, [TR1, TR2])
            #make the triangles formed by each area congruent
            add_value(CONGRUENT, [AR1, AR2])
            add_value(CONGRUENT, [AR2, AR3])
            add_value(CONGRUENT, [AR3, AR4])
            #make all angles equal
            set_equal(A1, A2)
            set_equal(A2, A3)
            set_equal(A3, A4)
            #make sum values of angles equal to 120
            set_sum_value(A1, A2, 120)
            set_sum_value(A2, A3, 120)
            set_sum_value(A3, A4, 120)
    #If only two sides are parallel, make parallelogram.
    elif (contains(PARALLEL, [SA14, SA2]) and 
        contains(PARALLEL, [SB24, SB1])):
            make_parallelogram(AR3, AR4)
    elif (contains(PARALLEL, [SC34, SC1]) and 
        contains(PARALLEL, [SB24, SB1])):
            make_parallelogram(AR1, AR4)
    elif (contains(PARALLEL, [SA14, SA2]) and 
        contains(PARALLEL, [SC34, SC1])):
            make_parallelogram(AR2, AR4)

def set_perpendicular(name1, name2):
    global perpendicular_count
    global recursion_count #FROM HERE
    recursion_count += 1
    if recursion_count > RECURSION_LIMIT:
        return#TO HERE
    if perpendicular_count < MAX_PERPENDICULAR or not is_right_TR1 or not is_right_TR2:
        if (name1 == SA14 or name2 == SA14):
            if(name1 == SB1 or name1 == SB3 or name2 == SB1 or name2 == SB3):
                add_value(PERPENDICULAR, [SA14, SB1])
                add_value(PERPENDICULAR, [SA14, SB3])
                set_sum_value(B4, C3, 90)
                perpendicular_count += 1
            elif(name1 == SC1 or name1 == SC2 or name2 == SC1 or name2 == SC2):
                add_value(PERPENDICULAR, [SA14, SC1])
                add_value(PERPENDICULAR, [SA14, SC2])
                set_sum_value(C2, C4, 90)
                perpendicular_count += 1
            elif((name1 == SB24 or name2 == SB24) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA14, SB24])
                set_sum_value(A4, B4, 90)
                is_right_TR2 = True
            elif((name1 == SC34 or name2 == SC34) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA14, SC34])
                set_sum_value(A4, C4, 90)
                is_right_TR2 = True
        elif(name1 == SB24 or name2 == SB24):
            if(name1 == SA2 or name1 == SA3 or name2 == SA2 or name2 == SA3):
                add_value(PERPENDICULAR, [SA2, SB24])
                add_value(PERPENDICULAR, [SA3, SB24])
                set_sum_value(A3, A4, 90)
                perpendicular_count += 1
            elif(name1 == SC1 or name1 == SC2 or name2 == SC1 or name2 == SC2):
                add_value(PERPENDICULAR, [SB24, SC1])
                add_value(PERPENDICULAR, [SB24, SC2])
                set_sum_value(A1, C4, 90)
                perpendicular_count += 1
            elif((name1 == SA14 or name2 == SA14) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA14, SB24])
                set_sum_value(A4, B4, 90)
                is_right_TR2 = True
            elif((name1 == SC34 or name2 == SC34) and not is_right_TR2):
                add_value(PERPENDICULAR, [SB24, SC34])
                set_sum_value(B4, C4, 90)
                is_right_TR2 = True
        elif(name1 == SC34 or name2 == SC34):
            if(name1 == SA2 or name1 == SA3 or name2 == SA2 or name2 == SA3):
                add_value(PERPENDICULAR, [SC34, SA2])
                add_value(PERPENDICULAR, [SC34, SA3])
                set_sum_value(A4, B2, 90)
                perpendicular_count += 1
            elif(name1 == SB1 or name1 == SB3 or name2 == SB1 or name2 == SB3):
                add_value(PERPENDICULAR, [SC34, SB1])
                add_value(PERPENDICULAR, [SC34, SB3])
                set_sum_value(B1, B4, 90)
                perpendicular_count += 1
            elif((name1 == SA14 or name2 == SA14) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA14, SC34])
                set_sum_value(A4, C4, 90)
                is_right_TR2 = True
            elif((name1 == SB24 or name2 == SB24) and not is_right_TR2):
                add_value(PERPENDICULAR, [SB24, SC34])
                set_sum_value(B4, C4, 90)
                is_right_TR2 = True
        elif((name1 == SC2 or name2 == SC2) and (name1 == SA2 or name2 == SA2) and not is_right_TR1):
            add_value(PERPENDICULAR, [SA2, SC2])
            set_sum_value(B2, C2, 90)
            set_sum_value(B3, C1, 90)
            is_right_TR1 = True
        elif((name1 == SA3 or name2 == SA3) and (name1 == SB3 or name2 == SB3) and not is_right_TR1):
            add_value(PERPENDICULAR, [SA3, SB3])
            set_sum_value(A3, C3, 90)
            set_sum_value(A2, C1, 90)
            is_right_TR1 = True
        elif((name1 == SB1 or name2 == SB1) and (name1 == SC1 or name2 == SC1) and not is_right_TR1):
            add_value(PERPENDICULAR, [SB1, SC1])
            set_sum_value(A1, B1, 90)
            set_sum_value(A2, B3, 90)
            is_right_TR1 = True
        else:
            add_value(PERPENDICULAR, [NULL]) 
    else :
        add_value(PERPENDICULAR, [NULL])

def set_equal(name1, name2):
    if ((name1 in LINE_SET and name2 not in LINE_SET)
    or (name1 in ANGLE_SET and name2 not in ANGLE_SET)
    or (name1 in AREA_SET and name2 not in AREA_SET)):
        add_value(EQUAL, [NULL])
    else:
        add_value(EQUAL, [name1, name2])

def set_fraction(name1, name2, fraction):
    if ((name1 in LINE_SET and name2 not in LINE_SET)
    or (name1 in ANGLE_SET and name2 not in ANGLE_SET)
    or (name1 in AREA_SET and name2 not in AREA_SET)
    or fraction <= 0):
        add_value(FRACTION, [NULL])
    else:
        add_value(FRACTION, [name1, name2, fraction])

def set_sum_value(name1, name2, sum):
    #name1 and name 2 must be from the same set (i.e. both angles or both lines etc.).
    if ((name1 in LINE_SET and name2 not in LINE_SET)
    or (name1 in ANGLE_SET and name2 not in ANGLE_SET)
    or (name1 in AREA_SET and name2 not in AREA_SET)
    or (name1 in ANGLE_SET and name2 in ANGLE_SET and sum >= 180)
    or sum <= 0):
        add_value(SUM_VALUE, [NULL])
    else:
        add_value(SUM_VALUE, [name1, name2, sum])
    #Angles in triangles add up to 180. So do angles that form a straight line. Thus, certain sums can be inferred.
    if ((name1 == A1 and name2 == C1) or (name1 == C1 and name2 == A1)):
        add_value(SUM_VALUE, [B4, C3, sum])
        #make perpendicular where applicable. Check if already perpendicular to avoid infinite recursion.
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SB1]):
            set_perpendicular(SA14, SB1)
    elif ((name1 == B4 and name2 == C3) or (name1 == C3 and name2 == B4)):
        add_value(SUM_VALUE, [A1, C1, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SB1]):
            set_perpendicular(SA14, SB1)
    elif ((name1 == A2 and name2 == C2) or (name1 == C2 and name2 == A2)):
        add_value(SUM_VALUE, [A3, A4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA2, SB24]):
            set_perpendicular(SA2, SB24)
    elif ((name1 == A3 and name2 == A4) or (name1 == A4 and name2 == A3)):
        add_value(SUM_VALUE, [A2, C2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA2, SB24]):
            set_perpendicular(SA2, SB24)
    elif ((name1 == A2 and name2 == B2) or (name1 == B2 and name2 == A2)):
        add_value(SUM_VALUE, [A1, C4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB24, SC2]):
            set_perpendicular(SB24, SC2)
    elif ((name1 == A1 and name2 == C4) or (name1 == C4 and name2 == A1)):
        add_value(SUM_VALUE, [A2, B2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB24, SC2]):
            set_perpendicular(SB24, SC2)
    elif ((name1 == A3 and name2 == B3) or (name1 == B3 and name2 == A3)):
        add_value(SUM_VALUE, [B1, B4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB3, SC34]):
            set_perpendicular(SB3, SC34)
    elif ((name1 == B1 and name2 == B4) or (name1 == B4 and name2 == B1)):
        add_value(SUM_VALUE, [A3, B3, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB3, SC34]):
            set_perpendicular(SB3, SC34)
    elif ((name1 == B3 and name2 == C3) or (name1 == C3 and name2 == B3)):
        add_value(SUM_VALUE, [A4, B2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA3, SC34]):
            set_perpendicular(SA3, SC34)
    elif ((name1 == A4 and name2 == B2) or (name1 == B2 and name2 == A4)):
        add_value(SUM_VALUE, [B3, C3, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA3, SC34]):
            set_perpendicular(SA3, SC34)
    elif ((name1 == B1 and name2 == C1) or (name1 == C1 and name2 == B1)):
        add_value(SUM_VALUE, [C2, C4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SC1]):
            set_perpendicular(SA14, SC1)
    elif ((name1 == C2 and name2 == C4) or (name1 == C4 and name2 == C2)):
        add_value(SUM_VALUE, [B1, C1, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SC1]):
            set_perpendicular(SA14, SC1)
    elif ((name1 == A4 and name2 == B4) or (name1 == B4 and name2 == A4)):
        add_value(SUM_VALUE, [A1, C2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SB24]):
            set_perpendicular(SA14, SB24)
    elif ((name1 == A1 and name2 == C2) or (name1 == C2 and name2 == A1)):
        add_value(SUM_VALUE, [A4, B4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SB24]):
            set_perpendicular(SA14, SB24)
    elif ((name1 == B4 and name2 == C4) or (name1 == C4 and name2 == B4)):
        add_value(SUM_VALUE, [A3, B2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB24, SC34]):
            set_perpendicular(SB24, SC34)
    elif ((name1 == A3 and name2 == B2) or (name1 == B2 and name2 == A3)):
        add_value(SUM_VALUE, [B4, C4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB24, SC34]):
            set_perpendicular(SB24, SC34)
    elif ((name1 == A4 and name2 == C4) or (name1 == C4 and name2 == A4)):
        add_value(SUM_VALUE, [B1, C3, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SC34]):
            set_perpendicular(SA14, SC34)
    elif ((name1 == B1 and name2 == C3) or (name1 == C3 and name2 == B1)):
        add_value(SUM_VALUE, [A4, C4, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA14, SC34]):
            set_perpendicular(SA14, SC34)

#set_tan() does not apply to our diagrams so always add null value
def set_tan(name1, name2):
    add_value(TAN, [NULL])

####REMEMBER TO MAKEK GET_ALL RETURN NULL WHEN APPLICABLE.MAYBE FIX TRIFORCE(EX: PERPENDICULAR)###	
def get_all():
    global is_right_TR1
    global is_right_TR2
    global perpendicular_count
    global recursion_count#HERE
    #copy the dictionary and its contents to return after original is cleared
    dict = copy.deepcopy(relations)
    #clear dictionary and reset other variables
    for x in relations.values():
        x.clear()
    is_right_TR1 = False 
    is_right_TR2 = False 
    perpendicular_count = 0
    recursion_count = 0#HERE
    #return copy of relations dictionary or "null" if dictionary contains a "null" value
    for x in dict.values():
        if (x.count(["null"]) > 0):
            return "null"
    return dict 
    
def main():
    while(True):
        print("""
1: set parallel
2: set perpendicular
3: set equal
4: set fraction
5: set sum value
6: get all

Enter number of operation you would like to perform: """)
        op = input()
        if not op == '6':
            name1 = input("Enter name of first variable: ")
            name2 = input("Enter name of second variable: ")
        if op == '1':
            set_parallel(name1, name2)
        elif op == '2':
            set_perpendicular(name1, name2)
        elif op == '3':
            set_equal(name1, name2)
        elif op == '4':
            fraction = input("Enter fraction value: ")
            set_fraction(name1, name2, float(fraction))
        elif op == '5':
            sum = input("Enter sum value: ")
            set_sum_value(name1, name2, float(sum))
        elif op == '6':
            result = get_all()
            #Print result after checking if it is a string or a dictionary
            if isinstance(result, str):
                print(result)
            else:
                for x, y in result.items():
                    if len(y) == 0:
                        continue
                    print(x, y)
            break
        else:
            print("Please enter valid number.")
    

if __name__ == "__main__":
    main()
