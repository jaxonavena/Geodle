from executive import Executive

def main():
    file_name = input("Enter a file name: ")
    executive = Executive(file_name)
    executive.run()
    executive.lists()

if __name__ == '__main__':
    main()

