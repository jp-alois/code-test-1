import torch

def x():
     # check 
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available. Using GPU.")
    else:
        device = torch.device("cpu")
        print("CUDA is not available. Using CPU.")
    x = torch.tensor([1.0, 2.0, 3.0])
x = x.to(device)
print(f"Tensor is on device: {x.device}")

