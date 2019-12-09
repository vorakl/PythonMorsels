class Point(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, obj):
        return (self.x == obj.x) and (self.y == obj.y) and (self.z == obj.z)

    def __add__(self, obj):
        return Point(self.x+obj.x, self.y+obj.y, self.z+obj.z)

    def __sub__(self, obj):
        return Point(self.x-obj.x, self.y-obj.y, self.z-obj.z)
