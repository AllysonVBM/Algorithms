def ReverseString(s):
    s = list(s)
    p1, p2 = 0, len(s) -1
    while p1 < p2:
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1
    return ''.join(s)


def main():
    test_cases = [
        "hello",            
        "world",            
        "racecar",          
        "SpaceX",           
        "rocket"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = ReverseString(test_case)
        print(f"Test case {i}: Original: '{test_case}' | Reversed: '{result}'")

if __name__ == "__main__":
    main()



# USING HIGH-LEVEL FUNCTION
# s = list('batata')
# s.reverse()
# print(s)