import pandas as pd
import torch

def load_embedding_data(pt_filepath, name, layer):
    pt_file = torch.load(f"{pt_filepath}/{name}.pt",weights_only=True)
    labels = pt_file['label']
    mean_representations = pt_file['mean_representations']

    layer_data = {
        'Name': labels,  # Sequence names
        **{f'D{i+1}': mean_representations[layer][i].item() for i in range(len(mean_representations[layer]))}
    }
    embedding_df = pd.DataFrame([layer_data])
    embedding_df = embedding_df.set_index('Name')
    X = embedding_df.values
    return embedding_df.index, X
