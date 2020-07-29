class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __sub__(self, other):
        return Points(*(a - b for a, b in zip(self, other)))

    def dot(self, other):
        return sum(a * b for a, b in zip(self, other))

    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y,
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.x)

    def absolute(self):
        return sum(n * n for n in self) ** .5
