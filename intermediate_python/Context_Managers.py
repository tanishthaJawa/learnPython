from contextlib import contextmanager
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('Enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception')
        #  print('exc:',exc_type,exc_val)
        print('exit')
        return True


with ManagedFile('notes.text') as file:
    print("Do some stuff todo...")
    file.write("Some todo...")
    file.somemethod()
print('continuing....')


@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try:
        yield f # all the code of enter function
    finally: # all the code of exit fucntion
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some toodoo')