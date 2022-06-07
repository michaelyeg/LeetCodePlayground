from icecream import ic

"""
CodeSignal assessment from DropBox interview.
Scenario
Your task is to implement a simplified version of text editor.

All operations that should be supported are listed below. Partial credit will be given for each implemented operation. Please submit often to ensure partial credits are captured.

Implementation tips

Implement operations and provided steps one by one, and not all together, keeping in mind that you will need to make refactors to support each additional step. In the first three levels you can assume that only one text document is modified.

Note

After every operation, add the current state of the text to the resulting array. The returning array should consist of all the states after each operation is applied and have the same length as the # of input queries.

Level 1
The editor starts with a blank text document, with the cursor at initial position 0.

1. APPEND <text> should append the inputted string text to the document starting from the current position of the cursor. After the operation, the cursor should be at the end of the added string.

queries = [
    ["APPEND", "Hey"],                | "" -> "Hey"
    ["APPEND", " there"],             | "Hey" -> "Hey there"
    ["APPEND", "!"]                   | "Hey there" -> "Hey there!"
]

// returns: [ "Hey",
//            "Hey there",
//            "Hey there!" ]
2. MOVE <position> should move the cursor to the specified position. The cursor should be positioned between document characters, and are enumerated sequentially starting from 0. If the specified position is out of bounds, then move the cursor to the nearest available position.

queries = [
    ["APPEND", "Hey you"],            | "" -> "Hey you"
    ["MOVE", "3"],                    | moves the cursor after the first "y"
    ["APPEND", ","]                   | "Hey you" -> "Hey, you"
]

// returns: [ "Hey you",
//            "Hey you",
//            "Hey, you" ]
3. FORWARD_DELETE should remove the character right after the cursor, if any.

queries = [
    ["APPEND", "Hello! world!"],      | "" -> "Hello! world!"
    ["MOVE", "5"],                    | moves the cursor before the first "!"
    ["FORWARD_DELETE"],               | "Hello! world!" -> "Hello world!"
    ["APPEND", ","]                   | "Hello world!" -> "Hello, world!"
]

// returns: [ "Hello! world!",
//            "Hello! world!",
//            "Hello world!",
//            "Hello, world!" ]
and

queries = [
    ["APPEND", "!"],                  | "" -> "!"
    ["FORWARD_DELETE"],               | "!" -> "!"
    ["MOVE", "0"],                    | moves the cursor before the first symbol
    ["FORWARD_DELETE"],               | "!" -> ""
    ["FORWARD_DELETE"]                | "" -> ""
]

// returns: [ "!",
//            "",
//            "",
//            "",
//            "" ]
Level 2
Introduce methods to copy a part of the document text.

4. SELECT <left> <right> should select the text between the left and right cursor positions. Selection borders should be returned to the bounds of the document. If the selection is empty, it becomes a cursor position. Any modification operation replace the selected text and places the cursor at the end of the modified segment.

Additionally,

SELECT and APPEND should replace the selected characters with the appended characters
SELECT and FORWARD_DELETE should delete the selected characters
SELECT and MOVE deselects characters if there were any and moves the cursor
For example, the following operations

queries = [
    ["APPEND", "Hello cruel world!"], | "" -> "Hello cruel world!"
    ["SELECT", "5", "11"],            | selects " cruel"
    ["APPEND", ","],                  | "Hello cruel world!" -> "Hello, world!",
                                      | as " cruel" has been replaced with "," by APPEND
    ["SELECT", "5", "12"],            | selects ", world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello!",
                                      | as ", world" has been deleted by FORWARD_DELETE
    ["SELECT", "4", "6"],             | selects "o!"
    ["MOVE", "1"]                     | moves cursor before "e", deselects "o!"
]

// returns: [ "Hello cruel world!",
//            "Hello cruel world!",
//            "Hello, world!",
//            "Hello, world!",
//            "Hello!",
//            "Hello!",
//            "Hello!" ]
produce "Hello!" with the cursor positioned after letter H.

5. CUT should remove the selected text and save it to the clipboard, if there is an active non-empty selection.
6. PASTE should append the text from the clipboard. If clipboard is empty, does nothing. The current selected text (if any) is overwriten with the clipboard value after the operation, and the cursor is placed at the end of the pasted text.

For example, the following operations

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "5", "12"],            | selects ", world"
    ["CUT"],                          | "Hello, world!" -> "Hello!",
                                      | as ", world" has been deleted by CUT and saved to clipboard
    ["MOVE", "4"],                    | moves the cursor between "l" and "o": "Hell|o!"
    ["PASTE"],                        | "Hello!" -> "Hell, worldo!",
                                      | as ", world" has been pasted from the clipboard
    ["PASTE"],                        | "Hell, worldo!" -> "Hell, world, worldo!"
                                      | as ", world" has been pasted from the clipboard
    ["SELECT", "4", "19"],            | selects ", world, worldo"
    ["PASTE"]                         | "Hell, world, worldo!" -> "Hell, world!",
                                      | as selected ", world, worldo" has been replaced
                                      | with ", world" from the clipboard
]

// returns: [ "Hello, world!",
//            "Hello, world!",
//            "Hello!",
//            "Hello!",
//            "Hell, worldo!",
//            "Hell, world, worldo!"
//            "Hell, world, worldo!" 
//            "Hell, world!" ]
Level 3
The text editor should allow document changes to be tracked and reverted. Consider only operations that actually modify the contents of the text document.

7. UNDO should restore the document to the state before the previous modification or REDO operation. The selection and cursor position should be also restored to the state they were before.

For example,

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello, !",
                                      | as "world" has been deleted by FORWARD_DELETE
    ["UNDO"],                         | restores "Hello, world!" with "world" selected
    ["APPEND", "you"]                 | "Hello, world!" -> "Hello, you!",
                                      | as "world" has been replaced with "you"
]

// returns: [ "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "Hello, world!",
              "Hello, you!" ]
8. REDO can only be performed if the document has not been modified since the last UNDO operation. REDO should restore the state before the previous UNDO operation, including the selection and cursor position. Multiple UNDO and REDO operations can be performed in a row.

For example,

queries = [
    ["APPEND", "Hello, world!"],      | "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["FORWARD_DELETE"],               | "Hello, world!" -> "Hello, !",
                                      | as "world" has been deleted by FORWARD_DELETE
    ["MOVE", "6"],                    | moves the cursor after the comma 
    ["UNDO"],                         | restores "Hello, world!" with "world" selected
    ["UNDO"],                         | restores initial ""
    ["REDO"],                         | restores "Hello, world!" with "world" selected
    ["REDO"]                          | restores "Hello, !" with the cursor after the comma
]

// returns: [ "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "Hello, !",
              "Hello, world!",
              "",
              "Hello, world!",
              "Hello, !" ]
Level 4
The text editor should support multiple text documents with a common clipboard.

9. CREATE <name> should create a blank text document name. If such a file already exists, ignore the operation and return empty string. Modification history is stored individually for each document.
10. SWITCH <name> should switch the current document to name. If there is no such file, ignore the operation and return empty string. When switching to a file, the position of the cursor and selection should return to the state in which they were left.

Note: it is guaranteed that all operations from previous levels will be executed on the active document. For backward compatibility, assume for Levels 1-3 there is a single, initially active document.

For example,

queries = [
    ["CREATE", "document1"],          | creates document1
    ["CREATE", "document2"],          | creates document2
    ["CREATE", "document1"],          | raises a runtime exception
    ["SWITCH", "document1"],          | switches to document1
    ["APPEND", "Hello, world!"],      | document1: "" -> "Hello, world!"
    ["SELECT", "7", "12"],            | selects "world"
    ["CUT"],                          | cuts "world" to the clipboard
    ["SWITCH", "document2"],          | switches to document2
    ["PASTE"],                        | document2: "" -> "world"
    ["SWITCH", "document1"],          | switches to document1
    ["FORWARD_DELETE"]                | document1: "Hello, !" -> "Hello,!"
]

// returns: [ "",
              "",
              "",
              "",
              "Hello, world!",
              "Hello, world!",
              "Hello, !",
              "",
              "world",
              "Hello, !",
              "Hello,!" ]
Example

For

queries = [
    ["APPEND", "Hey"],
    ["APPEND", " you"],
    ["APPEND", ", don't"],
    ["APPEND", " "],
    ["APPEND", "let me down"]
]
the output should be

solution(queries) = [
    "Hey",
    "Hey you",
    "Hey you, don't",
    "Hey you, don't ",
    "Hey you, don't let me down"
]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string queries

An array of operations need to be applied to the text editor. It is guaranteed that each operation is one of the operations described in the description, all operation parameters are given in correct format, and the text editor will never be in an incorrect state that is not described in the description.

Guaranteed constraints:
1 ≤ queries.length ≤ 250.

[output] array.string

After every operation, add the current state of the text to the resulting array. The returning array should consist of all the states after each operation is applied and have the same length as the # of input queries.
"""


# REDO can only be performed if the document has not been modified since the last UNDO operation.
def can_perform_redo(queries, q, temp_text, result):
    q -= 1
    while q >= 0:
        if queries[q] == 'UNDO':
            break
        q -= 1
    if q == 0:
        return False
    return temp_text == result[q]


def solution(queries):
    result = []
    select_text = ''
    paste_text = ''
    # Used to track for undo & redo
    revert_pos = None
    # Use dictionary to store doc_name => document
    documents = {'default': Document()}
    # index for current document
    doc_current = 'default'
    for q in range(len(queries)):
        op = queries[q][0]
        cursor = documents[doc_current].cursor
        match op:
            case 'APPEND':
                if select_text == '':
                    documents[doc_current].text = documents[doc_current].text[0: cursor:] \
                                                  + queries[q][1] + documents[doc_current].text[cursor::]
                else:
                    documents[doc_current].text = documents[doc_current].text.replace(select_text, queries[q][1])
                # temp_text = doc_current
                documents[doc_current].cursor += len(queries[q][1])
            case 'MOVE':
                documents[doc_current].cursor = moveCursor(cursor, queries[q][1], documents[doc_current].text)
            case 'FORWARD_DELETE':
                if select_text == '' and cursor < len(documents[doc_current].text):
                    documents[doc_current].text = documents[doc_current].text[0: cursor:] + documents[doc_current].text[
                                                                                            cursor + 1::]
                else:
                    documents[doc_current].text = documents[doc_current].text.replace(select_text, '')
                    documents[doc_current].cursor += len(select_text)
            case 'SELECT':
                if int(queries[q][1]) < 0:
                    left = 0
                else:
                    left = int(queries[q][1])
                if int(queries[q][2]) >= len(documents[doc_current].text):
                    right = len(documents[doc_current].text) - 1
                else:
                    right = int(queries[q][2])
                select_text = documents[doc_current].text[left: right:]
                # If the selection is empty, it becomes a cursor position.
                if select_text == '':
                    documents[doc_current].cursor = left
            case 'CUT':
                if select_text != '':
                    documents[doc_current].cursor = documents[doc_current].text.find(select_text) - 1
                    documents[doc_current].text = documents[doc_current].text.replace(select_text, '')
                    paste_text = str(select_text)
                    select_text = ''
            case 'PASTE':
                if select_text != '' and paste_text != '':
                    # Search for select_text and replace it with paste_text
                    documents[doc_current].text = documents[doc_current].text.replace(select_text, paste_text)
                    documents[doc_current].cursor += len(paste_text)
                else:
                    documents[doc_current].text = documents[doc_current].text[0: cursor:] + paste_text + \
                                                  documents[doc_current].text[cursor::]
                    documents[doc_current].cursor += len(select_text)
            case 'UNDO':
                # Look for next previous result which is different from result[-1]
                if revert_pos is not None:
                    revert_pos -= 1
                else:
                    revert_pos = q - 2
                while result[revert_pos] == result[q - 1] and revert_pos > 1:
                    revert_pos -= 1
                if revert_pos == 0 and result[revert_pos] == result[q - 1]:
                    documents[doc_current].text = ""
                else:
                    documents[doc_current].text = result[revert_pos]
            case 'REDO':
                if can_perform_redo(queries, q, documents[doc_current].text, result):
                    revert_pos += 1
                    documents[doc_current].text = result[revert_pos]
            case 'CREATE':
                doc_name = queries[q][1]
                if doc_name not in documents.keys():
                    documents[queries[q][1]] = Document()
            case 'SWITCH':
                doc_current = queries[q][1]
        result.append(documents[doc_current].text)
        q += 1
    # ic(result)
    return result


def moveCursor(index, move, text):
    move = int(move)
    if move < len(text) and move > 0:
        return move
    elif move <= 0:
        return 0
    elif index < len(text) <= move and move > 0:
        return len(text)
    else:
        return index


class Document:
    cursor = 0
    text = ''


# Test cases
# Level 1
assert solution([["APPEND", "Hey"], ["APPEND", " there"], ["APPEND", "!"]]) == ["Hey", "Hey there", "Hey there!"]

assert solution([["APPEND", "Hey you"], ["MOVE", "3"], ["APPEND", ","]]) == ["Hey you", "Hey you", "Hey, you"]

assert solution([["APPEND", "Hello! world!"], ["MOVE", "5"], ["FORWARD_DELETE"], ["APPEND", ","]]) == [
    "Hello! world!", "Hello! world!", "Hello world!", "Hello, world!"]
# Level 2
assert solution([["APPEND", "Hello cruel world!"], ["SELECT", "5", "11"], ["APPEND", ","], ["SELECT", "5", "12"],
                 ["FORWARD_DELETE"], ["SELECT", "4", "6"], ["MOVE", "1"]]) == [
           "Hello cruel world!", "Hello cruel world!", "Hello, world!", "Hello, world!", "Hello!", "Hello!", "Hello!"
       ]

assert solution([["APPEND", "Hello, world!"], ["SELECT", "5", "12"], ["CUT"], ["MOVE", "4"], ["PASTE"], ["PASTE"],
                 ["SELECT", "4", "19"], ["PASTE"]]) == [
           "Hello, world!", "Hello, world!", "Hello!", "Hello!", "Hell, worldo!", "Hell, world, worldo!",
           "Hell, world, worldo!", "Hell, world!"
       ]
# Level 3
assert solution(
    [["APPEND", "Hello, world!"], ["SELECT", "7", "12"], ["FORWARD_DELETE"], ["UNDO"], ["APPEND", "you"]]) == [
           "Hello, world!", "Hello, world!", "Hello, !", "Hello, world!", "Hello, you!"
       ]
assert solution(
    [["APPEND", "Hello, world!"], ["SELECT", "7", "12"], ["FORWARD_DELETE"], ["MOVE", "6"], ["UNDO"], ["UNDO"],
     ["REDO"], ["REDO"]]) == [
           "Hello, world!", "Hello, world!", "Hello, !", "Hello, !", "Hello, world!", "", "Hello, world!", "Hello, !"
       ]
# Level 4
assert solution(
    [["CREATE", "document1"], ["CREATE", "document2"], ["CREATE", "document1"], ["SWITCH", "document1"],
     ["APPEND", "Hello, world!"], ["SELECT", "7", "12"], ["CUT"], ["SWITCH", "document2"],
     ["PASTE"], ["SWITCH", "document1"], ["FORWARD_DELETE"]]) == [
           "", "", "", "", "Hello, world!", "Hello, world!", "Hello, !", "", "world", "Hello, !", "Hello,!"]
