def BinarySearch(guessNumber):
    guessNumber = int(guessNumber)

    low_hint, high_hint = 0, 1000
    attempt = 0
    
    while low_hint <= high_hint and attempt < 10:
        mid = (low_hint + high_hint) // 2

        print(f"Attempt {attempt + 1}: Current range [{low_hint}, {high_hint}], middle: {mid}")
        
        if guessNumber == mid:
            print(f"The number you chose is {mid}. You win! Congratulations!!")
            return
        
        elif guessNumber > mid:
            low_hint = mid + 1
        
        else:
            high_hint = mid - 1
        
        attempt += 1
    
    print("Number of attempts exceeded or the number was not found.")


if __name__ == "__main__":
    choose = input("Enter a number from 0 to 1000: \n")
    BinarySearch(choose)
