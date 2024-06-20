from pdf_processing import process_pdf
import random
import pandas as pd

# Define the PDF path and number of sentences per chunk
pdf_path = "Nutrition_text_book.pdf"
num_sentence_chunk_size = 10

# Process the PDF to get pages and chunks
pages_and_chunks = process_pdf(pdf_path, num_sentence_chunk_size)


# filtering the count_token_length to above 30

min_token_length = 30

def filter_token(pages_and_chunks,min_token_length):
    df = pd.DataFrame(pages_and_chunks)
    pages_and_chunks_over_min_token_limit = df[df["chunk_token_count"]>=min_token_length].to_dict(orient="records")

    return pages_and_chunks_over_min_token_limit

updated_token_list = filter_token(pages_and_chunks,min_token_length)

print(random.sample(updated_token_list,k=1))
