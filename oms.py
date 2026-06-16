import json
import os
class Product:
    def __init__(self,pro_id,pro_name,category,price,stock):
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.category =category
        self.price =price
        self.stock  =stock
    
    def to_dict(self):
        return{
        "pro_id" : self.pro_id,
        "pro_name" : self.pro_name,
        "category": self.category,
        "price" : self.price,
        "stock" : self.stock
        }
    
class Product_management_system:
    FILE_NAME = "Product.json"

    def __init__(self):
        self.product = self.load_data()
        
       
       
        if self.product is None:
            self.product = []

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
            return []
        
    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.product, file,indent=5)

    def add_product(self):
        product_id=input("Enter the product ID: ")
        # for product in self.product:
        #     if product[product_id] == product_id:
        #         print("This product aldready exist. ")
        #         return
        pro_name = input("Enter the pro_Name: ")
        category = input("Enter the category: ")
        price = input("Enter the price: ")
        stock= input("Enter the stock: ")
        
        New_Product=Product(product_id,pro_name,category,price,stock)
        
        self.product.append(New_Product.to_dict())
        self.save_data()

        print("Product Added Sucessfully: ")
    
def view_product(self):
    if not self.product:
        print("No product record found.")
        return

    print("\n{:<8}{:<20}{:<20}{:<10}{:<10}".format(
        "ID", "Product Name", "Category", "Price", "Stock"))
    print("-" * 70)

    for product in self.product:
        print("{:<8}{:<20}{:<20}{:<10}{:<10}".format(
            product["pro_id"],
            product["pro_name"],
            product["category"],
            product["price"],
            product["stock"]
        ))
    
    def search_product(self):
        product_id=input("Enter the product_ID: ")
        for product in self.product:
            if product["pro_id"] == product_id:
                print("\nproduct is found. ")
                print(product)
                return
        print("product is not found. ")
    
    def update_product(self):
        product_id = input("Enter the product_ID: ")
        for product in self.product:
            if product["pro_id"] == product_id:
                product["pro_name"]=input(f"Enter the product name:")
                product["category"]=input(f"Enter the category:") 
                product["price"]=input(f"Enter the price:")
                product["stock"]=input(f"Enter the stock:")
                self.save_data()
                print("product updated. ")

                return
            print("product not found. ")
    def delete_product(self):
                product_id = input("Enter the product_ID to delete: ")
                for product in self.product:
                    if product["pro_id"] == product_id:
                        self.product.remove(product)
                        self.save_data()
                        print("product deleted Successfully. ")
                        return
                    print("product not found. ")

    def menu(self):
        while True:
            print("****Order_Management_System****")
            print("1. Add Product")
            print("2. View Product")
            print("3. Search Product")
            print("4. Update Product")
            print("5. Delete Product")
            print("6.Exit")

            choice=input("Enter the Choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_product()
            elif choice == "3":
                self.search_product()
            elif choice == "4":
                self.update_product()
            elif choice == "5":
                self.delete_product()
            elif choice == "6":
                print("Thankyou for using the product Management System")
            else:
                print("Your choice is invalid so please enter the correct choice. ")

if __name__ == '__main__':
    sms=Product_management_system()
    sms.menu()
    