<a id="title"></a>
# Test Practice on **Sauce Demo** Sandbox Website
This project explores Quality Assurance and automated testing techniques using the Page Object Model (POM). This is created to demonstrate how to structure and build automated tests to maintain web application effectively. This project focuses on testing **Sauce Demo's** app which provides a sandbox for testing e-commerce websites. 

> Note to recruiter:
> Hello po Sir Eric and RJ. Please consider this Github repo as my latest work. Apologies po for the oversight as I forgot to read my emails last Wednesday. Nevertheless, thank you pa rin po for this opportunity you have given me!

## Table of contents
- [Test Practice on **Sauce Demo** Sandbox Website](#test-practice-on-sauce-demo-sandbox-website)
  - [Table of contents](#table-of-contents)
  - [Tech Stack:](#tech-stack)
  - [Usage](#usage)
  - [Tested Pages](#tested-pages)
  - [Project Structure](#project-structure)
  - [Github Workflow](#github-workflow)

<a id="tech-stack"></a>
## Tech Stack:
1. Programming Language - `python`
2. Testing Library - `pytest`
3. Automation Library - `Selenium`
4. Reporting Format - `JUnit`
5. CICD Platform - `Github Actions/Workflow`

<a id="usage"></a>
## Usage
To replicate a collaborative development environment, GitHub Workflows is setup to automate remote test runs whenever an individual pushes or creates a pull request to the repository. \
\
Additionally, an ad-hoc test run of the workflow can be performed using the following steps.
1. In the repository home, click on the 'Actions' tab of the repository and navigate to the 'test' workflow. You will then find previous runs of the test cases. 
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/7d12d335-161a-47d2-a23d-48b18c21225f" alt="Go to Workflow" height="250">
</p>
2. From the list of workflow runs, click the name of the run to see details and other options.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/a6e6429a-567d-4ab6-a29c-48dac6a4396b" alt="Go to Workflow" width="750">
</p>
3. In the upper-right corner of the workflow, re-run all jobs. If a prompt asks to rerun, just click Re-run jobs. 
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/bcb0a374-b3fb-4555-a261-82b8ca8cd52c" alt="Go to Workflow" width="750">
</p>
4. Once all the jobs are finished, go to the Artifact section below to download the test reports.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/0eee6339-dbce-4d19-a267-03d6ce5f404e" alt="Go to Workflow" width="750">
</p>
> You can also view details on the job by clicking on the job name in the left pane under 'jobs' section.
<p align="center">
<img src="https://github.com/jbeaver-abellera/the-internet_pytest-suite/assets/108796284/7736a012-5ce2-496e-9cfc-41fb3cf2a8d0" alt="Go to Workflow" height="250">
</p>

<a id="tested-pages"></a>
## Tested Pages 
This automated test covers several tasks a user might perform in the website, which includes:
* `Login` - The user must be able to login if they entered the correct credentials.
* `Add to Cart` - User must change the sorting of the items, add to cart the first 'n' results, and see that the cart badge has 'n' items.
* `And many more to come!`

<a id="project-structure"></a>
## Project Structure
This project follows an organized structure for automated UI testing projects. Here is a brief description of structure.
* **Root Folder**
   Contains subdirectories and configuration files for the project. This includes a gitignore, readme, requirements.txt for dependencies, pytest's conftest.py, etc.
* **.github/**
   Contains all the configuration for the testing pipeline in Github Workflow CI/CD.  
* **junit/**
  Contains test results
* **PageClasses/**
  Directory of classes of pages that is tested by this project. A POM model is implemented for the web application, to create reusable and separated code for each pages.
* **tests/**
  Has all the files for testing the web app. Due to the nature of the website, test will be conducted for each page, instead of mimicking user interaction like buying an item.
* **utils/**
  Directory of python methods that are helpful for project files. This includes a constants file, and WebDriverSingleton() that ensures driver is created and closed only once.
    
<a id="workflow"></a>
## Github Workflow
For this project, CICD platform Github Workflow is used for automated testing of the webpage. See below for how it is setup:
1. **Trigger Workflow**: The workflow will be run at every push or pull request to the main branch.
2. **Setup Environment**: To tell github workflow the configuration of the environment such as the OS, and to use the docker image for Selenium. 
3. **Code Checkout**: The workflow will checkout the files in this repository, as well as setup python and the required libraries.
4. **Test Executon**: It will now run the test usng pytest along wiith some options such as handling warnings and capturing results.
5. **Uploading Results**: When the tests are complete, the workflow will locate the test results and upload them to the 'Artifacts' section of the job run.
