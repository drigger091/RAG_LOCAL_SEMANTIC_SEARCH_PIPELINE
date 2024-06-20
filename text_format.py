import fitz
from tqdm.auto import tqdm
from spacy.lang.en import English

def text_formatter(text: str) -> str:
    """Perform formatting on text"""
    cleaned_text = text.replace("\n", "").strip()
    return cleaned_text

def open_and_read_pdf(pdf_path: str) -> list[dict]:
    """
    Opens a PDF file, reads its text content page by page, and collects statistics.
    
    Parameters:
    pdf_path (str): The path to the PDF document to be opened and read.
    
    Returns:
    list[dict]: A list of dictionaries each containing the page number (adjusted),
    character count, word count, sentence count, token count, and extracted text for each page.
    """
    doc = fitz.open(pdf_path)  # open the document
    pages_and_texts = []

    for page_number, page in tqdm(enumerate(doc, start=1)):  # page numbers start at 1
        text = page.get_text()
        cleaned_text = text_formatter(text)
        pages_and_texts.append({
            "page_number": page_number - 41,  # adjust page number if necessary
            "page_char_count": len(cleaned_text),
            "page_word_count": len(cleaned_text.split()),
            "page_sentence_count": len(cleaned_text.split(".")),
            "page_token_count": len(cleaned_text.split()),  # token count as word count
            "text": cleaned_text
        })

    return pages_and_texts

def split_into_sentences(pages_and_texts: list[dict]) -> list[dict]:
    """
    Splits the text of each page into sentences using Spacy's sentencizer.
    
    Parameters:
    pages_and_texts (list[dict]): A list of dictionaries with text data for each page.
    
    Returns:
    list[dict]: Updated list with sentences split and sentence count added.
    """
    nlp = English()
    nlp.add_pipe("sentencizer")

    for item in tqdm(pages_and_texts):
        doc = nlp(item["text"])
        sentences = [str(sent) for sent in doc.sents]
        item["sentences"] = sentences
        item["page_sentence_count_spacy"] = len(sentences)
    
    return pages_and_texts

# Define the path to the PDF
pdf_path = "Nutrition_text_book.pdf"

# Process the PDF to extract text and statistics
pages_and_texts = open_and_read_pdf(pdf_path)

# Split text into sentences using Spacy
pages_and_texts = split_into_sentences(pages_and_texts)


