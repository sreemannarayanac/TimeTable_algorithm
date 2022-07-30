from template_functions import makeTemplate, set_subject, set_lunch

a, b, c = makeTemplate()

set_subject(b, 'A1', 'MATH', 3)
print(b["A1"][0].subject)
print(b["A1"][1].subject)
print(b["A1"][2].subject)
# set_subject(b, "L1", "PHYS1001P", 1)
# set_subject(b, 'A1', 'PHYS', 3)

# set_subject(b, 'A1', 'MATH', 3)
# print(b["L5"][0].subject)

set_lunch(b, 2)