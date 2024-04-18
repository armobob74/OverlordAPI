# Overlord API

This is a simple Flask API designed to run overlord sequences.

## Passing Variables

This API takes variables in the standard PMAN format. That is, POST requests with the following body:

```json
{
  "args": [1,0,2],
  "kwargs": {
    "name": "apple",
    "quantity": 3
  }
}
```

The `args` field is a list of arguments. It's used for easy compatibility with CSV files.
The `kwargs` field holds an Object, allowing key/value pairs.

## How variables are passed
Overlord itself doesn't let us pass variables to our sequences, so we have to be a bit clever with it. 
We write our variables to a file, then tell the sequence to read from that file. In this way, we can effectively pass as many arguments as we want.

Unfortunately, Overlord's built-in C# doesn't let us parse `JSON` files, so we have to do the parsing using basic string manipulation. To make this easy, we use a simple format called `PVAR` (**P**ersist **VAR**iables). The format is shown below:

```
name=apple
quantity=3
```

Notice that there are no spaces, quote marks, or anything. This is because the C# script reads it line-by-line and decides what the Type of the value is based on the Key. For parsing utils, check out `pvar.py`
