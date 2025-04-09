# KnotebookLM RAG Service

This RAG is used to take text and break it down to use for potentially finding things about the text 

What it does, is it takes the text and splits it into seperate chunks in order to handle the whole thing better.  Once it splits the text into multiple chunks, it sends those chunks to an api key where it takes those chunks into another RAG serivice.  From there it takes each word in those splits, and puts in meaning space.  In other words it takes each word and gives it a set of values in order to relate it with other words.  This can then be used to generate text to create an AI in the future.  