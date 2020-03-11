Introduction

- So we dont just want to look at the neighborhood of a pixel, instead we want to look non-locally, to find information to denoise the image.

- Construct a new filtered pixel using values from every other pixel,

- In order to do so, we must assign some weighting according to similarity

  - v is the value of the pixel
  - w is the weighting function
  - NL boils down to sum of every other pixel with weighting.

- What is similarity?

  - Some motivation in this example
    - want to denoise pixel p
      - Look at the patch centered at p
    - To be specific, Say the candidates are q1 and q3.
    - Then q1 is more similar to p than q3, we must give more weighting to q1.
  - For two difference pixels i and j, we define similarity as the euclidean distance between the two patches centered at i and j respectively
    - v is the values of the intensity gray level vector
  - On the other hand we also want to take texture and edges in to consideration
    - Often times nearby pixels have similar texture and edge continuation
    - In this picture
      - want to denoise pixel p, we look at the patch centered at p
      - as an example, the candidates are patch q1 and patch q3
      - q1 and q3 both has same intensity as p, but q1 is more similar to p by texture, thus we should weight q1 more
      - How do we do that?
  - Want to weighting function that takes distance into consideration, the further away from the target pixel, the less a pixel is weighted.
    - we use Gaussian distribution function, where the center is the position of target pixel
    - As distance from center increase, the weighting decrease
  - Putting together we have the weighting function defined such that patches close together with a similar intensity grey level have larger weights.
    - Just a gaussian distribution function
    - Z is the normalizing vector, and h can be thoughted as the degree of filtering
  - Some properties of weighting function
    - all weights are between 0 and 1
    - weight sum up to 1 
    - we expect the difference between two patches to be the difference between the true values of the two patches with a bit of variance
      - implies that from similar patches gets weighted more, actually where the correctness of the algorithm lies dmnfnw ndin
      - nijiushi
  - Putting every thing together

- Implementation

  - The algorithm is easy, for every pixel at position i, calculate values of the filtered image at position  i with the previous show Non-local mean formula.
    - then return the filtered image
  - Implementation can be found on github, we also put our presentation slides and notes in it, you can take a look if you want
  - Complexity is big-Oh of number of pixels times the windows size times the patch size
    - The author suggest that you limit the windows size to 21 times 21 and patch size to 7 times 7 for a good result
    - With such configuration, on my computer it takes 6 hours to finish execution, yours might be faster, but in general not very fast algorithm

- Comparison

  - Visual quality

    - the top left is the noisy image, bottom right is the result of non local mean
    - comparing with gauss filter, anisotropic filter, total variation, neighborhood filtering
    - unlike other filters, non local mean filtering does not degrade or remove details on the texture and edge

  - Method noise

    - Method noise, is the artifact caused by the denoising algorithm

      - for example from the previous image you can see gaussian filtering blur the image
      - ideally we want those artifact to be like gaussian white noise, which is doesn't look bad like gaussian filtering

      - Non local mean has gaussian white noise as the artifact which is good

- Efficiency

  - Again we have discussed, the initial implementation is super slow
  - though result is good, can't really use it on cell phone cameras
  - Further work has been done to improve runtime, like using recursive calculation of similar weight, so you keep track of previous calculations like dynamic programming
  - adaptively choose the windows size of denoising, improve performance

- Types of noise

  - Originally implemented towards Gaussian noise, gaussian noise is an additive noise, but there are many other noise like speckle noise which is an multiplicative noise, which happens a lot in ultrasonic imaging
  - Some further work has done to implement on speckle noise

