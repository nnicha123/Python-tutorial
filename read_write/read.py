ipsum_file = open('files/ipsum.txt')

# for line in ipsum_file:
#     print(line.rstrip())

# # Restart at the top of the file
# ipsum_file.seek(0)
# # To read again
# lines = ipsum_file.readlines()
# print(lines)

# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)
# ipsum_file.close()

def sequence_filter(line):
    # Remove when > not in the line
    return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print (list(filter(sequence_filter,lines)))