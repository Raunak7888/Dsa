def linear_search(nums,target):
    for i,num in enumerate(nums):
        if num == target:
            return i
    return -1

def main():
    print(linear_search([0,1,2,3,4,5,6,7,8,9],7))
    
if __name__ == "__main__":
    main()