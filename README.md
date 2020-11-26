# GRAIL

Implementing a participant registry microservice with an API that supports adding, updating, removing and retrieving personal information about participants in the study.

Assumption made that there is already a separate microservice with an API that can be used to allocate unique reference numbers to new participants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Run

- Clone this repo to your local machine using:

```
git clone https://github.com/vagifaliyev/GRAIL
```

- The functions craeted can be imported as suchL
```
from grail import *
```

## Functions 

info - dictionary containing the data on information  
ref - Reference Number
sec - section interested in (i.e Name)

### Verify 

Checks if the ref and sec exist in info.
Returns booleans for both of the checks and prints out an error for the user.

```
verify(info,ref,sec)
```

### Add 

Prints out the current information in ref at sec and prompts the user to input to append to the data.
```
add(info,ref,sec)
```

### Update 

Prints out the current information in ref at sec and prompts the user to input to replace the data.

```
update(info,ref,sec)
```


### Remove 

Prints out the current information in ref.
```
retrive(info,ref)
```

## Running the test

```
python3 test.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/vagifaliyev/Matrix-Solver/blob/master/LICENSE) file for details.
