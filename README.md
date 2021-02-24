# XML parser

### Info

```
Used to parse XML files and output them into JSON format.
```

### Prerequisites

Make sure you have installed all the following prerequisites on your pc:

* You should have [Python 3.x](https://www.python.org/downloads/) on your system.

### Usage

* Run `main.py` followed with filenames, without the file extension `.xml`, as system arguments. Then wait for the
  result. Here is an example of a command:

  ```
    $ python main.py seatmap1 seatmap2
  ```

### Output

* You will have an output file for each input file named `{INPUT_FILE_NAME}_parsedAll.json`.
* For the files `seatmap1` and `seatmap2`, you will have a result of `seatmap{1/2}_parsed.json`.
* You can pass `seatmap1` and `seatmap2` in any order.