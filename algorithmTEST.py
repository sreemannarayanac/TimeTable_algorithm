from algorithm import isLectures, sortByCategory
from template_functions import makeTemplate, set_subject, set_lunch, gen_time_table


#* Step 1: Inputs
syllabus = {  # L, T, P, A, C
    "NM": [3, 0, 0, 0, 3],  # slots by hours
    "IOT": [2, 0, 2, 0, 3],
    "COA": [3, 0, 0, 0, 3],
    "OS": [3, 0, 0, 0, 3],
    "CN": [3, 0, 2, 0, 4],
    "DAA": [3, 0, 2, 0, 4],
    "ES": [3, 0, 0, 0, 0],
    "CSD": [0, 0, 0, 6, 1]
}

# n_sets = int(input("Enter number of sets: "))
n_sets = 4

""" If number of sets is 3 or less than only one lunch slot for every set, else two lunch slots are needed to make more distinct sets. """
practicals = sortByCategory(syllabus, 3)
print(practicals)



#* Making sets
sets = []
for i in range(n_sets):
    sets.append(makeTemplate())

if n_sets <= 3 and n_sets > 0:
    for i in range(n_sets):
        set_lunch(sets[i][1], 1)
elif n_sets > 3 and n_sets <= 5:
    for i in range(3):
        set_lunch(sets[i][1], 1)
    for i in range(3, n_sets):
        set_lunch(sets[i][1], 2)

print(gen_time_table(sets[2][0]))