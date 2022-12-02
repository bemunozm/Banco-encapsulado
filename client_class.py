class Client:
    def __init__(self,id,name,last_name,run,mail,bank,account_type="Vista",amount=0):
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__run = run
        self.__mail = mail
        self.__bank = bank
        self.__account_type = account_type
        self.__amount = amount

    def withdraw(self):
        print("--------MENU BANCARIO--------")
        print("1.- INGRESAR DINERO")
        print("2.- RETIRAR DINERO")
        print("SALDO ACTUAL: ",self.__amount)
        print("----------------")
        opcion = int(input("Ingrese la operacion que desea realizar: "))

        if(opcion==1):
            amount = int(input("Ingrese el monto a depositar: "))
            if(amount>0):
                self.__amount += amount
        elif(opcion==2):
            amount = int(input("Ingrese el monto a retirar: "))
            if(amount<=self.__amount):
                self.__amount -= amount
            elif(amount>self.__amount):
                print("Usted no posee el dinero suficiente para realizar este retiro")
        else:
            print("Ingrese una opcion valida!")

        print("Saldo actual: ",self.__amount)

    def show_info(self):
        print("Nombre cliente: ",self.__name,self.__last_name)
        print("RUT: ",self.__run)
        print("Correo: ",self.__mail)
        print("Banco: ",self.__bank," Cuenta: ",self.__account_type)
        print("Saldo actual: ",self.__amount)

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_run(self):
        return self.__run
    def get_mail(self):
        return self.__mail
    def get_bank(self):
        return self.__bank
    def get_account_type(self):
        return self.__account_type
    def get_amount(self):
        return self.__amount
    def set_id(self,id):
        self.__id = id
    def set_name(self,name):
        self.__name = name
    def set_last_name(self,last_name):
        self.__last_name = last_name
    def set_run(self,run):
            self.__run = run
    def set_mail(self,mail):
        self.__mail = mail
    def set_bank(self,bank):
        self.__bank = bank
    def set_account_type(self,account_type):
        self.__account_type = account_type
    def set_amount(self,amount):
        self.__amount = amount
