import workers.structure
from hwltd.reports import *

#reference of the children. from children to parents
#white pointes
InfrastructureTeam=workers.structure.Group("Infrastructure Team",None,[],"workers")
AppTeam=workers.structure.Group("App Team",None,[],"workers")
DriversTeam=workers.structure.Group("Drivers Team",None,[],"workers")
QATeam=workers.structure.Group("QA Team",None,[],"workers")

ChipTeam=workers.structure.Group("Chip Team",None,[],"workers")
BoardTeam=workers.structure.Group("Board Team",None,[],"workers")
PowerTeam=workers.structure.Group("Power Team",None,[],"workers")

DesignTeam=workers.structure.Group("Design Team",None,[],"workers")
PocTeam=workers.structure.Group("Poc Team",None,[],"workers")

TechTeam=workers.structure.Group("Tech Team",None,[],"workers")
StaffTeam=workers.structure.Group("Staff Team",None,[],"workers")

IncomeTeam=workers.structure.Group("Income Team",None,[],"workers")
OutcomeTeam=workers.structure.Group("Outcome Team",None,[],"workers")

#black points
SWGroup=workers.structure.Group("SW Group",None,[InfrastructureTeam,AppTeam,DriversTeam,QATeam],"")
HWGroup=workers.structure.Group("HW Group",None,[ChipTeam,BoardTeam,PowerTeam],"")
CTOGroup=workers.structure.Group("CTO Group",None,[],"workers")
SystemGroup=workers.structure.Group("System Group",None,[DesignTeam,PocTeam],"")

RecruitmentGroup=workers.structure.Group("Recruitment Group",None,[TechTeam,StaffTeam],"")
CultureGroup=workers.structure.Group("Culture Group",None,[],"workers")

SalariesGroup=workers.structure.Group("Salaries Group",None,[],"workers")
BudgetGroup=workers.structure.Group("Budget Group",None,[IncomeTeam,OutcomeTeam],"")

#Black squares
EngineeringDepartment=workers.structure.Group("Engineering Department",None,[SWGroup,HWGroup,CTOGroup,SystemGroup],"")
HRDepartment=workers.structure.Group("HR Department",None,[RecruitmentGroup,CultureGroup],"")
FinanceDepartment=workers.structure.Group("Finance Department",None,[SalariesGroup,BudgetGroup],"")

HelloWorld=workers.structure.Group("Hello World",None,[EngineeringDepartment,HRDepartment,FinanceDepartment],"")

#reference of the parents. from parents to chilren
#Black squares
FinanceDepartment.parentGroup=HelloWorld
HRDepartment.parentGroup=HelloWorld
EngineeringDepartment.parentGroup=HelloWorld

#black points
BudgetGroup.parentGroup=FinanceDepartment
SalariesGroup.parentGroup=FinanceDepartment
CultureGroup.parentGroup=HRDepartment
RecruitmentGroup.parentGroup=HRDepartment
SystemGroup.parentGroup=EngineeringDepartment
CTOGroup.parentGroup=EngineeringDepartment
HWGroup.parentGroup=EngineeringDepartment
SWGroup.parentGroup=EngineeringDepartment

#white pointes
OutcomeTeam.parentGroup=BudgetGroup
IncomeTeam.parentGroup=BudgetGroup
StaffTeam.parentGroup=RecruitmentGroup
TechTeam.parentGroup=RecruitmentGroup
PocTeam.parentGroup=SystemGroup
DesignTeam.parentGroup=SystemGroup
PowerTeam.parentGroup=HWGroup
BoardTeam.parentGroup=HWGroup
ChipTeam.parentGroup=HWGroup
QATeam.parentGroup=SWGroup
DriversTeam.parentGroup=SWGroup
AppTeam.parentGroup=SWGroup
InfrastructureTeam.parentGroup=SWGroup


class Employees():
    dictEmployees = dict() #contains email:team
    dictEmployeesWorkers=dict()#contains email:worker

class Hello_World:
    def __init__(self,path):
        #adds the workers to their teams
        #adds employee to dictEmployees:{ email:team: }
        # adds employee to dictEmployees:{ email:workers }
        with open(path, 'r') as input_file:
            for line in input_file:
                if(line[0]!='#'):
                    self.add_employees(line)

    def addToTeam(self,worker,teamName):
        ListofTeams={'outcome':OutcomeTeam,'income':IncomeTeam,'staff':StaffTeam,'tech':TechTeam,'poc':PocTeam,'design':DesignTeam,'power':PowerTeam,'board':BoardTeam,'chip':ChipTeam,'qa':QATeam,'drivers':DriversTeam,'app':AppTeam,'infrastructure':InfrastructureTeam}
        for x,y in ListofTeams.items():
            if(x==teamName):
                y.subgroups.append(worker)
                return y
    def whichWorker(self,str):
        count = 0
        for i in str:
            if i == ';':
                count = count + 1
        return count

    def add_employees(self,line):
        data = line.split(',')
        if len(data)!=9:
          return
        #erase spaces
        i=0
        for d in data:
            data[i]=d.strip()
            data[i]=d.replace(" ", "")
            i+=1
        try:
            whichWorker=self.whichWorker(data[8])
            #create a worker
            if whichWorker==0: #staff

                worker=workers.structure.Worker(data[0],data[1],data[2],data[3],data[4],data[5],data[8])
                #print("in try")
                team=self.addToTeam(worker,data[6])
                Employees.dictEmployeesWorkers[worker.person.email]=worker
                Employees.dictEmployees[worker.person.email]=team
            elif whichWorker==1:# engineer
                worker=workers.structure.Engineer(data[0],data[1],data[2],data[3],data[4],data[5],data[8])
                team=self.addToTeam(worker,data[6])
                Employees.dictEmployeesWorkers[worker.person.email] = worker
                Employees.dictEmployees[worker.person.email] = team
            else:
                worker=workers.structure.SalesPerson(data[0],data[1],data[2],data[3],data[4],data[5],data[8])
                team=self.addToTeam(worker, data[6])
                Employees.dictEmployeesWorkers[worker.person.email] = worker
                Employees.dictEmployees[worker.person.email] = team

        except:
            print("an Exception")

