# This is just a small Product Data Storage Software where we create a interface for Barcode scanner too
class Billing:
    __Product_ID = None
    __Product_Name = None
    __Product_Company = None
    __Product_Price = None

    #This is gonna be a Parent class for all type of Billing Info that we are gonna need here"

    def __init__(self):
        self.__Product_ID = None
        self.__Product_Name = None
        self.__Product_Company = None
        self.__Product_Price = None

    # This function will take input from user:
    def get_info(self):
        self.__Product_ID = input("Enter the value of Product Id:\t")
        self.__Product_Name = input("Enter the Name of Product:\t")
        self.__Product_Company = input("Enter the Name of Product Company:\t")
        self.__Product_Price = input("Enter the Price of Product:\t")

    # This will show Class content
    def display_info(self):
        print("The value of Product ID is:\t"+self.__Product_ID)
        print("The value of Product Name is:\t"+self.__Product_Name)
        print("The value of Product Company is:\t" + self.__Product_Company)
        print("The value of Product Price is:\t"+self.__Product_ID)


