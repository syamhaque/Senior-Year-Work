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
SB23 = "sb2_3"
SA23 = "sa2_3"
SB1 = "sb1"
SA1 = "sa1"
SE3 = "se3"
SC12 = "sc1_2"
SC3 = "sc3"
SD3 = "sd3"
LINE_SET = {SB23, SA23, SB1, SA1, SE3, SC12, SC3, SD3}#CHANGED add this line
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
D3 = "d3"
E3 = "e3"
ANGLE_SET = {A1, B1, C1, A2, B2, C2, A3, B3, C3, D3, E3}#CHANGED add this line
#areas
AR1 = "ar1"
AR2 = "ar2"
AR3 = "ar3"
AREA_SET = {AR1, AR2, AR3}#CHANGED add this line
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
#C2 + E3 always = 360
RECURSION_LIMIT = 10
recursion_count = 0

#Adds value to corresponding key in relations dictionary. Does not add value if duplicate.
def add_value(key, value):
    if relations[key].count(value) == 0:
        relations[key].append(value)

#Checks if the relations dictionary contains the value in the array corresponding to key.
def contains(key, value):
    if relations[key].count(value) > 0:
        return True
add_value(SUM_VALUE, [C2, E3, 360])#CHANGED  
#Make a triangle equilateral
def make_equilateral(name1):
    if name1 == AR1:
        set_equal(SC12, SA1)
        set_equal(SA1, SB1)
        set_equal(A1, B1)
        set_equal(B1, C1)
        set_sum_value(A1, B1, 120)
        set_sum_value(B1, C1, 120)
    elif name1 == AR2 or name1 == TR2:
        set_equal(SA23, SB23)
        set_equal(SB23, SC12)
        set_equal(A2, B2)
        set_equal(B2, C2)
        set_sum_value(A2, B2, 120)
        set_sum_value(B2, C2, 120)
    elif name1 == AR3:
        set_equal(SE3, SA23)
        set_equal(SA23, SB23)
        set_equal(SB23, SC3)
        set_equal(SC3, SD3)
        set_equal(A3, B3)
        set_equal(B3, C3)
        set_equal(C3, D3)
        set_equal(D3, E3)
        set_sum_value(A3, B3, 216)
        set_sum_value(B3, C3, 216)
        set_sum_value(C3, D3, 216)
        set_sum_value(D3, E3, 216)
    elif name1 == TR1:
        set_equal(A1, C3)
        set_equal(C3, D3)
        set_sum_value(A1, C3, 120)
        set_sum_value(C3, D3, 120)

#Make parallelogram made up of 2 areas
def make_parallelogram(name1, name2):
    if name1 == AR1 and name2 == AR2:
        set_equal(A1, C2)
        set_equal(SB1, SA23)
        set_equal(SA1, SB23)

def set_parallel(name1, name2):
    if(name1 == SA23 and (name2 == SB1 or name2 == SC3) or
       name2 == SA23 and (name1 == SB1 or name1 == SC3)):
        add_value(PARALLEL, [SA23, SB1])
        add_value(PARALLEL, [SA23, SC3])
    elif((name1 == SC12 and name2 == SD3) or (name1 == SD3 and name2 == SC12)):
        add_value(PARALLEL, [SC12, SD3])
    elif(name1 == SB23 and (name2 == SA1 or name2 == SE3) or
       name2 == SB23 and (name1 == SA1 or name1 == SE3)):
        add_value(PARALLEL, [SB23, SA1])
        add_value(PARALLEL, [SB23, SE3])
    else:
        add_value(PARALLEL, [NULL])

    if(contains(PARALLEL, [SA23, SB1]) and
       contains(PARALLEL, [SB23, SA1]) and
       contains(PARALLEL, [SC12, SD3])):
        make_equilateral(AR1)
        make_equilateral(AR2)
        make_equilateral(TR1)
        set_equal(SB1, SC3)
        set_equal(SA1, SE3)
        set_equal(AR1,AR2)
        add_value(SIMILAR, [TR1,TR2])
        set_equal(A1, A2)
        set_equal(A2, A3)
        set_equal(B2, B3)
        set_equal(B3, C3)
        set_equal(C3, D3)
        set_sum_value(A1, A2, 120)
        set_sum_value(A2, A3, 120)
        set_sum_value(B2, B3, 120)
        set_sum_value(B3, C3, 120)
        set_sum_value(C3, D3, 120)
    elif(contains(PARALLEL, [SA23, SB1]) and
        contains(PARALLEL, [SB23, SA1])):
        make_parallelogram(AR1, AR2)

def set_perpendicular(name1, name2):
    global recursion_count
    recursion_count += 1
    if recursion_count > RECURSION_LIMIT:
        recursion_count = 0
        return
    global perpendicular_count
    global is_right_TR1
    global is_right_TR2
    if perpendicular_count < MAX_PERPENDICULAR or not is_right_TR1 or not is_right_TR2:
        if (name1 == SA23 or name2 == SA23):
            if(name1 == SA1 or name1 == SE3 or name2 == SA1 or name2 == SE3):
                add_value(PERPENDICULAR, [SA23, SA1])
                add_value(PERPENDICULAR, [SA23, SE3])
                set_sum_value(A2, C1, 90)
                perpendicular_count += 1
            elif((name1 == SC12 or name2 == SC12) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA23, SC12])
                set_sum_value(B2, C2, 90)
                is_right_TR2 = True
            elif((name1 == SB23 or name2 == SB23) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA23, SB23])
                set_sum_value(A2, B2, 90)
                is_right_TR2 = True
        elif(name1 == SC12 or name2 == SC12):
            if(name1 == SA1 or name1 == SE3 or name2 == SA1 or name2 == SE3):
                add_value(PERPENDICULAR, [SC12, SA1])
                add_value(PERPENDICULAR, [SC12, SE3])
                set_sum_value(A2, A3, 90)
                perpendicular_count += 1
            elif(name1 == SB1 or name1 == SC3 or name2 == SB1 or name2 == SC3):
                add_value(PERPENDICULAR, [SC12, SB1])
                add_value(PERPENDICULAR, [SC12, SC3])
                set_sum_value(B2, B3, 90)
                perpendicular_count += 1
            elif((name1 == SA23 or name2 == SA23) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA23, SC12])
                set_sum_value(B2, C2, 90)
                is_right_TR2 = True
            elif((name1 == SB23 or name2 == SB23) and not is_right_TR2):
                add_value(PERPENDICULAR, [SB23, SC12])
                set_sum_value(A2, C2, 90)
                is_right_TR2 = True
        elif(name1 == SB23 or name2 == SB23):
            if(name1 == SB1 or name1 == SC3 or name2 == SB1 or name2 == SC3):
                add_value(PERPENDICULAR, [SB23, SB1])
                add_value(PERPENDICULAR, [SB23, SC3])
                set_sum_value(B1, B2, 90)
                perpendicular_count += 1
            elif((name1 == SA23 or name2 == SA23) and not is_right_TR2):
                add_value(PERPENDICULAR, [SA23, SB23])
                set_sum_value(A2, B2, 90)
                is_right_TR2 = True
            elif((name1 == SC12 or name2 == SC12) and not is_right_TR2):
                add_value(PERPENDICULAR, [SB23, SC12])
                set_sum_value(A2, C2, 90)
                is_right_TR2 = True
        elif((name1 == SA1 or name2 == SA1) and (name1 == SB1 or name2 == SB1) and not is_right_TR1):
            add_value(PERPENDICULAR, [SA1, SB1])
            set_sum_value(B1, C1, 90)
            set_sum_value(C3, D3, 90)
            is_right_TR1 = True
        elif((name1 == SC3 or name2 == SC3) and (name1 == SD3 or name2 == SD3) and not is_right_TR1):
            add_value(PERPENDICULAR, [SC3, SD3])
            set_sum_value(A1, D3, 90)
            is_right_TR1 = True
        elif((name1 == SD3 or name2 == SD3) and (name1 == SE3 or name2 == SE3) and not is_right_TR1):
            add_value(PERPENDICULAR, [SD3, SE3])
            set_sum_value(A1, C3, 90)
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
        add_value(SUM_VALUE, [B2, B3, sum])
        #make perpendicular where applicable. Check if already perpendicular to avoid infinite recursion.
        if sum == 90 and not contains(PERPENDICULAR, [SC12, SC3]):
            set_perpendicular(SC12, SC3)
    elif ((name1 == B2 and name2 == B3) or (name1 == B3 and name2 == B2)):
        add_value(SUM_VALUE, [A1, C1, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SC12, SC3]):
            set_perpendicular(SC12, SC3)
    elif ((name1 == A1 and name2 == B1) or (name1 == B1 and name2 == A1)):
        add_value(SUM_VALUE, [A2, A3, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SC12, SE3]):
            set_perpendicular(SC12, SE3)
    elif ((name1 == A2 and name2 == A3) or (name1 == A3 and name2 == A2)):
        add_value(SUM_VALUE, [A1, B1, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SC12, SE3]):
            set_perpendicular(SC12, SE3)
    elif ((name1 == A2 and name2 == C2) or (name1 == C2 and name2 == A2)):
        add_value(SUM_VALUE, [B1, B3, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB23, SC12]):
            set_perpendicular(SB23, SC12)
    elif ((name1 == B1 and name2 == B3) or (name1 == B3 and name2 == B1)):
        add_value(SUM_VALUE, [A2, C2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SB23, SC12]):
            set_perpendicular(SB23, SC12)
    elif ((name1 == B2 and name2 == C2) or (name1 == C2 and name2 == B2)):
        add_value(SUM_VALUE, [A3, C1, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA23, SC12]):
            set_perpendicular(SA23, SC12)
    elif ((name1 == A3 and name2 == C1) or (name1 == C1 and name2 == A3)):
        add_value(SUM_VALUE, [B2, C2, sum])
        if sum == 90 and not contains(PERPENDICULAR, [SA23, SC12]):
            set_perpendicular(SA23, SC12)


#set_tan() does not apply to our diagrams so always add null value
def set_tan(name1, name2):
    add_value(TAN, [NULL])

#CHANGED replace your get_all() function with this one
#Call this function to return copy of relations dictionary and then reset dictionary and global variables.
def get_all():
    global is_right_TR1
    global is_right_TR2
    global perpendicular_count
    global recursion_count
    #copy the dictionary and its contents to return after original is cleared
    dict = copy.deepcopy(relations)
    #clear dictionary and reset other variables
    for x in relations.values():
        x.clear()
    is_right_TR1 = False 
    is_right_TR2 = False 
    perpendicular_count = 0
    add_value(SUM_VALUE, [C2, E3, 360])
    recursion_count = 0
    #return copy of relations dictionary or "null" if dictionary contains a "null" value
    for x in dict.values():
        if (x.count(["null"]) > 0):
            return "null"
    return dict
#CHANGED replace your main function with this one
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
