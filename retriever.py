#retriever.py
import sys
import lucene

from java.io import File
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field
from org.apache.lucene.search import IndexSearcher, BooleanClause
from org.apache.lucene.index import IndexReader, DirectoryReader
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser, QueryParserBase
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.search.similarities import ClassicSimilarity, BM25Similarity, LMDirichletSimilarity, BooleanSimilarity
import string

def retriever_fn(search_string, index_pth_str="index/"):
    
    analyzer = EnglishAnalyzer()
    indexPath = File(index_pth_str).toPath()
    indexDir = FSDirectory.open(indexPath)
    reader = DirectoryReader.open(indexDir)
    searcher = IndexSearcher(reader)
    searcher.setSimilarity(BM25Similarity(1.0, 0.5))

    fields = ['qns_title_processed', 'qns_body_processed', 'ans_body_processed']
    flags = [BooleanClause.Occur.SHOULD, BooleanClause.Occur.SHOULD, BooleanClause.Occur.SHOULD]
    query_parser = MultiFieldQueryParser(fields, analyzer)
    query = query_parser.parse(search_string, fields, flags, analyzer)
    MAX = 10
    hits = searcher.search(query, MAX)

    print("\nFound %s document(s) that matched the query :" % hits.totalHits.toString())
    for ind,hit in enumerate(hits.scoreDocs):
        doc = searcher.doc(hit.doc)
        print("\nRank = ",ind)
        print("Score = ",hit.score)
        print("qn_id : ",doc.get("qid"))
        print("qn_title : ",doc.get("qn_title"))
        print("qn_link : ",doc.get("qn_link"))
    print("\n")

if __name__ == "__main__":
    
    lucene.initVM() 
    table = str.maketrans(dict.fromkeys(string.punctuation))  
    
    search_string = input("Please enter your search string (if you want to terminate please type EXIT) = :\n")  
    print(search_string)
    while(search_string != "EXIT"):
        new_str = search_string.translate(table) #filter punctuations
        retriever_fn(str(new_str))
        search_string = input("Please enter your search string (if you want to terminate please type EXIT) = :\n")
        print(search_string)
