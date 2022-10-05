if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # summ = 0
    # for key, 
    # print(student_marks)
    marks = student_marks[query_name]
    print("{:.2f}".format(sum(marks)/3))
