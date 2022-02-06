
h = open(file='/home/phyzician/LearnGB/pythonMyProject/pythonProject/shure_eq/shure50_1.feq', mode='w')
with open(file='/home/phyzician/LearnGB/pythonMyProject/pythonProject/shure_eq/shure50.feq', mode='r') as f:
    list = f.readlines()
for i in list:
    a = str(int(i)+1)
    h.write(a)
    h.write('\n')
h.close()

    
