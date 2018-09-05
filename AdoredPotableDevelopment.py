registry = {}
class MetaClass(type):  
  def register_class(target_class):    
    registry[target_class.__name__] = target_class
  def __new__(cls, clsname, bases, attrs):      
      newclass = super(MetaClass, cls).__new__(cls, clsname, bases, attrs)
      cls.register_class(newclass)
      return newclass

class MyClass(metaclass=MetaClass):
  pass
class MyOtherClass(metaclass=MetaClass):
  pass
x=MyClass()
y=MyOtherClass()

print("REGISTRY",registry)
