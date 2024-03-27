#!/usr/bin/env python3

import os
import time
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
from langchain_community.vectorstores import CouchbaseVectorStore
from langchain_openai import OpenAIEmbeddings

pa = PasswordAuthenticator(os.getenv("CB_USERNAME"), os.getenv("CB_PASSWORD"))
# cluster = Cluster("couchbase://" + os.getenv("CB_HOSTNAME"), ClusterOptions(pa))
cluster = Cluster("couchbases://" + os.getenv("CB_HOSTNAME") + "/?ssl=no_verify", ClusterOptions(pa))

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")) 

vs = CouchbaseVectorStore(cluster, "vectordemos", "langchain", "basic", embeddings, "basic_index")

text_array = ["lions", "tigers", "bears", "bicycle", "car", "motorcycle", "rock", "stone", "slab", "block"]
print("text_array to add", text_array ,"\n")
res = vs.add_texts(text_array, batch_size=2)
# print("Docs created with IDs:", res, "\n")

time.sleep(1)
for query in ["vespa", "puma", "nugget"]:
    print("QUERY:", query)
    results = vs.similarity_search_with_score(query, k=3)
    for result in results:
        print("\t",result)
    print("")

print("run ./setup.py again and answer 'y' to flush data")
# print("flushing bucket vector_demo_sdk, this may take some time")
# cluster.buckets().flush_bucket("vector_demo_sdk")
