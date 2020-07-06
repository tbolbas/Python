class Customer:
    __count = 0

    def __init__(self):
        Customer.__count +=1
        self.__id =  Customer.__count
        self.__firstName = ""
        self.__secondName = ""
        self.__middleName = ""
        self.__address = ""
        self.__creditCardNumber = 0
        self.__balance = 0
        print("Пустой пользователь добавлен под номером №")

    def __init__(self,secondname,firstname,middlename,address,cardnumber,balance):
        Customer.__count += 1
        self.__id = Customer.__count
        self.__firstName = firstname
        self.__secondName = secondname
        self.__middleName = middlename
        self.__address = address
        self.__creditCardNumber = cardnumber
        self.__balance = balance
        print("Пользователь №" + str(self.__id) + " " + str(self.__secondName) + " " + str(self.__firstName)
              + " " + str(self.__middleName) +" добавлен")

    def __str__(self):
        return (str(self.__id) + " " + self.getSecondName() + " " + self.getFirstName() + " " + self.getMiddleName()
              + " " + self.getAddress() + " " + str(self.getCreditCardNumber()) + " " + str(self.getBalance()))

    def getId(self):
        return self.__id

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__secondName

    def getMiddleName(self):
        return self.__middleName

    def getCreditCardNumber(self):
        return self.__creditCardNumber

    def getBalance(self):
        return self.__balance

    def getAddress(self):
        return self.__address

    def setBalance(self,balance):
        self.__balance = balance


def sortCustomer(list):
    newList = sorted(list, key=lambda x:x.getSecondName())
    print("\nСортировка пользователей по фамилии в алфавитном порядке")
    print("Id Фамилия Имя Отчество Адресс Карта Баланс")
    for i in newList:
       print(i)


def getListWithBalanceInRange(list):
    a = int(input("\nНижняя граница баланса:\n"))
    b = int(input("Верхняя граница баланса:\n"))
    print("Пользователи с балансом в диапазоне ["+str(a)+"-"+str(b)+"]:" )
    newList=[]
    for i in list:
        if a<=i.getBalance()<=b:
            print(i)

"""---------------"""
customerList = [Customer("Aa","BB","CC","kjkj",79797,2),
     Customer("Hkhf","lwkl","iw","ywytw",98298,45),
     Customer("Oijhjfh","Ljskjf","Lo","kjkj",52652,827)]
newCust = Customer("Atrtra","uyuBB","nmnLo","kjkj",545452,6454)
customerList.append(newCust)

sortCustomer(customerList)
getListWithBalanceInRange(customerList)










