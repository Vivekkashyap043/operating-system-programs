import random
def sequential_allocation():
 # Get the number of blocks
    n = int(input("Enter number of blocks: "))
 
 # Allocate blocks randomly (1 for allocated, 0 for not allocated)
    blocks = [random.randint(0, 1) for _ in range(n)]
 
    print("Initial block allocation:")
    print(blocks)
 
 # Get the number of files
    num_files = int(input("Enter number of files: "))
 
    for file_index in range(num_files):
 # Get the number of blocks the file will take
        num_blocks_needed = int(input(f"Enter number of blocks for file {file_index + 1}: "))
 
 # Find a sequence of free blocks
        start_block = -1
        for i in range(n - num_blocks_needed + 1):
            if all(block == 0 for block in blocks[i:i + num_blocks_needed]):
                start_block = i
                break
 
 # Allocate the blocks if a suitable sequence was found
        if start_block != -1:
            for i in range(start_block, start_block + num_blocks_needed):
                blocks[i] = 1
            print(f"File {file_index + 1} allocated blocks: {list(range(start_block, start_block + num_blocks_needed))}")
        else:
            print(f"File {file_index + 1} could not be allocated.")
sequential_allocation()