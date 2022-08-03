from template_functions import makeTemplate, set_subject, set_lunch

a, b, c = makeTemplate() # a = dic (day wise), b = code_dic (code wise), c = filled_dic (filled code wise)

set_subject(b, c, 'A1', 'MATH', 3)
set_subject(b, c, 'L2', 'PHYS1001P', 1)

set_lunch(b, 2)
print(c)
