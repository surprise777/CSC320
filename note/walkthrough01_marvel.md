# Non-local Mean Algorithm

## Self Introduction

Hi I am Jinny, and this is jefferson, We are gonna introduce Non-local Mean filtering Algorithm for image denoising.

* So here's our agenda today: 

* we will first give u a bref introduction about our problem space, the image noise actually, 
* and some background information about the image denoising method. 
* Then we will talk about some typical smoothing filters algorithm with their performance. 
* Then We will focus on the Non-local Mean Algorithm, giving you definition, formula and consistency. 
* We will also show your our own implementation of non-local algorithm with a living demo, and the result comparision with other classical local smoothing algorithm. 
* Finally we will have a bref discussion about the limitation of the Non-local Mean algorithm and insignts of future works.

OK Now let's start from the problem - Noise.

## Problem - Noise

### What is Noise In Image?

* **Unwanted information which deteriorates image quality**

* Images taken by digital cameras or conventional film cameras will pick up noise from a variety of sources by a device's mechanism or image processing algorithms

* Noise can be random or with different frequency distribution

  * like gaussian noise as known as with normal frquency distrbution

     short noise as known as with Poisson frequency distribution

### Noise Type

#### 1. Salt and Pepper Noise
* to short with, they are sparse light and dark disturbances
  * As you can see in example picture, there are some pixels are very different in color or intensity from their surrounding pixels
  * so when viewed, the image contains dark and white dots, hence in term salt and pepper 
* And they  usually caused by
    *  flecks of dust inside the camera
    * the camera is overheated 

And Next common noise type is :

#### 2. Gaussian Noise

* so they are Noises with Gaussian-ditributed frequency distribution
  * that is to say, each pixel in the image will be changed from its original value by a small amount
  * and the values that the noise can take on are Gaussian-distributed
* Notice that Gaussian distribution - a good model for representing noise frequency in image
  * since by [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem),  the sum of different noises tends to approach a Gaussian distribution (
* And this kind of noise are usally caused
  1. during acquisition - that is, caused by sensor
     * if you take photo in  a poor illumination or  high temperature
  2. or caused by  electronic circuit transmission

So our alogrithm 's goal is to 

## Goal - Noise reduction
###  Image Denoising

* recover the original image from a noisy measurement

####  One Attempt Operator - Smoothing Filters
*  using a [spatial filter](https://en.wikipedia.org/wiki/Spatial_filter) to smooth an image
### Denoising Operator 

* a denoising operator $\large{D_h}$ can be defined as this model

$\Huge{v = D_hv + n(D_h, v)}$ 

*  where we denotes $\large{v} \to$ noisy image that is observed value,    $\large{h}\to$ filtering parameter $\propto$ standard deviation of noise,  $\large{n()} \to$ noise perturbation
*  so a noisy image v after denoising by operator D will approach to the true value of the image
*  And Ideally
   * the true value image should be smoother than the observed noisy image
   * and the noise perturbation should be a realization of a gaussian white noise
*  which is a Special case of *Gaussian noise*

   *  whose values at any pair of times are uncorrelated

Now let us introduce some 

## Previous Work - Local Smoothing Filters

#### we 've been familiar with  Smoothing Filters Algorithm

#### So what is a  Local Smoothing Filters Algorithm

* **Collect information from adjacent pixels to smooth out disturbance**

* **Denoising by Averaging**
  * take the [mean](https://en.wikipedia.org/wiki/Mean) value of a group of pixels surrounding a target pixel to smooth the image

Let's see some example algorithm

### Gaussian Filtering

* Performence 

  * optimal in harmonic flat parts of the image
  * blurred around edges and texture

### Anisotropic Filtering

* Performence

  * the straight edges are well restored
  *  flat and textured regions are degraded

### Neighborhood Filtering

* Performance

  1. the good thing is that the algorithm does not blur the edges
  2. comparing only grey level values in a single pixel is not so robust when these values are noisy

Though Local filter does solve the problem in some degree, there are some

###  common weekness of the local filters 

for example

* fine-scaled image edges and details will get blurred because they also correspond to blocked high frequencies
* image can be over smoothed when they are not very noisy