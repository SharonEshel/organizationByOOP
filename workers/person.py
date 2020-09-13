import re

class Phone:
    def __init__(self, phoneStr):
        # phone might start with + or a digit
        # hyphen can appear after a digit
        # the minimum numbers of digit are 8
        pattern = '^(\+|\d\-?)(\d\-?){7,}\d$'
        if re.match(pattern, phoneStr):
            self.phone=phoneStr
        else:
            raise Exception
            #self.phone=None

class Address:
    def __init__(self, country,city):
        self.country=country
        self.city=city

    def to_string(self):
        addDetails= self._additionalDetails()
        return "country: "+self.country +", city: "+self.city+ addDetails

    def _additionalDetails(self):
        raise NotImplementedError

class StreetAddress(Address):
    def __init__(self, country,city, streetName,  houseNumber):
        super().__init__(country,city)
        self.streetName=streetName
        self.houseNumber=houseNumber

    def _additionalDetails(self):
        return ", street name: "+self.streetName +", house number: "+self.houseNumber

class PobAddrees(Address):
    def __init__(self, country,city, postNumber):
        super().__init__(country,city)
        self.postNumber=postNumber

    def _additionalDetails(self):
        return ", post office box number: "+self.postNumber


class Person:
    IDnumber=0
    def __init__(self, firstName, lastName,birthYear,email,phones="",address=""):
        self.__firstName=firstName
        self.__lastName=lastName
        self._phones = []

        if self.isValidEmail(email):
            self.__email=email
        else:
            raise Exception(email+" invalid Email")
            print(email+" invalid Email")
        self._ID = self.raiseAndReturnID()


        if birthYear!="": #there is a birthYear parameter
            self.birthYear=birthYear

        if phones!="":#there is a phones parameter
            phonesList=phones.split(";")
            for phone in phonesList:
                temp=Phone(phone)
                if temp is not None:
                    self._phones.append(temp)

        if address!="":#there is an address parameter
            #self._address=address #go to setter-don't work
            addressList = address.split(";")
            if len(addressList) == 3:
                self._address = PobAddrees(addressList[0], addressList[1], addressList[2])
            elif len(addressList) == 4:
                self._address = StreetAddress(addressList[0], addressList[1], addressList[2], addressList[3])

    @property
    def address(self):
        return self._address.to_string()

    @address.setter
    def address(self, address):
        addressList = address.split(";")
        if len(addressList) == 3:
            self._address = PobAddrees(addressList[0], addressList[1], addressList[2])
        elif len(addressList) == 4:
            self._address = StreetAddress(addressList[0], addressList[1], addressList[2], addressList[3])
        print("in address setter")

    #without setter it should never be changed
    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def ID(self):
        return self._ID

    @property
    def email(self):
        return self.__email

    @property
    def phones(self):
        return self._phones

    def addPhone(self, phone):
        self._phones.append(phone)

    def removePhone(self, phone):
        self._phones.remove(phone)



    @classmethod
    def returnID(cls):
        return  cls.IDnumber

    @classmethod
    def raiseAndReturnID(cls):
        cls.IDnumber+=1
        return cls.IDnumber

    @staticmethod
    def isValidEmail(email):
        #email comtains: alpha-numeric chars+'@'+ subdomain(s)+ '.hwltd.com'
        #subdomain might contain digit, letters,and '-' not as first or last char
        pattern='^\w+@(([a-zA-Z0-9]+[\.-]?[a-zA-Z0-9]+)+|[a-zA-Z0-9])\.hwltd\.com$'
        return re.match(pattern, email)


#p1= Person("kohen", "rivka",  "abc@mail.hwltd.com", "1990","0986754545;+654575567;675495366","israel;betar; brim;89")
#p2=Person("kohen", "rivka",  "abc@mail.hwltd.com", "1990","0986754545;+654575567;675495366","israel;betar; brim;89")
#print(p1.firstName+" "+p1.lastName+" "+p1.email+" "+p1.address)
#print(p1.phones)
#for p in p1.phones:
 #   print(p.phone)

#print(p1.ID)
#print(p2.ID)