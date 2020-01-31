1.Exercise:Python: 
Input a grey-scale image, count number of colored areas in the image. Output the  result.

The implement is in Bruce_Gong_exercise1.py. It is a class called count_area(). The function count_areas() is used to count the areas for different grayscale level and output them. It can read .bin image and .png,.jpeg,.jpg image by using ReadBin() and ReadImage() automatically.

The algorithm:
1. Get the number of grayscale levels
2. Loop each grayscale levels, mark it to 1 and others to 0
3. Apply CCA 2 pass algorithm to find the numbers of areas of this grayscale level
4. Save the numbers of areas for each grayscale level in an Array. End the loop of each grayscale

Input: .bin image or .png,.jpeg,.jpg image; height and length.

Output: array of 256 unsigned int numbers, each of them being a count of areas
colored with the corresponding shade of grey.

 'shades-of-grey.png' and 'sample.bin'.

How to use it:

> python3 count-areas.py <filename> --shape <height>,<width>

For example:

> python3 count-areas.py cat.420x240.bin --shape 240,420


