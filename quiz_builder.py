# task_6

import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from pdf_processing import DocumentProcessor
from embedding_client import EmbeddingClient
from chroma_collection_creator import ChromaCollectionCreator

if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-quizify-431202",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        #st.header("Quizzify")
        
        # 1) Initalize DocumentProcessor and Ingest Documents from pdf_processing
        document_processor = DocumentProcessor()
        document_processor.ingest_documents()
        # 2) Initalize the EmbeddingClient from embedding_client with embed config
        embedding_client = embedding_client = EmbeddingClient(**embed_config)
        # 3) Initialize the ChromaCollectionCreator from chroma_collection_creator
        chroma_creator = ChromaCollectionCreator(document_processor, embedding_client)

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
            # 4) Use streamlit widgets to capture the user's input
            topic_input = st.text_input('Topic for Generative Quiz', type="default", placeholder="Enter the Topic of the Document")
            # 4) for the quiz topic and the desired number of questions
            questions = st.slider("Number of Questions", min_value=1, max_value=10 )
            #st.write(questions, "questions will be generated")

            
            document = None
            
            submitted = st.form_submit_button("Generate a Quiz!")
            if submitted:
                
                # 5) Use the create_chroma_collection() method to create a Chroma collection from the processed documents
                chroma_creator.create_chroma_collection()         
                # Uncomment the following lines to test the query_chroma_collection() method
                document = chroma_creator.query_chroma_collection(topic_input) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)