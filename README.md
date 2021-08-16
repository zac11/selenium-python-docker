# selenium-python-docker
## Use Python Selenium with docker

This is just a sample of how to run Selenium test cases with a Docker image.

## Docker Image
The docker image is take from here - [https://github.com/joyzoursky/docker-python-chromedriver]( Repo )

Shout out to creator `joyzoursky` for this repo. You can really use any other python versions from his repo and
use the docker file to run the test cases.

The docker file is based off on a debian image and has Python 3.9, and latest Chromedriver along with
`Selenium 3.141.0` installed ( which is the latest stable version).

In case you want to try the alpha/beta versions of Selenium, just change the last command where Selenium is installed 
to

`pip install selenium={version_you_want}`

for eg, the latest version is 4.0.0.b4 as of June 8,2021, so you would need to do

`pip install selenium==4.0.0.b4`


## Test Script

It is a very simple test script. The sample test script tries to go to the
[https://the-internet.herokuapp.com/]( Internet ) page and perform a couple of click operations

The script contains a test case that passes and a test case that fails.

## Build And Execution
To build the docker image , first you need to have docker installed on your system. If you do not have docker installed,
then go to Google and search for the same and then come back to this step.

To build the docker image, run

`docker build -t sel-doc .`

The command basically tells docker to use the Dockerfile situated in the pwd (specified by .) and build an executable 
image.
The name `sel-doc` is a tag assigned to this image. This will be useful once we run the image to build a container.
You can use any name for this tag.


Once the image is build successfully, we will use this below command to run the test case

`docker run -it -w /usr/workspace -v $(pwd):/usr/workspace sel-doc /bin/bash`

Let us understand this command -

`docker run` command is used to execute a built image, which we already built in the previous step.

`docker run -it` means the run command opens an interactive terminal

The next part of the command is rather interesting. Here what we are doing is

`-w /usr/workspace` - here in this command we're setting the current working directory of the execution to
`/usr/workspace`

`-v $(pwd):/usr/workspace` - In this command we're using the volume mapping functionality of docker to map a 
disk volume to a specific work directory in the docker. This will mount the present working directory of the user
on your system to the `/usr/workspace` directory inside the docker container.

You can avoid this volume mapping if you want to not use a volume mapping by copying the files present in the 
present working directory inside the Dockerfile using the `COPY` command.


`sel-doc /bin/bash` - Since `sel-doc` is the name of the tag that we gave this image when we built it, we're going
to use that to execute the image and create our container. `/bin/bash` is simply stating that we need the `bash` 
terminal opened when the run command is executed.

Once you execute this command, docker will open the shell of the container for you, something like this

`root@d20a07d21c95:/usr/workspace# `

which is the `/usr/workspace` of the `root` user in this container.

Once inside the container, run this command

`python demo_use_case.py`

this will start the selenium execution.


## Results

Since we already designed one test case to pass and one to fail, it will show one pass and one failed. Sample output

```root@010baba0f715:/usr/workspace# python demo_use_case.py 
test_case_1 (__main__.TestCaseTemp) ... ok
test_case_2 (__main__.TestCaseTemp) ... FAIL

======================================================================
FAIL: test_case_2 (__main__.TestCaseTemp)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/workspace/demo_use_case.py", line 33, in test_case_2
    el1 = self.driver.find_element_by_css_selector('#dropdown')
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"#dropdown"}
  (Session info: headless chrome=92.0.4515.131)


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/workspace/demo_use_case.py", line 36, in test_case_2
    self.fail(ex2.msg)
AssertionError: no such element: Unable to locate element: {"method":"css selector","selector":"#dropdown"}
  (Session info: headless chrome=92.0.4515.131)

----------------------------------------------------------------------
Ran 2 tests in 19.768s

FAILED (failures=1)```


