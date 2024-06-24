import random
def linked_allocation():
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
 
 # Find free blocks
 free_blocks = [i for i, block in enumerate(blocks) if block == 0]
 
 # Allocate the blocks if there are enough free blocks
 if len(free_blocks) >= num_blocks_needed:
 allocated_blocks = free_blocks[:num_blocks_needed]
 for block in allocated_blocks:
 blocks[block] = 1
 print(f"File {file_index + 1} allocated blocks: {allocated_blocks}")
 else:
 print(f"File {file_index + 1} could not be allocated.")
linked_allocation()
