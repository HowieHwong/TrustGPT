# TRIAD





### How to use Automa for evaluating LLMs in [lmsys](https://chat.lmsys.org/)?

Above all: the script, the files suffixed with json, are based on the automa plugin. Therefore, users need to install Automa in advance, and the following steps are based on the user's completion of the above operations.  

How to install Automa in Chrome or Firefox. [link](https://www.automa.site/)

Step 1: Import the json script in automa.  
Step 2: Create a table in storage to store the testing results ("res" and "action" columns are used as an example).  

![Example](img/table_example.png "Table Example")

Step 3: Insert the prepared prompt content into the block **<em>loop data</em>**.  
Prompt format in **<em>loop data</em>**: [prompt1, prompt2, prompt3, ...]  

Step 4: 