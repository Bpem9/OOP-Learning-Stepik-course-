class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = self.__class__.__name__
    def __call__(self, next, *args, **kwargs):
        self.next_layer = next
        return self.next_layer

class Input(Layer):
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs

class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, first):
        self.first = first
    def __iter__(self):
        obj = self.first
        while obj:
            yield obj
            obj = obj.next_layer

it = Input(128)
nel = it(Dense(it.inputs, 500, 'linear'))
nel1 = nel(Dense(nel.inputs, 250, 'bilinear'))
nel2 = nel1(Input(500))
nel3 = nel2(Dense(nel2.inputs, 250, 'trilinear'))
for x in NetworkIterator(it):
    print(x.name)




