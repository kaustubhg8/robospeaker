import os

if __name__ == '__main__':
    print("Welcome to the Robo Speaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'q':
            os.system('wsay "bye bye"')
            break
        command = f'wsay "{x}"'
        os.system(command)
