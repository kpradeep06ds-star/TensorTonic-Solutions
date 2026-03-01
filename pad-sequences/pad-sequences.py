import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    r, c = len(seqs), max([len(i) for i in seqs])
    if max_len is not None:
            c = max_len
    output = []
    for s in seqs:
        lens = len(s)
        if c > lens:
            s.extend([pad_value]*(c - lens))
        elif c < lens:
            s = s[0:(c - lens)]
        output.append(s)
    return output
        