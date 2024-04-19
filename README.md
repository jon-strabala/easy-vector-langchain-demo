## Basic Vector Search Demo using Couchbase, Langchain, and OpenAI

This is a demo app built to highlight basic functionality of vector search of Couchbase to utilize OpenAI embeddings for semantic search.
Once your environment variables are setup and your server has the right resources. 

The demo will run for both self-managed OnPrem 7.6+ Couchbase deployments and also clould based 7.6+ Capella deployments.

If you don't have the time to run the demo you can just download and watch the 4 minute video: [easy-vector-langchain-demo_1920x1080.mp4](https://github.com/jon-strabala/easy-vector-langchain-demo/blob/main/easy-vector-langchain-demo_1920x1080.mp4) 

### Prerequisites 

You will need a database user with login credentials to your Couchbase cluster and an OpenAI API bearer key for this Linux demo

You probably want to create and activate a virtual environment using the standard library’s virtual environment tool venv and install packages.

- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Quick tips on python virtual environments

- Create and activate a virtual environment in the current directory<br><br>
`python3 -m venv .venv`<br>
`source .venv/bin/activate`

- Then when all done deactivate it<br><br>
`deactivate`

### How does this demo work?

It loads ten (10) simple words into a Couchbase collection.

It executes three (3) canned queries against the Couchbase collection containing your vector embeddings.

For each question, you will three ordered answers from your vector search

### How to Run

- Install dependencies

  `pip install -r requirements.txt`

- Copy the template environment template

  `cp _setup.tmpl _setup`

- Required environment variables that you must configure in _setup
  ```
  export CB_HOSTNAME="<the hostname or IP address of your Couchbase server>" 
  export CB_FTSHOSTNAME="<the hostname or IP address of a node running Search in your Couchbase cluster>" 
  export CB_USERNAME="<username_for_couchbase_cluster>" 
  export CB_PASSWORD="<password_for_couchbase_cluster>"
  export OPENAI_API_KEY="<open_ai_api_key>"
  ```

- Note CB_HOSTNAME may not be the same as CB_FTSHOSTNAME.
The evar CB_HOSTNAME is typically an IP in your cluster (or the Capella CONNECT hostname) for the Python SDK to connect to couchbases://${CB_HOSTNAME}. 
The evar CB_FTSHOSTNAME is set to a node running the search service (or fts) for a curl like connection to https://${CB_FTSHOSTNAME}:18094 used for index creation. 

- Optional environment variables that you may alter in _setup

  ```
  export CB_BUCKET=vectordemos
  export CB_SCOPE=langchain
  export CB_COLLECTION=basic
  export CB_SEARCHINDEX=basic_index
  ```

- Source the _setup file (we assume a bash shell) to configure your environment variables

  `. _setup`

- If needed set the executable bit via chmod for the following:

  `chmod +x basic_couchbase_langchain.py  check_couchbase.sh  check_openai.py  setup.py`

- Verify connectivity and authentication to your Couchbase server

  `./check_couchbase.sh`

- Verify connectivity and authentication to OpenAI

  `./check_openai.py`

- Setup the Couchbase infrastructure (bucket, scope, collection and a search vector index) via the bash script

  `./setup.py`

- Run the application

  `./basic_couchbase_langchain.py`

- You should see the following output on the first time your run it

  ```
  text_array to add ['lions', 'tigers', 'bears', 'bicycle', 'car', 'motorcycle', 'rock', 'stone', 'slab', 'block']

  QUERY: vespa
           (Document(page_content='motorcycle'), 0.8247162103652954)
           (Document(page_content='bicycle'), 0.8190407156944275)
           (Document(page_content='car'), 0.8068346977233887)

  QUERY: puma
           (Document(page_content='tigers'), 0.8625560998916626)
           (Document(page_content='lions'), 0.844732403755188)
           (Document(page_content='bears'), 0.8318537473678589)

  QUERY: nugget
           (Document(page_content='slab'), 0.8305376768112183)
           (Document(page_content='stone'), 0.8148258924484253)
           (Document(page_content='rock'), 0.8030873537063599)

  run ./setup.py again and answer 'y' to flush data
  ```

- Other

  Running basic_couchbase_langchain.py multiple times will load the same data again

  You can run `./setup.py` again to get an option to reset your collection (drop/create) and readd your search index.
