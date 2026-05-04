# /// script
# dependencies = [
#   "langchain-groq",
#   "langchain-core",
#   "python-dotenv",
# ]
# ///
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



def main():

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    
    model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "What is the capital of {country}?"),
    ])

    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    country = input("Enter a country name: ")

    response = chain.invoke({"country": country})
    print(response)

if __name__ == "__main__":
    main()