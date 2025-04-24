# KnotebookLM RAG Service

This RAG is used to take text and break it down to use for potentially finding things about the text 

What it does, is it takes the text and splits it into seperate chunks in order to handle the whole thing better.  Once it splits the text into multiple chunks, it sends those chunks to an api key where it takes those chunks into another RAG serivice.  From there it takes each word in those splits, and puts in meaning space.  In other words it takes each word and gives it a set of values in order to relate it with other words.  This can then be used to generate text to create an AI in the future.  

This service uses libraries from langchain. 
It uses RecursiveCharacterTextSplitter from langchain_text_splitters, and Document from langchain_core.documents 
It also uses request and Flask from the flask library
Then it needs to import request, json, sys, and pysqlite3

To install these it is neceassary to pip install each library by tying in the terminal:"pip install" and the library you want to download.  

# How to Work the Code

1. First you add the text you want to embed into the text.txt file.  
2. Second you run api.py in the terminal, and then open a second terminal while that's runing
3. Once you have done that, you can give a request by opening a second terminal and running a post request from there. 
    - You could use the post.py file as a reference to how to make a post request
    - If it is successful, you should have the embedding ids returned and a message saying "Request Successful" otherwise it will return an error

    