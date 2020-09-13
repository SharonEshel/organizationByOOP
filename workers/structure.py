import itertools
import workers.person
import sys


sys.setrecursionlimit(10000)

class Worker:
    def __init__(self,firstName, lastName,birthYear,email,phones,address, salary):
        self.person= workers.person.Person(firstName, lastName, birthYear, email, phones, address)
        self.salary=float(salary)


    def get_salary(self):
        return self.salary


class Engineer(Worker):
    def __init__(self,firstName, lastName,birthYear,email,phones,address,data): #data includes: salary;bonus
        dataList = data.split(";")
        super().__init__(firstName, lastName,birthYear,email,phones,address,dataList[0])
        self.bonus=float(dataList[1])


    def get_salary(self):
        self.salary+self.bonus
        return self.salary+self.bonus


class SalesPerson(Worker):
    def __init__(self,firstName, lastName,birthYear,email,phones,address,data): #data includes: salary;commission;number;number;...
        dataList = data.split(";")
        super().__init__(firstName, lastName,birthYear,email,phones,address,dataList[0])
        self.commission=dataList[1]
        self.deals=dataList[2:len(dataList)]

    def get_salary(self):
        sum=0
        for deal in self.deals:
            sum+=int(deal)
        return float(self.salary)+float(self.commission)*sum


class Group:
    def __init__(self, name,parentGroup,subgroups,description=""):
        self.name=name
        self.parentGroup=parentGroup
        self.subgroups=subgroups
        self.description=description #if subgroups contains workers description contain "workers" else ""

    def get_workers(self):
        if self.description=="workers":
            #print("workers")
            return self.subgroups
        else:
            res = []
            for g in self.subgroups:
                res = itertools.chain(res, g.get_workers())

            c = [*res]
            return c



    def get_parents(self):# returns list
        return list(self.help_parents_groups())

    def help_parents_groups(self):
        temp = self.parentGroup
        while not temp == None:
            yield temp.parentGroup
            temp = temp.parentGroup

