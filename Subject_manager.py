class subject():
    subjects = ['English', 'Urdu', 'Math']
    count = [1, 2, 3]
    # print(len(count))
    # print(len(subjects))

    while True:
        print('1: See all subject.')
        print('2: No of books.')
        print('3: Add subject.')
            
            
        user = int(input('Enter a num: '))
    
    
    
            
        if user ==  1:
            for subject in subjects:
                print(subject)    

        if user ==  2:
            if len(subjects) == len(count):
                no_books = len(subjects)
                print(f'There are {no_books} books.')
            else:
                print("There is any error")
                
                
        if user ==  3:
            new_book = str(input("Enter a book name: "))       
            subjects.append(new_book)
            count.append(4)
            print('Saved...') 
            
            