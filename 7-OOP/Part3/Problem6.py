class FlexibleDict:
    def __init__(self):
        self.dic={}

    def __setitem__(self, key, value):
        if isinstance(key,str) and key.isdigit():
            self.dic[int(key)]=value
        else:
            self.dic[key] = value

    def __getitem__(self, key):
        if isinstance(key, str) and key.isdigit():
            if int(key) not in self.dic:
                raise ValueError('Index Not Found')
            return self.dic[int(key)]
        else:
            if key not in self.dic:
                raise ValueError('Index Not Found')
            return self.dic[key]

fd = FlexibleDict()
fd['a'] = 100
print(fd['a']) # Like regular dict
fd[5] = 500
print(fd[5]) # Like regular dict
fd[1] = 100
print(fd['1']) # actual Key is int but still trying to access through str key.
fd['1'] = 100
print(fd[1])
