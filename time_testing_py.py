import timeit

my_setup = "from template_functions import makeTemplate, set_subject, set_lunch, gen_time_table"

my_statement = """a, b, c = makeTemplate() # a = dic (day wise), b = code_dic (code wise), c = filled_dic (filled code wise)

set_subject(b, c, 'A1', 'MATH', 3)
set_subject(b, c, 'L2', 'PHYS1001P', 1)

set_lunch(b, 1)"""

#timeit code here

print(timeit.timeit(my_statement, my_setup, number=9000))