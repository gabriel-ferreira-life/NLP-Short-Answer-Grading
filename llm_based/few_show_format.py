import pandas as pd

def few_shot_format(row):
    """
    Create formatted string for a single few-shot example.
    """
    output_format = f"""---
    Question: {row['Question']},
    Response: {row['Response']},
    Correct Answer: {row['CorrectAnswer']},
    Label: {row['label']} \n"""

    return output_format

# Create few shot examples
def create_few_shot_examples(df, n=2):
    """
    Randomly sample n examples from each label (1, 0, -1)
    """
    
    # Group by label
    label_groups = {label: df[df['label'] == label] for label in [1, 0, -1]}

    # Sample n rows per label, with replacement if needed
    sampled_dfs = []
    for label, group_df in label_groups.items():
        if group_df.shape[0] < n:
            sampled = group_df.sample(n=n, replace=True, random_state=42)
        else:
            sampled = group_df.sample(n=n, random_state=42)
        sampled_dfs.append(sampled)

    # Concatenate the sampled DataFrames
    sampled_df = pd.concat(sampled_dfs).reset_index(drop=True)
    return sampled_df