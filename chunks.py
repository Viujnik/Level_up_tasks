def create_user_list():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    step = int(input("Enter the step number: "))
    user_list = [i for i in range(start, end, step)]
    return user_list

def chunks(lst, n):
    """Последовательные чанки размером n из lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

user_list = create_user_list()

n = int(input("Enter the len of chunks: "))

chunks = chunks(user_list, n)

if __name__ == "__main__":
    for i in range(len(user_list)//n):
        print(next(chunks))
