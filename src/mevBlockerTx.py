from dune_client.client import DuneClient
from dune_client.types import QueryParameter
from dune_client.query import QueryBase
import os
from dotenv import load_dotenv
load_dotenv()


#extract the x hashes that went through mev blocker
def get_tx(block_number):
    dune = DuneClient(
        api_key=os.getenv("DUNE_API_KEY"),
        base_url="https://api.dune.com",
        request_timeout= 30000
    )

    query = QueryBase(query_id = 3769799, 
            params=[
                QueryParameter.text_type(name="blocknumber", value=block_number)])
    df = dune.run_query_dataframe(query=query, batch_size = 1000)
    return list(df['user_tx'])