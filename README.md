# CLI-Sage
Introducing "CLI-Sage" - a command line productivity tool that seamlessly integrates a powerful large language model with your command line interface. Responding to your prompts with programs, shell commands and chats directly from your terminal. Boost your efficiency and creativity by harnessing the combined power of a AI language model and your CLI, making it easier than ever to streamline your workflow and tackle complex tasks with ease.

### Demo Video


### Installation
#### Prerequisites
> Create your OpenAI API key
```shell
https://platform.openai.com/account/api-keys
```

> Python >= v3.10.12 and pip
```shell
sudo apt install python3 pip
```

#### Dependencies

> openai
```shell
pip install openai
```
> coloroma
```shell
pip install colorama
```

#### Configurations

> Clone this repository anywhere and cd into it
```shell
git clone https://github.com/Ansh212/CLI-Sage
```
```shell
cd CLI-Sage
```
> Run setup.py and enter your OpenAI API key
```shell
python3 setup.py
```

### List of arguments

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

  #Sage: The distance from Earth to Alpha Centauri is approximately 4.37 light-years.
```


```shell
  sage --code "Write a code to add two numbers in java"

  # public class AddNumbers {
  #   public static void main(String[] args) {
  #       int num1 = 5;
  #       int num2 = 10;
  #       int sum = num1 + num2;
  #       System.out.println("Sum: " + sum);
  #   }
  # }
```


```shell
  sage --code -f "sum.java" "Write a code to add two numbers in java"

  # Response saved to sum.java
```

```shell
    sage --shell

```
![shell](https://github.com/Ansh212/CLI-Sage/assets/97459476/5bd68bd7-436b-488b-84dd-05ea5f3fe80c)



```shell
    sage --debug
```
![Debug](https://github.com/Ansh212/CLI-Sage/assets/97459476/c0299f69-4c69-417a-b08c-d11ae09e1c3f)


### Declarations

All this code was written during Hackathon.
