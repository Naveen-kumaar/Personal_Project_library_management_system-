class Library():
    def __init__(self,list):
        self.bklist = list
        self.avbklist = list[:]
        self.bklen={}#key-book,#value-user name
    def display_all_books(self):
        print( self.bklist)
        for i in self.bklist:
            print(i)

    def display_available_books(self):
        for book in self.avbklist:
            print(book)

    def length_books(self,name,book):
        if book not in self.bklist:
            print("incorrect book name.please enter book list")
            return
        if book in self.avbklist:
            self.bklen.update({book:name})
            self.avbklist.remove(book)
            print("you can take the book ")
        else:
            print("The book is already taken by "+ self.bklen[book])

    def return_book(self,book):
        del self.bklen[book]
        self.avbklist.append(book)



if __name__=="__main__":
    lib = Library([" Deep in SQL","Depth of javascript","DBMS","Power of Coding","Crack Python","Clean Code"])
    print("Welcome to library.enter an option. ")
    while True:
        print("""
1.Display all books
2.Display available books
3.Borrow books
4.Return books
5.Quit""")
        client_choice=int(input("enter a value : "))
        if client_choice == 1:
            lib.display_all_books()
        elif client_choice == 2:
            lib.display_available_books()
        elif client_choice == 3:
            name = input("Enter your name : ")
            book = input("Enter book name : ")
            lib.length_books(name,book)
        elif client_choice == 4:
            book=input("Enter the name of the book")
            lib.return_book(book)
        elif client_choice == 5:
            break
        else:
            print("please enter a correc value")


