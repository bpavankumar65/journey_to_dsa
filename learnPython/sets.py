def set_exaple(exam, project):
    print(exam, project)
    print("both exams and prpject are submitted by", (exam & project))
    print("who only given exam", (exam - project))
    print("Which students only submitted the project?", (project - exam))
    print("List all students who took either (or both) of the exam and the project", (exam | project))
    print("List all students who took either (but not both) of the exam and the project.", (project ^ exam))
    exam.add("srilekha")
    project1 = project.copy()
    if project1.intersection(project) == project1:
        print("yes its a subset")
    if "rajesh" in exam:
        exam.remove("rajesh")

    for elem in exam:
        print("each person in exam", elem)


def find_largest_common_prefix(list_ofthe_strings):
    shortest_string = min(list_of_strings, key=len)
    if list_ofthe_strings is None:
        return ''
    for i in range(len(shortest_string)):
        for elem in list_ofthe_strings:
            if elem[i] == shortest_string[i]:
                continue
            else:
                return shortest_string[:i]


def find_largest_prefix(str_list):
    if str_list is None:
        return ''
    shortest_string = min(str_list, key=len)
    for i, char in enumerate(shortest_string):
        if str_list[0][i] != char:
            return shortest_string[:i]


if __name__ == "__main__":
    exam = {'pavan', 'rajesh', 'jagadeesh', 'gautam'}
    project = {'pavan', 'jagadeesh', 'madhuri', 'samatha'}
    list_of_strings = ['pqrxyz', 'pqrabc', 'pqs']
    set_exaple(exam, project)
    print(find_largest_common_prefix(list_of_strings))
    print(find_largest_prefix(list_of_strings))
