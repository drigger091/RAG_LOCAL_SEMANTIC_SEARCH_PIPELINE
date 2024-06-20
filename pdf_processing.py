import random
from tqdm.auto import tqdm
import re
from text_format import open_and_read_pdf, split_into_sentences

def split_list(input_list: list, slice_size: int = 10) -> list[list[str]]:
    """
    Splits the input_list into sublists of size slice_size (or as close as possible).
    
    For example, a list of 18 sentences would be split into two lists of [[10], [8]].
    """
    return [input_list[i:i + slice_size] for i in range(0, len(input_list), slice_size)]

def update_pages_with_chunks(pages_and_texts, num_sentence_chunk_size=10):
    """
    Updates pages_and_texts with sentence chunks and their counts.
    
    Parameters:
    pages_and_texts (list): List of pages and texts.
    num_sentence_chunk_size (int): Number of sentences per chunk.
    
    Returns:
    list: Updated pages_and_texts with sentence chunks and their counts.
    """
    pages_and_texts2 = split_into_sentences(pages_and_texts)
    
    for item in tqdm(pages_and_texts2):
        item["sentence_chunks"] = split_list(input_list=item["sentences"], slice_size=num_sentence_chunk_size)
        item["num_chunks"] = len(item["sentence_chunks"])
    
    return pages_and_texts2

def create_pages_and_chunks(pages_and_texts2):
    """
    Creates a list of pages and chunks from the updated pages_and_texts2.
    
    Parameters:
    pages_and_texts2 (list): List of pages and texts with sentence chunks.
    
    Returns:
    list: List of pages and chunks with their stats.
    """
    pages_and_chunks = []

    for item in tqdm(pages_and_texts2):
        for sentence_chunk in item["sentence_chunks"]:
            chunk_dict = {}
            chunk_dict["page_number"] = item["page_number"]

            # Join the sentences together in the list into a simple paragraph
            joined_sentence_chunk = " ".join(sentence_chunk).replace(" ", "").strip()
            joined_sentence_chunk = re.sub(r'\.([A-Z])', r'. \1', joined_sentence_chunk)

            chunk_dict["sentence_chunk"] = joined_sentence_chunk

            # Get stats about chunk
            chunk_dict["chunk_char_count"] = len(joined_sentence_chunk)
            chunk_dict["chunk_word_count"] = len(joined_sentence_chunk.split(" "))
            chunk_dict["chunk_token_count"] = len(joined_sentence_chunk) / 4  # 1 token = 4 chars

            pages_and_chunks.append(chunk_dict)

    return pages_and_chunks

def process_pdf(pdf_path, num_sentence_chunk_size=10):
    """
    Main function to process the PDF and return pages and chunks.
    
    Parameters:
    pdf_path (str): Path to the PDF file.
    num_sentence_chunk_size (int): Number of sentences per chunk.
    
    Returns:
    list: List of pages and chunks with their stats.
    """
    # Step 1: Read PDF and get pages and texts
    pages_and_texts = open_and_read_pdf(pdf_path=pdf_path)

    # Step 2: Split pages and texts into sentences and chunks
    updated_pages_and_texts = update_pages_with_chunks(pages_and_texts, num_sentence_chunk_size=num_sentence_chunk_size)

    # Step 3: Create pages and chunks with stats
    pages_and_chunks = create_pages_and_chunks(updated_pages_and_texts)

    return pages_and_chunks
