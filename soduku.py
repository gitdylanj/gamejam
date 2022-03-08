#Soduku time
import re
import sys
e = '*'
matrix = (
[[5, 3, e, e, 7, e, e, e, e], 
[6, e, e, 1, 9, 5, e, e, e],
[e, 9, 8, e, e, e, e, 6, e],
[8, e, e, e, 6, e, e, e, 3],
[4, e, e, 8, e, 3, e, e, 3],
[7, e, e, e, 2, e, e, e, 6],
[e, 6, e, e, e, e, 2, 8, e],
[e, e, e, 4, 1, 9, e, e, 5],
[e, e, e, e, 8, e, e, 7, 9]]
)

print('WELCOME TO SODUKU. INPUT A ROW AND COLUMN IN FORM(r, c, value) TO PLAY')

def check_columns(entry):
    '''
    Checks if an entry is valid in a column. Returns True if valid.
    '''
    return (entry[2] not in matrix[entry[1]] and matrix[entry[0]][entry[1]] == e)

def check_rows(entry):
    '''
    Checks if an entry is valid in a row. Returns True if valid.
    '''
    return (entry[2] not in matrix[entry[0]] and matrix[entry[0]][entry[1]] == e)

def check_grid(entry):
    ''''
    Checks if there are no duplicates of an entry in a 3x3 grid
    '''
    section_length = 3
    row_section = entry[0] // section_length
    column_section = entry[1] // section_length
    row_chunk = matrix[(row_section * section_length):(row_section + 1) * section_length]
    chunk = [i[(column_section * section_length):(column_section + 1) * section_length] for i in row_chunk]
    chunk_list = []
    for i in chunk:
        chunk_list = chunk_list + i
        
    # print(row_section)
    # print(column_section)
    print(chunk_list)
    return (entry[2] not in chunk_list)

while True:
    playarea = ''
    for r, s in enumerate(matrix):
        for c, s in enumerate(matrix[r]):
            slot =  '|' + str(matrix[r][c])
            playarea + slot
        playarea + '|\n'  
    print(playarea)

    user_input = input()
    temp = re.findall(r'\d+', user_input)
    entry = list(map(int, temp))

    if e not in matrix:
        print("You won")
        sys.exit()
    elif check_columns(entry) and check_rows(entry) and check_grid(entry):
        matrix[entry[0]][entry[1]] = entry[2]
        print(matrix)
    else:
        print("Invalid assignment. Please try again")

#This is a test of github
print('this is a test')