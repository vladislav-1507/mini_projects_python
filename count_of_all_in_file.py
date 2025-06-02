with open('file.txt') as file:
    content = file.read()
    lines = content.split('\n')
    words = ' '.join(lines).split()
    letters = list(filter(lambda x: x.isalpha(), ''.join(words)))
       
    
    print(f'''Input file contains:
{len(letters)} letters
{len(words)} words
{len(lines)} lines''')




