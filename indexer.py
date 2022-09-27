# indexer.py
import sys
import lucene

from java.io import File
from org.apache.lucene.analysis.en import EnglishAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, StringField, FieldType
from org.apache.lucene.index import IndexWriter, IndexWriterConfig, IndexOptions
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.search.similarities import ClassicSimilarity, BM25Similarity, LMDirichletSimilarity, BooleanSimilarity
import pandas as pd

def indexing_docs(file_path):
    lucene.initVM()
    indexPath = File("index/").toPath()
    indexDir = FSDirectory.open(indexPath)
    writerConfig = IndexWriterConfig(EnglishAnalyzer())
    writerConfig.setSimilarity(BM25Similarity(1.0,0.5))
    writer = IndexWriter(indexDir, writerConfig)
   
    t1 = FieldType()
    t1.setStored(True)
    t1.setTokenized(False)
    t1.setIndexOptions(IndexOptions.NONE)
   
    t2 = FieldType()
    t2.setStored(False)
    t2.setTokenized(True)
    t2.setIndexOptions(IndexOptions.DOCS_AND_FREQS)
   
    df_file = pd.read_csv(file_path)
    cntr = 0
    for i, row in df_file.iterrows():
        doc = Document()
        doc.add(Field("qid", row['qid'], t1))
        doc.add(Field("qn_title", row['qn_title'], t1))
        doc.add(Field("qn_link", row['qn_link'], t1))
        doc.add(Field("qns_title_processed", row['qns_title_processed'], t2))
        doc.add(Field("qns_body_processed", row['qns_body_processed'], t2))
        doc.add(Field("ans_body_processed", row['ans_body_processed'], t2))
        writer.addDocument(doc)
        print("Indexed document = ", i)
        cntr += 1
       
    print("\nIndexed %d records (%d docs in index)" % (cntr, writer.getDocStats().numDocs))
    print("Closing index of %d docs..." % writer.getDocStats().numDocs)
    writer.close()
    indexDir.close()
         
if __name__ == '__main__':
    file_path = input("Please enter the csv file path = :\n")
    print(file_path)
    indexing_docs(file_path)


