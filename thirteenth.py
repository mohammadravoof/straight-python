# more on modules
# There is a variant of the import statement that imports names from a module directly into the importing module’s namespace
from fibo import fib
fib(500)

# Importing all the methods from the fibo and using it directly
from fibo import *
fib(500)

# Importing the module and naming it something else or shorter
import fibo as fib # module
fib.fib(500)

# Importing the module and then finding a method and naming it something more conventional
from fibo import fib as fibonacci # method
fibonacci(500)