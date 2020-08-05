import D128 as d
import D228 as d2
####Test code by calling functions to affect diagram and using get_all() to retrieve results as shown below.

#print result to check that get_all() returned the correct value (either the dictionary or "null")
def print_result(result):
    if isinstance(result, str):
        print(result)
    else:
        for x, y in result.items():
            if len(y) == 0:
                continue
            print(x, y)
    print("")

d.set_parallel("sb2_4", "sb1")
d.set_parallel("sc3_4", "sc2")
d.set_parallel("sa1_4", "sa3")
result = d.get_all()
print_result(result)

d.set_perpendicular("sa1_4", "sb1")
d.set_perpendicular("sc3_4", "sb1")
d.set_perpendicular("sb2_4", "sa2")
d.set_tan("doesnt", "matter")
#d.set_sum_value("sc2", "a1", 180)
d.set_sum_value("a1", "c1", 90)
result = d.get_all()
print_result(result)

d2.set_parallel("sb2_3", "sa1")
d2.set_parallel("sc1_2", "sd3")
d2.set_parallel("sa2_3", "sb1")
result = d2.get_all()
print_result(result)

d2.set_perpendicular("sa2_3", "sa1")
d2.set_perpendicular("sc1_2", "sa1")
d2.set_perpendicular("sb2_3", "sb1")
d2.set_tan("doesnt", "matter")
#d.set_sum_value("sc2", "a1", 180)
d2.set_sum_value("a1", "b1", 90)
result = d2.get_all()
print_result(result)


