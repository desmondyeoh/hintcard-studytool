# hintcard-studytool
Instead of trying to remember entire answer of the flash card, this app asks you to remember a small portion of answer at first, by hiding `MISSING_RATE` (0-1) parts of texts in the answer. You can control the `MISSING_RATE` value by gradually increasing it to `1` (hide the entire answer).

![Demo Image](demo.png)

## How to Use
1. Set variable `data` to hold your Question-Answer pairs. Every Question-Answer pair is separated by `===`, and within the pair, the question and the answer are separated by `---`.
2. Set the `MISSING_RATE` with any value ranging from `0` to `1` (`0` means show everything, `1` means hide everything).
3. Run the file `python3 main.py`
