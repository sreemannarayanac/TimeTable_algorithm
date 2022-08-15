
"""  

1. Inputs needed
inputData = {
    "Subject1": ["L", "T", "P", "A", "C"],   # L - lectures, T - Tutorial, P - Practical, C - Credits 
    "Subject2": ["L", "T", "P", "A", "C"],
}
Know number of sets
assign lunch slot

2. Processing given data
totalLectures =
totalPracticals =
greater of lectures and practicals
whichever is greater that will be given maximum preference before lunch 

3. Assigning Labs
According to preference assign lab slots (either left or right of lunch)
assigning of lab slots should be done in descending order of number of practicals, using related slots

4.

INDIVIDUAL WORKS
Akshith:
    1. Write a sorting algorithm, preference -> P, L, A
    2. 

Sreeman:
    1.  Assigning lunch slot
    2.  Assigning lab slots
    3.
"""


#* Step 2: Processing given data
def sortByCategory(syllabus: dict, category: int) -> dict:
    """ Takes in two arguments, syllabus and category, and returns a dictionary of sorted syllabus according to category \n categor 1 -> lectures, 2 -> tutorials, 3 -> practicals, 4 -> activities """
    practLec = set()
    subs = []
    resDict = {}

    for key in syllabus.keys():
        if syllabus[key][category-1]>0:
            obj = syllabus[key][category-1]
            practLec.add(obj)

    while (len(practLec) > 0):
        maxCredit = max(practLec)
        practLec.remove(maxCredit)

        for key in syllabus.keys():
            if syllabus[key][category-1] == maxCredit:
                subs.append(key)

    for i in subs:
        resDict[i] = syllabus[i]

    return resDict

def isLectures(syllabusInput) -> bool:
    """ Notifies whether if total number of lectures are greater than total number of practicals """
    l, p = None, None
    for details in syllabusInput.values():
        l += details[0]
        p += details[2]
    if l > p:
        return True
    return False