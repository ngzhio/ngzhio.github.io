---
title: "Notes on \"Computer Science: An Overview, 12th Edition\""
categories: [Notes]
tags: [computer science]
---

Here are some notes I took while I was reading [*Computer Science: An Overview*, 12th Edition](https://www.amazon.com/dp/B00XN4D0BQ) (Global Edition, 2014) by Glenn Brookshear and [Dennis Brylow](https://www.cs.mu.edu/~brylow/).

![front cover](https://m.media-amazon.com/images/I/51LM1-F57vL.jpg){: .align-right width="25%" }

## Chapter 1. Data Storage

### 1.9 Data Compression

#### Generic Data Compression Techniques

- *Run-length encoding* (lossless): Replacing sequences of identical data elements with a code indicating the element that is repeated and the number of times it occurs in the sequence.
- *Frequency-dependent encoding* (lossless): The length of the bit pattern used to represent a data item is inversely related to the frequency of the item's use. For example, [Huffman codes](https://en.wikipedia.org/wiki/Huffman_coding).
- *Relative encoding*, or *differential encoding* (lossless or lossy): Recording the differences between consecutive data units rather than entire units.
- *Dictionary encoding* (lossless or lossy): Here the term *dictionary* refers to a collection of building blocks from which the message being compressed is constructed, and the message itself is encoded as a sequence of references to the dictionary.
  - *Adaptive dictionary encoding*, or *dynamic dictionary encoding*: The dictionary is allowed to change during the encoding process. For example, [Lempel-Ziv-Welsh (LZW) encoding](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch).

#### Compressing Images

- [*Graphic Interchange Format (GIF)*](https://en.wikipedia.org/wiki/GIF) developed by CompuServe.
  
  It approaches the compression problem by reducing the number of colors that can be assigned to a pixel to only 256. These 256 encodings are stored in a dictionary called the *palette*. Each pixel in an image can then be represented by a single byte whose value indicates which of the 256 palette entries represents the pixel's color. So that GIF is a lossy compression algorithm.

- [*JPEG*](https://en.wikipedia.org/wiki/JPEG) developed by Joint Photographic Experts Group.

  Image compression using the JPEG baseline standard requires a sequence of steps, some of which are designed to take advantage of a human eye's limitations. In particular, the human eye is more sensitive to changes in brightness than to changes in color.

  Starting from an image that is encoded in terms of luminance and chrominance components, then follow these steps:

  1. To average the chrominance values over 2x2 pixel squares. This reduces the size of the chrominance information by a 1/4 while preserving all the original brightness information.
  2. To divide the image into 8x8 pixel blocks and to compress the information in each block as a unit. This is done by applying the [*discrete cosine transform*](https://en.wikipedia.org/wiki/Discrete_cosine_transform).

        > The important point is that this transformation converts the original eight-by-eight block into another block whose entries reflect how the pixels in the original block relate to each other rather than the actual pixel values. Within this new block, values below a predetermined threshold are then replaced by zeros, reflecting the fact that the changes represented by these values are too subtle to be detected by the human eye.

  3. More traditional run-length encoding, relative encoding, and variable-length encoding techniques are applied to obtain additional compression.

  > All together, JPEG’s baseline standard normally compresses color images by a factor of at least 10, and often by as much as 30, without noticeable loss of quality.

### 1.10 Communication Errors
