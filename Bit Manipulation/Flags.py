# FLAGS

NEURAL_READ = 0b1000
NEURAL_WRITE = 0b0100
NEURAL_EXEC = 0b0010
NEURAL_CHANGE = 0b0001

def myfunction(permission):
    print(bin(permission))
    
if __name__ == '__main__':
    myfunction(NEURAL_WRITE | NEURAL_READ)
