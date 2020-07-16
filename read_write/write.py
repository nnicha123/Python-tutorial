# with open('files/write.txt','w') as write_file:
#     write_file.write('Hey there python is awesome')
#     write_file.write('\nI love it so much')
# with open('files/write.txt','a') as write_file:
#     write_file.write('\nYo there')

quotes = [
    '\nI can resist every temptation',
    '\nI can stand whatever comes my way',
    '\nBecause I know I am already living the dream',
]

with open('files/write.txt','a') as write_file:
    write_file.writelines(quotes)