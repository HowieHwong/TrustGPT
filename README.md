# TRIAD

TRIAD is a benchmark used to assess ethical considerations of large language models (LLMs). It evaluates from three perspectives: toxicity, bias, and value-alignment.  

## Overview


## News

*** **UPDATE** ***


## Model


## Dataset


## Headboard


## How to ues TRIAD?


### How to use Automa for evaluating LLMs in [lmsys](https://chat.lmsys.org/)?

Above all: the script, the files suffixed with json, are based on the automa plugin. Therefore, users need to install Automa in advance, and the following steps are based on the user's completion of the above operations.  

How to install Automa in Chrome or Firefox: [link](https://www.automa.site/)

Step 1: Import the json script in automa.  
Step 2: Create a table in storage to store the testing results ("res" and "action" columns are used as an example).  

"res" column means generation results of LLMs and "action" means social norm in prompt template.
<img src="img/table_example.png" alt="Table Example" width="500" height="300">


Step 3: Insert the prepared prompt content into the block **<em>loop data</em>**.  
Prompt format in **<em>loop data</em>**: 
```
[prompt1, prompt2, prompt3, ...]  
```

Step 4: In the click button, set the LLMs number tested in this run (based on the number selected by the [lmsys](https://chat.lmsys.org/) page, the corresponding relationship between model selection and index number is shown in the figure below).  

<img src="img/model_index.png" alt="Model Index" width="350" height="500">



Step 5: Click the binding link between table and the table created in storage.  
Step 6: Click block **<em>get text</em>** and select the columns to store results and corresponding prompt after getting the text.  

**Optional operations:**  
Delay setting: Set the delay time to adapt to the user operating environment. If the script is too slow, it takes a long time to run. If the script is too fast, the text generation process may not be completed.  

As the lmsys website undergoes changes, the aforementioned scripts may no longer be applicable. If you still wish to utilize these large language models, we highly recommend you to learn how to use [automa](https://docs.automa.site/) or deploying the models locally for optimal usage.  