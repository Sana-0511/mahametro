# Only for Demonstration Purposes
import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
from matplotlib import pyplot as plt,cm as c
from scipy.ndimage.filters import  gaussian_filter
import scipy
import torchvision.transforms.functional as F
from model import CSRNet
import torch
from torchvision import transforms

transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])

model = CSRNet()

checkpoint = torch.load('./weights.pth', map_location="cpu")
model.load_state_dict(checkpoint)

image_path ="/mnt/c/Users/prana/Documents/mahametro/Crowd_photos/Video2/frame_video2_80.jpg"

plt.imshow(plt.imread(image_path))
plt.show()

img = transform(Image.open(image_path).convert('RGB'))
output = model(img.unsqueeze(0))
print("Predicted Count: ", int(output.detach().cpu().sum().numpy()))
temp = np.asarray(output.detach().cpu().reshape(output.detach().cpu().shape[2],output.detach().cpu().shape[3]))
plt.imshow(temp,cmap = c.jet)
plt.show()
