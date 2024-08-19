import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image

# Định nghĩa các phép biến đổi dữ liệu
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Tải tập dữ liệu MNIST
mnist_train = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
mnist_test = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# Lấy một hình ảnh và nhãn từ tập dữ liệu
image, label = mnist_train[0]

# Chuyển đổi hình ảnh từ tensor sang PIL Image để lưu
image_pil = transforms.ToPILImage()(image * 0.5 + 0.5)
image_pil.save("image.png")

# Chuyển đổi hình ảnh từ tensor sang numpy array để hiển thị
image = image * 0.5 + 0.5
image_np = image.numpy().squeeze()

# Hiển thị hình ảnh
plt.imshow(image_np, cmap="gray")
plt.title(f'Label: {label}')
plt.show()
