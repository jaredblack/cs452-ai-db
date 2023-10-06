import argparse
import os
import openai

from query import select_from_table
from schema import get_schema
from db import create_connection

DATABASE = "./horse.db"

def main(conn, prompt):
    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"
    # openai.api_key = os.getenv("OPENAI_KEY")
    print(f"Prompt: {prompt}")

    prompt = f"""
    
    Given the following SQL Schema:{get_schema()}
    Write a valid SQLite query to answer this prompt: {prompt}
    
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )


    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}")
    print("Answer: \n")
    select_from_table(conn, q)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="Who is the best horse?")
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn, prompt=args.query)

