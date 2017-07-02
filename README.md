# ptt-cli
> a command line tool for ptt

## Requirement
- python3

## Usage
### login
```
python3 ptt.py login <account> <password>
```
### post
- content from file
    ```
    python3 ptt.py post <account> <password> -b <board> -a <article> -t <type> -f <file>
    ```
- content from stdin
    ```
    python3 ptt.py post <account> <password> -b <board> -a <article> -t <type> -c <content>
    ```

## Features
- [X] Login
- [X] Logout
- [X] Post
- [ ] Comment

## Version
v1.0

## License
MIT
