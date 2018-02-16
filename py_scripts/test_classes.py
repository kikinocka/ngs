class Whatever:
    att = 50
    coordinates = []
    
    def __init__(self, name, text, hit_start):
        self.name = name
        self.text = text
        self.hit_start = hit_start
    
    def __repr__(self):
        res = f'my name is {self.name}'
        return res
    
    def text_len(self):
        x = len(self.text)
        return x
    
    def set_coordinates(self, data):
        self.coordinates.append(data)
    
    def coo_as_string(self, dont):
        return '{0} {1} {0} {0}'.format(self.coordinates, dont)


list_of_coordinates = [('bla',10), ('test',15)]

x = Whatever('test', 'blabla', 5)

for i in list_of_coordinates:
    if i[0] == 'test':
        x.set_coordinates(i[1])
