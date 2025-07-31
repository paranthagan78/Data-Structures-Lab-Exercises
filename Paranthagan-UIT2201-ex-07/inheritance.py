'''
This programi is to  build a model of real-time online 
shopping system using the concept of inheritance 
'''

class Product:
    '''This base class is as called Product and it contains 
    the name, price, and quantity of the product'''
    def __init__(self, name= '', price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items=[[self.name,self.price,self.quantity,self.price*self.quantity]]
    
    def get_name(self):
        '''to return the name of the product'''
        return self.name
    
    def get_price(self):
        '''to return the price of the product'''
        return self.price
    
    def get_quantity(self):
        '''to return the quantity of the product'''
        return self.quantity
    
    def total_price(self):
        '''to return the total price of the paroduct by multiplying
        the pice and quantity of the product'''
        return self.quantity * self.price
        
    def display_information(self):
        '''to return the information of the product'''
        print(f"name: {self.name}\n"
              f"price: {self.price}\n"
              f"quantity: {self.quantity}\n")

    def add_items(self,other):
        '''to add deatils of every product in a list'''
        if isinstance(other,Product):
            self.items.append([other.get_name(),
                                other.get_price(),
                                other.get_quantity(),
                                other.total_price()
                                ])
            
        elif isinstance(other, ElectronicProduct):    
            self.items.append([other.get_name(),
                                other.get_price(),
                                other.get_quantity(),
                                other.total_price(),
                                other.get_brand(),
                                other.get_model(),
                                ])
            
        elif isinstance(other, ClothingProduct):    
            self.items.append([other.get_name(),
                                other.get_price(),
                                other.get_quantity(),
                                other.total_price(),
                                other.get_size(),
                                other.get_color(),
                                ])
        
    def get_items(self):
        '''to return the list that contain details of the product'''
        return self.items
        
    def __add__(self,other):
        return self.get_name()+"-"+other.get_name() , self.total_price() + other.total_price()
        
class ElectronicProduct(Product):
    '''This base class is as called ElectronicProduct and it contains 
    the name, price, quantity, brand,model of the product'''
    def __init__(self, name, price, quantity, brand, model):#constructor code
        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model
        
    def display_information(self):
        '''to return the information of the product'''
        print(f"name: {self.name}\n"
              f"price: {self.price}\n"
              f"quantity: {self.quantity}\n"
              f"brand: {self.brand}\n"
              f"model: {self.model}\n")
        
    def get_name(self):
        '''to return the name of the product'''
        return super().get_name()
    
    def get_price(self):
        '''to return the price of the product'''
        return super().get_price()
    
    def get_quantity(self):
        '''to return the quantity of the product'''
        return super().get_quantity()
    
    def total_price(self):
        '''to return the total price of the paroduct by multiplying
        the pice and quantity of the product'''
        return super().total_price()
    
    def get_brand(self):
        '''to return the brand of the electronic product'''
        return self.brand
    def get_model(self):
        '''to return the model of ht electronic product'''
        return self.model
    
    def __add__(self,other):
        return self.get_name() +'-'+other.get_name() , self.total_price() + other.total_price()

class ClothingProduct(Product):
    '''This base class is as called ClothingProduct and it contains 
    the name, price, quantity, size, color of the product'''
    def __init__(self, name, price, quantity, size, color):
        super().__init__(name, price, quantity)
        self.size = size
        self.color = color
        
    def display_information(self):
        '''to return the information of the product'''
        print(f"name: {self.name}\n"
              f"price: {self.price}\n"
              f"quantity: {self.quantity}\n"
              f"brand: {self.size}\n"
              f"model: {self.color}\n")
        
    def get_name(self):
        '''to return the name of the product'''
        return super().get_name()
    
    def get_price(self):
        '''to return the price of the product'''
        return super().get_price()
    
    def get_quantity(self):
        '''to return the quantity of the product'''
        return super().get_quantity()
    
    def total_price(self):
        '''to return the total price of the paroduct by multiplying
        the pice and quantity of the product'''
        return super().total_price()
    
    def get_size(self):
        '''to return the size of the clothing product'''
        return self.size
    
    def get_color(self):
        '''to return the color of the clothing product'''
        return self.color
    
    def __add__(self,other):
        return self.get_name() +'-'+other.get_name() , self.total_price() + other.total_price()


#Driver code
if __name__ == "__main__":
    product = ["1.Milk","2.Butter","3.Ghee","4.Soap","5.Washing powder","6.Toothpaste"]
    e_product = ["1.Fridge","2.Air pod","3.Speaker","4.Ear phone","5.Mobile phone","6.Laptop"]
    c_product = ["1.Blazer","2.Hoodie","3.Jeans","4.T-shirt","5.Track","6.Shirt"]
    
    prod = Product()
    items = []
    while True:
        choice = int(input("Enter your Choice:\n1.General product\n2.Electronic product\n3.CLothing product\n4.Diplay bill\n"))
        
        if choice == 1:
            print(*product,sep = '\n')
            prod_choice = int(input("Enter your choice:"))
            prod_name = input("Enter product name: ")
            price = int(input("Enter the price: "))
            qty = int(input("Enter the quantity: "))
            prod_obj = Product(prod_name, price, qty)
            items.append(prod_obj)
            prod.add_items(prod_obj)

        elif choice == 2:
            print(*e_product, sep="\n")
            prod_choice = int(input("Enter your choice: "))
            prod_name = input("Enter product name: ")
            price = int(input("Enter the price: "))
            qty = int(input("Enter the quantity: "))
            brand = input("Enter the brand: ")
            model = input("Enter the model: ")
            prod_obj = ElectronicProduct(prod_name,price,qty,brand,model)
            items.append(prod_obj)
            prod.add_items(prod_obj)

        elif choice == 3:
            print(*c_product, sep="  ")
            prod_choice = int(input("Enter your choice: "))
            prod_name = input("Enter product name: ")
            price = int(input("Enter the price: "))
            qty = int(input("Enter the quantity: "))
            size = input("Enter the size: ")
            color = input("Enter the color: ")
            prod_obj = ClothingProduct(prod_name,price,qty,size,color)
            items.append(prod_obj)
            prod.add_items(prod_obj)

        elif choice == 4:
            values = []
            item_cl = prod.get_items()
            print(item_cl[1:])
            break

        else:
            print("Enter again!")
            continue
        