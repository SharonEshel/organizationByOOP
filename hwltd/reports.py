from hwltd.organization import *
import workers.structure
import hwltd.organization

def get_average_salary(group):
    workerList=group.get_workers()
    sum=0.0
    for worker in workerList:
        if type(worker.get_salary())==str:
            print (worker.get_salary())
        #print(worker.get_salary())
        sum+=worker.get_salary()

    return sum/len(workerList)

def get_relational_salary(worker):
    result={}
    emailWorker=worker.person.email
    myTeam=hwltd.organization.Employees.dictEmployees[emailWorker]
    for x, y in hwltd.organization.Employees.dictEmployees[emailWorker].items():
        if y==myTeam and x!=worker.person.email:
            result[x] = worker.get_salary()/hwltd.organization.Employees.dictEmployeesWorkers[x].get_salary()


def help_get_num_employees(department, depth):
    parentsList=[]
    if depth==1:
        print(department.name+": "+str(len(department.get_workers())))
    if depth == 2:
        print(department.name + ": " + str(len(department.get_workers())))
        for subgroup in department.subgroups:
            print("\t"+subgroup.name+": "+str(len(subgroup.get_workers())))
            parentsList.append(subgroup)
    if depth == 3:
        for subgroup in department.subgroups:
            print("\t" + subgroup.name + ": " + str(len(subgroup.get_workers())))
            for subsub in subgroup.subgroups:
                print("\t\t"+subsub.name + ": " + str(len(subsub.get_workers())))



def get_num_employees(department, depth):
    if department=='hr':
        help_get_num_employees(hwltd.organization.HRDepartment, depth)
    if department == 'engineering':
        help_get_num_employees(hwltd.organization.EngineeringDepartment, depth)
    else:
        help_get_num_employees(hwltd.organization.FinanceDepartment, depth)

