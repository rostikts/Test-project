# TestTask

## Contacts

This project was interesting and I would be so glad to get
feedback from reviewer.

My LinkedIn profile

www.linkedin.com/in/rostikts

My email:

rostiktsyapura.@gmail.com


## General information
This is test project for a automation QA vacancy.
Main goal of this project is to show my abilities to  automate test cases with the Python programming language using Selenium WebDriver and unittest framework.

## Project implementation

This project have abstraction layers wich simplified maintenance and implementing new features. In this project 
was used the page object pattern. In elements.py are described all general page objects like a buttons, text fields
and implemented methods wich helps to manipulate with this objects easyer.

Modules in the page folder contains clases where implemented main actions on the pages.

Modules in the locators folder are defined locators of all general objects on the page.

The main.py module contains class with main test scenarios.

## Test scenarios

#### Scenario 1. User is able to specify age of each child

1. go to home page
2. open menu for selecting strangers number
3. specify N number of children (N > 1)
Expect: the number of age inputs is equal to N

#### Scenario 2. User is required to specify booking date to see booking price
Preconditions:

User is at home page
1. choose any city from the menu below

Expect:
- page with listed hotels is opened
- calendar for specifying check in date is opened
- no result entry containing booking price or booking status
2. Click "show prices" button for any hotel

Expect: calendar for specifying check in date is opened

3. Set any dates for check in and out
4. Submit search form

Expect: each result entry has booking price or banner saying no free places

## Instruction

#### Step 1 – configure environment.

For configuration open terminal in project’s folder and type command

    pip install -r requirements.txt

#### Step 2 – configure local server

Open terminal in webdriver folder and run command

    java -jar server.jar

#### Step 3 – Execution 

Open terminal in project’s folder and type command

    python main.py
    
Than choose index of browser(Chrome - 0, Firefox - 1)

## Bugs

During the test task was found one minor bug

#### Bug summary

Date is not selected on the date bar while scrolling the page




