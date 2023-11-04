# CLI-Sage
Introducing "CLI-Sage" - a command line productivity tool that seamlessly integrates a powerful large language model with your command line interface. Responding to your prompts with programs, shell commands and chats directly from your terminal. Boost your efficiency and creativity by harnessing the combined power of a AI language model and your CLI, making it easier than ever to streamline your workflow and tackle complex tasks with ease.

### Demo Video
https://user-images.githubusercontent.com/6877923/115474571-03c75800-a23e-11eb-8096-8973aad5fa9f.mp4

### Installation

### Full list of arguments

```text
╭─ Name ───────────────────────────────────────────────────────────────────────────────────╮
│   sage                                                                                   │ 
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --shell             Converts natural language prompts into shell commands                │
│ --code              Converts natural language prompts into programs                      │
│ --debug             Detects and debugs errors in shell commands/files and provides fixes │
│ --help              Prints this page and exits                                           │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Assistance Options ─────────────────────────────────────────────────────────────────────╮
│ --code  -f                             Generates code files from natural language prompts│
│ (--debug) /reviewFile ./{file path}    Finds errors in the file and can                  │
│                                        modifies files to fix these errors                │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
```
### Usage
```shell
  sage "What is the distance of alpha centuri from earth?"
```
![Photo]()


```shell
  sage --code "Write a code to add two numbers in java"
```
![Photo]()

```shell
  sage --code -f "sum.java" "Write a code to add two numbers in java"
```
![Photo]()

```shell
    sage --shell
```
![Photo]()

```shell
    sage --debug
```
![Photo]()


