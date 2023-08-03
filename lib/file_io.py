def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode = 'a', encoding = 'utf-8') as logfile:
        logfile.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode = 'a', encoding = 'utf-8') as logfile:
        logfile.write(append_content)


def read_file(file_name):
    with open(f"{file_name}.txt",mode = 'r', encoding = 'utf-8') as logfile:
        return logfile.read()


write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
