import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    output = []
    for slen in range(seq_len):
        o, v =[], []
        for dlen in range(d_model):
            base_2i = (base**(2*(dlen//2)/d_model))
            if dlen%2 == 0:
                v =  np.sin(slen/base_2i)
            else:
                v =  np.cos(slen/base_2i)
            o.append(v)
        output.append(o)
        
    return np.array(output)


        