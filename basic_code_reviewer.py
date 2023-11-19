import openai
from dotenv import dotenv_values, load_dotenv
import os
import argparse # used for command line arguments

prompt="""
You will receive a file's contents as text.
Generate a code review for the file. Indicate what changes should be made to it's style, performance, readability and maintainability.
If there are any reputable libraries that could be introduces to improve code suggest them.
Be kind and constructive.
For each suggested change include line numbers to which you are refering.
"""

def basic_code_review(file_path, model):
    with open(file_path,'r') as file:
        content = file.read()
    print(basic_code_review_request(content, model)["choices"][0]["message"]["content"])

def basic_code_review_request(filecontent, model):
    messages = [
        {"role":"system", "content":prompt},
        {"role":"user","content":f"Code review the following file: {filecontent}"},
    ]

    result = openai.ChatCompletion.create(
        model=model,
        messages = messages,
    )
    return result

def main():
    # argument parser
    parser = argparse.ArgumentParser(description="simple code reviewer for a file")
    parser.add_argument("file")
    parser.add_argument("--model",default="gpt-4")
    args = parser.parse_args()

    # call for the function
    basic_code_review(args.file, args.model)

if __name__=="__main__":
    # passing the API Key to OpenAI
    # note while using this code create a ".env" file in the current file location and paste "OpenAI_secret_key='your OpenAI key'"
    load_dotenv()
    openai.api_key = os.getenv('OpenAI_secret_key')

    # call for main function
    main()