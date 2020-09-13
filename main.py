from hwltd.reports import *
if __name__ == '__main__':
    root=HelloWorld #the root of the organization
    # To enter worker to root:
    myProject = Hello_World(r'C:\Users\Sharon Eshel\Downloads\prework-python-data.txt')

    #using the root
    a = root.get_workers()[0]
    print(a.get_salary())
    print(hwltd.reports.get_average_salary(root))
    #  hwltd.organization.HRDepartment.get_workers()
    hwltd.reports.get_num_employees('engineering', 3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
