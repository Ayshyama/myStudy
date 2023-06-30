#### Feat 1. What is a class method called?

Select one option from the list

- There is no such term in OOP
- Variables and functions inside a class
- Any (non-static) function declared inside a class
- Any variable declared within a class

#### Feat 2. What are called class attributes?

Select one option from the list

- Only class variables
- Only class methods
- Instances (objects) of a class
- Variables and method names (references to methods) of a class

#### Feat 3. What role does the self parameter play in class methods?

Select one option from the list

- this is a reference to the current class method
- this is a reference to the class that the method belongs to
- it's just a required (reserved) parameter for class methods through which arbitrary data can be passed
- is a reference to the class object from which the method was called

#### Feat 4. Declare a class named MediaPlayer with two methods:

- open(file) - to open a media file named file (creates a local property filename with the value of the file argument in
  the object of the MediaPlayer class)
- play() - to play a media file (displays the string "Playing <media file name>")

Create two instances of this class named media1 and media2. Call the open() method from them with the argument "
filemedia1" for media1 and "filemedia2" for media2.
Then call the play() method through the objects. At the same time, two lines should be displayed on the screen (without
quotes):

- "Playback filemedia1"
- "Playback filemedia2"

#### Feat 5. Declare a class named Graph and methods:

- set_data(data) - transferring the data set for subsequent display (data - list of numeric data);
- draw() - display the data (in the same order as in the data list)

and attribute:

- LIMIT_Y = [0, 10]

The set_data() method must form the local data property of the Graph class object.
The data attribute must refer to the list passed to the method.
The draw() method must display the list as a string of space-separated numbers that belong to the specified range of the
LIMIT_Y attribute (bounds included).

Create a graph_1 object of the Graph class, call the set_data() method on it, and pass in the list:

- [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

Then, call the draw() method through the graph_1 object.
A line should appear on the screen with the corresponding set of numbers written with a space.
For example (output without quotes):

- "10 0 2 5 7"

#### Feat 6. There is the following class:

```py
class Exercises:
    def next_task(self):
        return "Next task"
```

And an object of this class is created:

- my_st = stepik()

Select all correct options for calling the next_task() method
Select all correct options from the list:

- Stepik.my_st.next_task()
- next_task(my_st)
- Stepik.next_task(my_st)
- my_st.next_task(Stepik)
- next_task(Stepik)
- my_st.next_task()

#### Feat 7. There is the following class for reading information from the input stream:

```py
import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # read a list of strings from the input stream
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
```

Which, then, can be used as follows:

```
sr = StreamReader()
data, result = sr.readlines()
```

It is necessary to declare another StreamData class with the method before the StreamReader class:

```py
def create(self, fields, lst_values): ...
```

which would receive the FIELDS tuple from the names of local attributes (passed to the fields attribute) and the list of
lst_in strings (passed to the lst_values attribute) as input and would form local properties in the StreamData class
object with field names from fields and corresponding values from lst_values.
If the creation of local properties succeeds, then the create() method returns True, otherwise False. If the number of
fields and the number of rows do not match, then the create() method returns False and no local attributes need be
created.

P.S. In the program, only the StreamData class needs to be additionally declared. Nothing more needs to be done.

Sample Input:

10
Python - the basics of craftsmanship
512