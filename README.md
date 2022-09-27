# QA_Search_Engine
A search engine implementation for a question answering data set.

<h2>Motivation</h2>

With the increase of documents on the internet, our queries and types of queries are also getting vast. Search Engines help user to quickly find most relevant information based on query. Stack Overflow is a question-and-answer (Q&A) website for professional and enthusiast programmers. It only accepts questions about programming that are tightly focused on a specific problem. 

During our systematic study we have found that Retrieval in a question-and-answer dataset require retrieving related questions which have been asked before with good answers for a user’s query. In contrast to typical document retrieval, a retrieval model for this task should take into consideration the question similarity as well as the similarity of the relevant answers for the retrieved questions. After exploring several data sets such as the data dumps available from Quora, we decided to use the LinkSo Data set, which has been derived from Stack Overflow question answer data dump. 

<h2>Implementation</h2>

Experimentation of different information retrieval models for question answer data, based on ‘LinkSo’ data set using semantic search. Implement different IR models like BM25, and Language model and then experiment on dataset to retrieve relevant documents. 

The objective of this project is to learn about different Indexing and retrieval algorithms and how they work, better utilization of inhouse knowledge bases, high precision & recall, scalability, given a repository of question & answer dataset, which models work better. Further we want to compare the results of each model. 

The focus is to develop a search engine which give ordered list of answers with first one being the most relevant to user’s query. Our hypothesis is that semantic search should retrieve more relevant information and would perform better on evaluation. We will try to find and corroborate our hypothesis empirically. 

<h2>Architecture</h2>

<p>&nbsp;</p>
<kbd>
<img src="https://user-images.githubusercontent.com/14356479/192401836-9a88570d-2821-446f-b8b0-fcd5e63b5ee4.jpg"  width="1000" ></kbd>
