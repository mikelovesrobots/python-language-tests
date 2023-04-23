import pytest

def test_abs_absolute_numbers():
    assert abs(-10) == 10
    assert abs(-10.5) == 10.5

def test_any_is_true_if_any_elements_are_true():
    # Note, this is not strict True, it's truthiness
    assert any([-1,0,1]) == True
    assert any([]) == False
    assert any([True, False]) == True
    assert any([False]) == False
    assert any([0]) == False

def test_bool():
    # returns the truthiness value for an argument
    assert bool({1}) == True
    assert bool([]) == False

def test_bytearray():
    # returns a mutable bytearray for an object
    # see bytes for the immutable version
    # would this be useful for changing encodings?
    assert bytearray("python", "utf-8") == b"python"

def test_callable():
    # returns true if the object appears callable
    class A:
        def b():
            pass
    
    assert callable(A)
    assert callable(A().b)
    assert not callable(A())
    assert callable(lambda x: x + 1)
    assert not callable(None)
    assert not callable(4)

def test_bytes():
    # returns an immutable bytearray
    # for the mutable version see bytearray()
    assert bytes("python", 'utf-8') == b"python"

def test_chr():
    # returns the unicode value of the character
    assert chr(1200) == "Ұ"
    assert chr(49) == "1"

def test_compile():
    # precompiles some string code, returning syntax errors if something is wrong
    # this is pretty complicated it takes all sorts of flags and various levels of sandboxiness, like you can provide a list of globals and locals available to it
    # or set it in exec, single or eval mode.
    assert eval(compile("True", "somefilename", "eval")) == True
    x = 50
    assert eval(compile("x == 50", "somefilename", "eval")) == True

def test_classmethod():
    # returns a class method from a regular method
    # I suppose it's useful for uh... completeness? Creating crazy-ass factories?
    # metaprogramming that nobody understands?
    class A:
        def b(self):
            return True

    A.c = classmethod(A.b)
    assert A.c() == True 

def test_complex():
    # constructs a complex number when real and imaginary parts are provided
    # never in my life have I ever needed to use a complex number, but I guess it's nice it's there?
    assert complex(2, -3) == 2-3j

def test_delattr():
    # like javascript's delete, you can delete an attribute from an object that supports it
    class A:
        a = 1    
    assert A().a == 1

    # Note it deletes it from objects that already created as well
    x = A()
    delattr(A, "a")
    with pytest.raises(AttributeError):
      x.a
    with pytest.raises(AttributeError):
      A().a

def test_dict():
    # creates a dictionary with a keyword, useful for programmatic creation I suppose
    assert dict() == {}
    assert dict(x=1) == {"x": 1}
    assert dict([("x", 1), ("y", 2)]) == {"x": 1, "y": 2}

    x = {"x": 1}
    assert dict(**x) == {"x": 1}

    assert dict({"x": 1}, y=2) == {"x": 1, "y": 2}

def test_dir():
    # dir recturns the list of attributes on the object
    assert "__eq__" in dir(1)

def test_divmod():
    # divmod returns quotient and remainder in a tuple
    assert divmod(8, 3) == (2, 2)
    assert divmod(8,3)[0] == 2
    assert divmod(8,3)[1] == 2

def test_enumerate():
    # enumerate adds a counter to an iterable and returns the enumerate object
    assert list(enumerate(["a","b"])) == [(0, "a"), (1, "b")]
    assert list(enumerate(["a","b"], start=1)) == [(1, "a"), (2, "b")] 

def test_staticmethod():
    # like classmethod, but staticmethod knows nothing about itself, it's not passed self
    class A:
        def sum(a, b):
            return a + b
    
    A.sum == staticmethod(A.sum)
    assert A.sum(1, 2) == 3

def test_filter():
    # behaves like a ruby select or filter
    assert list(filter(lambda x: x == 1, [1,2,3])) == [1]
    
    def condition_test(x):
        return x == 1
      
    assert list(filter(condition_test, [1,2,3])) == [1]

    # This is weird. WTF is this. You can use None as an iterator
    # to filter for truthy values
    assert list(filter(None, [False, None, 1, 2])) == [1,2]

def test_eval():
    # evals raw strings
    assert eval("True") == True

    # can eval precompiled strings
    assert eval(compile("True", filename="no filename", mode="eval")) == True

    # you can pass it faux globals and locals to limit its access
    globals = {"x": 10}
    locals = None
    assert eval("x", globals, locals) == 10

    # note that you can't execute anything with eval, see exec if you want more functionality
    with pytest.raises(SyntaxError):
      eval('for i in range(1, 11): print(i)')

def test_float():
    assert float() == 0.0

    # converts numbers to floats
    assert float(1) == 1.0
    assert float(int(4)) == 4.0

    # converts strings to floats
    assert float("1") == 1.0
    assert float("1.340") == 1.34

def test_format():
    # format() can do a lot of stuff, see format_strings_test
    assert '{:>6}'.format(1.23) == '  1.23'

def test_frozenset():
    # returns an immutable set that throws an error if you try to add to it
    assert list(frozenset(('a'))) == ['a']

    set('a').add('b')
    with pytest.raises(AttributeError):
      frozenset('a').add('b')

def test_getattr():
    # returns the named attribute of the object
    class A:
        x = 1    
    assert getattr(A(), 'x') == 1

def test_globals():
    # returns all the globals available right now
    assert '__name__' in globals()
    assert globals()['__name__'] == 'built_in_functions_test'

def test_exec():
    # see eval and compile
    # The eval() function can only execute Python expressions, while the exec() function can execute any valid Python code.
    a = 10
    exec("a = 1")
    assert a == 10

def test_hasattr():
    # returns true if the object has the attribute
    class A:
        def b():
            pass
        
    assert hasattr(A(), 'b') == True
    assert hasattr(A(), 'c') == False

def test_help(capsys):
    # returns the built-in help system for the object
    help(1)
    assert capsys.readouterr().out.startswith('Help on int object:')

def test_hex():
    # converts a number to its corresponding hexadecimal string
    assert hex(255) == "0xff"

def test_hash():
    # returns the hash value of an object. It's used to look up dictionary keys quickly.
    # It's not stable though between runs of a script, so that's kind of hard to test
    assert hash("asdfasd") == hash("asdfasd") 

def test_input():
    # input takes input from the user with an optional prompt and returns it
    # I'm not going to get into the trouble of injecting stdin code and returning it. it's fine.
    # it's basically gets() from other languages
    pass

def test_id():
    # id returns the built-in id for a given object.
    # like hash, it's hard to test as between runs the id changes
    # kind of a bummer as in ruby for a long time, id of nil was 0. it was the first object defined
    # and there was kind of something romantic about that.
    assert id(None) == id(None)

def test_isinstance():
    # returns true if the object is an instance or subclass of the provided class
    assert isinstance([], list) == True

    class A:
        pass
    
    class B(A):
        pass
    
    assert isinstance(A(), A) == True
    assert isinstance(A(), B) == False
    assert isinstance(B(), A) == True
    assert isinstance(A, object) == True
    assert isinstance(A(), object) == True
    
def test_int():
    # converts a number or string to its equivalent integer
    assert int(3.4) == 3
    assert int("3") == 3
    with pytest.raises(ValueError):
        # Note: you can't convert string floats to integers directly
        assert int("3.4") == 3
    assert int(float("3.4")) == 3

    # You can convert different bases to integers
    assert int("0xff", 16) == 255 

    # You can fulfil the int "interface" to override how int works on a custom class, could be useful for a linked list class or something
    class A:
        x = 10
        def __int__(self):
            return self.x
    
    assert int(A()) == 10

def test_issubclass():
    # returns true if the class is a subclass of the argument
    class A:
        pass
    
    class B(A):
        pass
    
    assert issubclass(A, object) == True
    assert issubclass(B, A) == True
    assert issubclass(A, B) == False

    # Note, a subclass is considered a subclass of itself cause...?
    assert issubclass(A, A) == True

def test_iter():
    # this is neat. it returns an iterator for the given argument
    iterable = iter([1,2,3])
    assert next(iterable) == 1
    assert next(iterable) == 2
    assert next(iterable) == 3
    with pytest.raises(StopIteration):
      assert next(iterable) == 4
    
    # you can provide a special "sentinel" value that's used to stop the sequence
    # but the iterable needs to be callable
    # there's a lot of value here for consuming something over and over, but stopping early when it returns like -1 or None
    x = [1,2,3]
    iterable = iter(lambda: x.pop(), 2)
    assert next(iterable) == 3
    with pytest.raises(StopIteration):
      next(iterable)

    # you can conform your custom object to the __iter__ and __next__ method interfaces to build a custom iterator
    class DoubleIt:
      start = 1

      def __iter__(self):
          return self

      def __next__(self):
          self.start *= 2
          if self.start > 8:
              raise StopIteration
          return self.start

      __call__ = __next__
    
    my_iter = iter(DoubleIt(), 16)
    assert next(my_iter) == 2
    assert next(my_iter) == 4
    assert next(my_iter) == 8
    with pytest.raises(StopIteration):
        next(my_iter)

def test_list():
    # constructs a list from an iterable
    assert list([1]) == [1]
    assert list(('a')) == ['a']
    assert list({'a': 1}) == ['a']

    # you can create a list from an iterable object  
    class DoubleIt:
      start = 1

      def __iter__(self):
          return self

      def __next__(self):
          self.start *= 2
          if self.start > 8:
              raise StopIteration
          return self.start

    assert list(DoubleIt()) == [2,4,8]

def test_locals():
    # returns a list of all the locals and symbols of the current execution point
    x = 1
    assert locals() == {"x": 1}

def test_len():
    # returns the number of items in an object
    assert len([]) == 0
    assert len([1]) == 1
    assert len("abc") == 3
    assert len(bytearray("abc", 'utf8')) == 3
    assert len({"x": 1}) == 1
    assert len(('a', 'b', 'c')) == 3
    assert len({1, 2, 3}) == 3

    # internally it calls .__len__() on the object
    class A:
        def __len__(self):
            return 10    
    assert len(A()) == 10

def test_max():
    # returns the largest item in an iterable
    with pytest.raises(ValueError):
      max([])
    
    assert max([0,1]) == 1
    assert max((0, 1)) == 1
    assert max({"x": 1, "y": 2}) == "y"

    # I have no idea what's happening here, but you can pass it multiple iterables
    assert max([0,1],[3,4],[5,6],[],[0,1]) == [5,6] 

    # This makes more sense
    assert max(0, 1, 2) == 2

    # largest key
    mydict = {1: 0, 2: 1}
    assert max(mydict) == 2

    # largest value
    assert max(mydict, key = lambda x: mydict[x]) == 2

def test_min():
    # returns the smallest item in an iterable
    with pytest.raises(ValueError):
      min([])
    
    assert min([0,1]) == 0
    assert min((0, 1)) == 0
    assert min({"x": 1, "y": 2}) == "x"

    # I have no idea what's happening here, but you can pass it multiple iterables
    assert min([0,1],[3,4],[5,6],[],[0,1]) == [] 

    # This makes more sense
    assert min(0, 1, 2) == 0

    # largest key
    mydict = {1: 0, 2: 1}
    assert min(mydict) == 1

    # largest value
    assert min(mydict, key = lambda x: mydict[x]) == 1

def test_map():
    # classic map
    x = [1,2,3]
    assert isinstance(map(lambda y: y * 2, x), map)
    assert list(map(lambda y: y * 2, x)) == [2,4,6]

def test_next():
    # see iter()
    pass

def test_memoryview():
    # Lets you both read from the internal memory array or buffer of an object
    # and write to it.  I'm not messing with this. this is really low-level.
    pass

def test_object():
    # returns a featureless object that's the base of all classes
    assert isinstance(object(), object)

def test_oct():
    # takes an integer and returns its octal representation
    assert oct(9) == '0o11'

def test_ord():
    # takes an integer and returns the unicode character, pretty much the opposite of chr
    assert chr(15000) == '㪘'

def test_open():
    # opens a file and returns the given file object
    f = open("tests/fixtures/test.txt", 'r')
    content = f.read()
    f.close()
    assert content == "abc\ndef\n"

    # with auto-closes. It's not clear how it detects that. is this just a special case in the python standard library?
    # note: see https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
    with open("tests/fixtures/test.txt", "r") as file1:
        assert file1.read() == "abc\ndef\n"

def test_pow():
    # computes the power of a number by raising the first argument to the second argument
    assert pow(2,4) == 16

    # you can oddly provide a modulus argument to the end, so this is equivalent to the following
    assert pow(2,4,3) == (pow(2,4) % 3) == 1

def test_print(capsys):
    # prints the string to stdout
    print("abc")
    assert capsys.readouterr().out == "abc\n"

    print([1,2,3])
    assert capsys.readouterr().out == "[1, 2, 3]\n"

    # like console.log in javascript you can pass it multiple arguments
    print(1, 2)
    assert capsys.readouterr().out == "1 2\n"

    print(1, 2, sep = '')
    assert capsys.readouterr().out == "12\n"

    # you can override the endline
    print("abc", end="")
    assert capsys.readouterr().out == "abc"

