from Filter import filter_token
from pdf_processing import process_pdf
from sentence_transformers import SentenceTransformer
import time
from tqdm.auto import tqdm
import pandas as pd


# Define the PDF path and number of sentences per chunk
pdf_path = "Nutrition_text_book.pdf"
num_sentence_chunk_size = 10
# Process the PDF to get pages and chunks
pages_and_chunks = process_pdf(pdf_path, num_sentence_chunk_size)
# Define the minimum token length for filtering
min_token_length = 30
# Filter the chunks based on the minimum token length
updated_token_list = filter_token(pages_and_chunks, min_token_length)



# Load the model
Embedding_model = SentenceTransformer(model_name_or_path='all-mpnet-base-v2',device = "cpu")

def  embed_chunks(updated_token_list):
      start_time = time.time()
      text_chunks =[item['sentence_chunk'] for item in updated_token_list]

      Embedding_model.to("cpu")
      text_chunk_embedding = Embedding_model.encode(text_chunks,batch_size = 8,convert_to_tensor = True)
      end_time = time.time()
      total_time = end_time - start_time
      print(total_time)
      return updated_token_list


updated_token_list = embed_chunks(updated_token_list)
#convert into df

text_chunks_and_embeddings_df = pd.DataFrame(updated_token_list)
embeddings_df_save_path = "Text_chunks_and_embeddings.csv"
text_chunks_and_embeddings_df.to_csv(embeddings_df_save_path)


      









