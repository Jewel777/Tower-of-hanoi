# Tower-of-hanoi


# Tower of Hanoi Visualized in Python 🧠

This project solves the classic **Tower of Hanoi** puzzle using recursion and visualizes it using **matplotlib** in Python.

## 🎯 Features

- Solves the puzzle for any number of disks.
- Animates the movement of each disk.
- Clean and modular Python code.

## 📷 Screenshot

![Example](./screenshot.png) *(optional)*

## 🧪 Requirements

- Python 3.x
- matplotlib

Install with:

```bash
pip install -r requirements.txt



🔍 How It Works
The towers are represented by three Stack objects. 

Disks are represented by integers (1 = smallest, N = largest).

The algorithm uses recursion:

Move N-1 disks from the source to the auxiliary.

Move the largest disk to the destination.

Move N-1 disks from the auxiliary to the destination.

