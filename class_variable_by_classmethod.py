class Pizza():
     radius = 42
     @classmethod
     def get_radius(cls):
         return cls.radius

print Pizza.get_radius()