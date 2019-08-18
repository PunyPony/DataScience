# Simple Muffin vs Chihuahua dataset

I did not find a dataset to train Muffin vs Chihuahua classifiers,
so I created one by crawling the Internet.

It contains crazy and less crazy pictures of many things, but usually either
- a chihuahua-like animal (plus other things);
- a muffin-like pastry (plus other things).

The dataset is **IMBALANCED**: you should take this into account before training
any classifier.


## Student task
1. train a classifier using the train and validation set (split it as per your needs);
2. process the test set to produce a submission file which will be used for grading.


## Files

For the **student** pack:
- `meme_jpg/`: contains original meme images, for fun;
- `meme_siftgeo/`: contains SIFT descriptors of original meme images, for fun;
- `test_set_sift/`: contains the SIFT descriptors of the 400 test set images;
- `train_val_set_jpg/`: contains 2694 training and validation images for both classes:
   1416 for the "chihuahua" (`chi`) class, and 1278 for the "muffin" (`muf`) class;
- `train_val_set_siftgeo/`: contains the SIFT descriptors of the training and validation images
   for both classes;
- `sample_results.json`: an example of result file (with random results);
- `README.md`: this file.


For the **teacher** pack:
- `gt.json`: ground truth for the test set;
- `orig_to_new.json`: mapping which was used to randomly rename the images for the test set;
- `test_set_jpg/`: images for the test set, with the same names as the randomized siftgeo files;
- `README.md`: this file.


## About the SIFT descriptors used (`.siftgeo` files)
Descriptors are stored in raw together with the region information provided by the software of Krystian Mikolajczyk.
There is no header (use the file length to find the number of descriptors).
A descriptor takes 168 bytes (floats and ints take 4 bytes, and are stored in little endian):
```
field      field type   description
x          float        horizontal position of the interest point
y          float        vertical position of the interest point
scale      float        scale of the interest region
angle      float        angle of the interest region
mi11       float        affine matrix component
mi12       float        affine matrix component
mi21       float        affine matrix component
mi22       float        affine matrix component
cornerness float        saliency of the interest point
desdim     int          dimension of the descriptors
component  byte*desdim  the descriptor vector (dd components)
```



## LICENSE
As we do not hold the copyright for the images used in this dataset,
it should be kept for private use.
