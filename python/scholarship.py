def check_scholarship(string1, string2):
    student_id = string1.split(',')
    scholar_id = string2.split(',')
    if len(student_id)<len(scholar_id):
        return "Invalid data"
    non_scholars = []
    for i in student_id:
        if i not in scholar_id:
            non_scholars.append(i)
    if len(non_scholars)==0:
        return "All students have scholarships"
    else:
        return non_scholars

student_id = input()
scholar_id = input()
data = check_scholarship(student_id, scholar_id)
if isinstance(data, (str,)):
    print(data)
else:
    print("Students without scholarships: "+','.join(data))
