# Sequences

## Learning Goals

- Utilize Python's `list`, `tuple`, `range`, and `str` data types to accomplish
several common programming tasks.
- Execute and test Python code using the Python shell and `pytest`.

***

## Key Vocab

- **Sequence**: a data structure in which data is stored and accessed in a
specific order.
- **Index**: the location, represented by an integer, of an element in a
sequence.
- **Iterable**: able to be broken down into smaller parts of equal size that
can be processed in turn. You can loop through any iterable object.
- **Slice**: a group of neighboring elements in a sequence.
- **Mutable**: an object that can be changed.
- **Immutable**: an object that cannot be changed. (_Many immutable objects
appear mutable because programmers reuse their names for new objects_.)
- **List**: a mutable data type in Python that can store many types of data.
The most common data structure in Python.
- **Tuple**: an immutable data type in Python that can store many types of
data.
- **Range**: a data type in Python that stores integers in a fixed pattern.
- **String**: an immutable data type in Python that stores unicode characters
in a fixed pattern. Iterable and indexed, just like other sequences.

***

## Introduction

A _sequence_ is a simple data structure that is present in all programming
languages in which data is stored in a specified order. The elements of a
sequence can be accessed by their _index_. Just as in JavaScript, indices
of a sequence begin at 0 and increase by 1 with each step down the sequence:

```js
// JavaScript
const my_list = [1, 2, 3, 4]
console.log(my_list[0])
// 1
```

```py
# Python
my_list = [1, 2, 3, 4]
print(my_list[0])
# 1
```

`list` and `tuple` objects can store any type of data. `range` objects store
only integers, and `str` objects can only store unicode characters.

## When Are Sequences Used?

Whenever values are logically connected to one another and it is important to
keep them in order, you should store them in a sequence data structure.

```py
# A dynamic sequence of values that allows duplicates
fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]

# An immutable, ordered sequence of months
month_tuple = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
)

# A simple pattern of numbers
even_numbers_up_to_100 = range(0, 101, 2)

# A grammatical sentence
sentence_string = "Strings are immutable sequences of Unicode code points."
```

After being defined, sequences can be used as more complex data structures such as
_queues_ and _stacks_. We will discuss these more later on in this module.

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>Which sequence type is surrounded by parentheses?</p>
    <div id="dialog_for_link1" class="enhanceable_content dialog" title="Answer">
        <p>Tuples!</p>
    </div>
    <p class="visible-desktop"><a id="link1" class="Button"
    href="#dialog_for_link1">Check Your Answer</a></p>
</div>

***

## [Common Sequence Operations][common sequence operations]

All sequence data types in Python support certain functions and operators and
possess certain methods. For a sequence `s`:

- `x in s` returns `True` if `x` is equal to at least one element of `s`.

- `s + s2` returns a single sequence of the elements of `s` followed by the
elements of `s2`.

- `s * n` returns a single sequence of `s` repeated `n` times.

- `s[i]`returns the `i`th element of `s` (starting at 0).
    > NOTE: Python also supports negative indices. `-1` represents the last
    element in a sequence.

- `s[i:j]` returns a _slice_ of `s` from index `i` up to (but not including!)
index `j`.

- `s[i:j:k]` returns a slice of `s` from `i` to `j` with steps of `k` in
between.

- `len(s)` returns the number of elements in `s`.

- `min(s)` and `max(s)` return the minimum and maximum values in `s`,
respectively.
    > NOTE: this requires the elements of `s` to be of
the same data type, either `str` or numerical.

- `s.index(x)` returns the index of the first `x` in `s`.

- `s.count(x)` returns the number of instances of `x` in `s`.

Open up the Python shell and test each of these operations for yourself:

```py
s = [4, 6, 3, 9, 3, 5, 1, 2]
1 in s
# True
s + s
# [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s * 2
# [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s[1]
# 6
s[-1]
# 2
s[2:5]
# [3, 9, 3]
s[2:5:2]
# [3, 3]
len(s)
# 8
min(s)
# 1
max(s)
# 9
s.index(3)
# 2
s.count(9)
# 1
```

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>How would you retrieve the last two elements of a sequence if you don't
    know the length?</p>
    <div id="dialog_for_link2" class="enhanceable_content dialog" title="Answer">
        <p>There are several strategies for accessing the ends of sequences:<p>
        <ul>Use the <code>len()</code> function to find the length of the
            sequence, then access the last two elements at
            <code>s[len(s) - 1], s[len(s) - 2].</code></ul>
        <ul>Use negative indexing to directly access the last two elements of
            the list: <code>s[-1], s[-2]</code>.</ul>
        <ul>Use negative indexing to slice the last two elements of the
            sequence: <code>s[-1:-3:-1]</code>.</ul>
    </div>
    <p class="visible-desktop"><a id="link2" class="Button"
    href="#dialog_for_link2">Check Your Answer</a></p>
</div>

***

## Lists

We've encountered lists in several of our lessons so far. As lists are mutable
and can store any types of data in the same list object, they have many use
cases and many operations, functions, and methods that allow us to manipulate
their contents.

### Sorting Lists

Python provides two straightforward solutions for sorting lists: the
`list.sort()` method and the `sorted()` function. Both of these solutions
require that all elements of the list be of the same data type.

`list.sort()` rearranges the elements of a list so that they are in order
alphanumerically.

```py
my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)
# [1, 2, 3, 4, 5, 6]
```

`list.reverse()` rearranges the elements of a list so that they are in
descending order alphanumerically- just the opposite of `list.sort()`.

`sorted()` returns an alphanumerically sorted copy of the original list. This
function should be used when you want to preserve the integrity of your
original list, but you need a sorted version for a separate task.

```py
my_list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list)
print(my_list)
# [3, 6, 4, 2, 1, 5]
print(sorted_list)
# [1, 2, 3, 4, 5, 6]
```

### Adding to Lists

Python allows us to modify any of the elements of a list using their index:

```py
my_list = [0, 1, 2, 3]
my_list[0] = None
print(my_list)
# [None, 1, 2, 3]
```

If we want to extend a list, we unfortunately cannot use the same approach:

```py
my_list = [0, 1, 2, 3]
my_list[4] = 4
# IndexError: list assignment index out of range
```

Python does provide us with two options to extend lists: `list.append()` and
`list.insert()`.

`list.append()` does exactly what you might expect: it _appends_ its parameter
to the list.

```py
my_list = [0, 1, 2, 3]
my_list.append(4)
print(my_list)
# [0, 1, 2, 3, 4]
```

`list.insert()` provides us a few extra options for extending our list. Where
`list.append()` can only add to the end of a list, `list.insert()` can insert
at any index.

`list.insert()` takes two arguments: an index and a value. If a value already
exists at the index, the new value is inserted before it and everything after
is moved up by 1. If no value exists at the index, the new value is added to
the end of the existing list.

```py
my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, 'e')
print(my_list)
# ['a', 'b', 'c', 'd', 'e', 'f']
my_list.insert(1000, 'g')
print(my_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>Which method allows you to insert characters into the middle of a string?</p>
    <div id="dialog_for_link3" class="enhanceable_content dialog" title="Answer">
        <p>list.insert()</p>
    </div>
    <p class="visible-desktop"><a id="link3" class="Button"
    href="#dialog_for_link3">Check Your Answer</a></p>
</div>

### Removing from Lists

Python provides us with four (4!!!) options for removing elements from a list.

- The `del()` function.
- The `list.pop()` method.
- The `list.remove()` method.
- The `list.clear()` method.

`del()` removes elements from a list, specified by an index or range of
indices.

```py
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print(my_list)
# ['b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0:3])
print(my_list)
# ['e', 'f', 'g']
```

`list.pop()` removes and returns the element at the index passed in as an
argument. When used without any arguments, it removes and returns the last
element of the list.

`list.remove()` removes the element passed in as an argument. This is one of
the few `list` methods that searches by value instead of index!

`list.clear()` erases all of the values of a list. This is usually not a very
useful tool, but it's a fast way to free up memory on your device if you're
working with a particularly large list in the Python shell.

```py
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.pop()
# 'g'
my_list.pop(0)
# 'a'
my_list.remove('f')
print(my_list)
# ['b', 'c', 'd', 'e']
my_list.clear()
print(my_list)
# []
```

***

## Tuples

Tuples do not have any special exclusive methods like lists do. This is because
tuples are _immutable_. The sequence that they are provided when they are
created is maintained as long as the tuple object exists.

***

## Ranges

Ranges are a very simple type of sequence that is most commonly used in `for`
loops. Ranges can only contain integers in a fixed pattern. You can build a range
using the `range()` constructor method and loop through it as if it were a
standard list.

The range constructor only requires one argument: the end of the range. You may
have noticed above that this top value is **not** included in the range itself.
This is similar to how slicing works in lists.

```py
for n in range(4):
    print(n)

# 0
# 1
# 2
# 3
```

There are two optional arguments that you can include when creating a range:
a start value and a step size.

- `range(4)` gives us `0, 1, 2, 3`
- `range(1, 4)` gives us `1, 2, 3`
- `range(0, 4, 2)` gives us `0, 2`

While ranges are very similar to lists, a range is a different data type
and they exhibit some unique behaviors.

For instance, when we `print()` a list, we can see its contents:

```py
my_list = [0, 1, 2, 3]
print(my_list)
# [0, 1, 2, 3]
```

When we print a range containing the same elements, here's what we see:

```py
my_range = range(4)
print(my_range)
# range(0, 4)
```

<div style="border: 3px solid #00EEE0; margin: 15px; padding: 15px; width: 65%;">
    <p style="color: #00EEE0; font-size: 1.5em;"><strong>Check for Understanding</strong></p>
    <p>What would <code>range(2, 10, 2) produce?</code></p>
    <div id="dialog_for_link4" class="enhanceable_content dialog" title="Answer">
        <p><code>range(2, 10, 2)</code></p>
        <p><code>range()</code> statements produce <code>range</code> objects.</p>
        <p>To view the contents, of a <code>range</code> object, you must
            loop through and print each element <em>or</em> cast the range
            object to a <code>list</code> or <code>tuple</code> using their class
            constructors.</p>
        <p>The contents of this <code>range</code> would be:
            <code>[2, 4, 6, 8]</code></p>
    </div>
    <p class="visible-desktop"><a id="link4" class="Button"
    href="#dialog_for_link4">Check Your Answer</a></p>
</div>

***

## Strings

Python strings have _many_ methods that allow you to access and manipulate
their individual elements. It's very important to remember while working with
strings that they are iterable objects (they can be looped through!) and
they are indexed.

```py
my_string = 'Hello world!'
for char in my_string:
    print(char)

# H
# e
# l
# l
# o
# 
# w
# o
# r
# l
# d
# !

my_string[0]
# 'H'
```

### Changing Case

Strings can be formatted for case using three methods:

- `str.upper()` returns an uppercase version of the original string.
- `str.lower()` returns a lowercase version of the original string.
- `str.title()` returns the original string in titlecase (with the first letter
of each new word capitalized.)

### [Other String Methods][string methods]

There are many other string methods that will allow you to accomplish most
simple reformatting and conversion operations that you'll want to do. There
are so many, in fact, that we're providing a
[link to a comprehensive list][string methods] instead of going in-depth on
each one.

The important thing to remember when working with strings is that they are
**immutable**. All string methods return a new object; they do not replace
the original.

```py
my_string = 'hello world!'
my_string.upper()
# HELLO WORLD!
print(my_string)
# hello world!
```

***

## Instructions

Time to get some practice! Write your code in the `sequences.py` file in the
`lib` folder. Run `pytest -x` to check your work. Your goal is to practice
manipulating sequences with the Python tools you've learned about in this
lesson and the lessons before.

Write a function `print_fibonacci()` that prints each element of the
[fibonacci sequence][fibonacci sequence] up to the length provided in the
function's parameters.

```py
print_fibonacci(9)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
```

When all of your tests are passing, submit your work using `git`.

***

## Resources

- [Common Sequence Operations][common sequence operations]
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Range Docs](https://docs.python.org/3/library/stdtypes.html#ranges)
- [String Methods][string methods]

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[string methods]: https://www.w3schools.com/python/python_ref_string.asp
[fibonacci sequence]: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
