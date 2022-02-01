
# README: Sorting Algorithms Visualiser

## Description

This project visualises various in place sorting algorithms. At the moment, the algorithms that can be visualised are the bubble, selection and insertion sorts.

The program will sort an unordered, randomly generated dataset of a given size by ascending order, and it will do so utilising the sorting algorithm as instructed. THe program will also visualise the steps of each sorting algorithm so that one can understand how each sorting algorithm works.

### In more detail

#### **Colors**

The program will generate an unsorted dataset of specified length and represent each number in this dataset using a bar, where the height of the bar is proportional to the magnitude of the number. When the sorting begins, the program will highlight two rectangles, one in blue and one in red. Since at the moment all three sorting algorithms require a nested loop, the rectangle in blue shows the element of the first loop which is the element which the algorithm is currently sorting, and the red rectangle shows the element of the inner loop, which is the element that is being compared to the element of the blue rectangle.

#### **Time**

In order to make the visualisation of each algorithm as clear as possible, various delays were added ar different points of the sorting in each algorithm. This means that the selection sort is manually slowed down more than the insertion sort so that it is easier to understand what is happenning. Therefore, the time taken by the algorithms to sort cannot be used comparatively to determine which algorithm is fastest. Instead, I have used two other metrics: the number of comparisons made by the algorithms, and the number of swaps made. These can be used to compare the efficiency of the sorting algorithms.

## Usage

Instructions on how to use the program are displayed on the program itself. Below is an exhaustive list of possible interactions with the program:

| Key | Action |
| :--------: | :--------------------------------------------------: |
| SPACEBAR   | Generates a new randomised data set                  |
| UP ARROW   | Increases the number of elements in the data set     |
| DOWN ARROW | Decreases the number of elements in the data set     |
| B          | Begins sorting the data set using the bubble sort    |
| S          | Begins sorting the data set using the selection sort |
| I          | Begins sorting the data set using the insertion sort |

On the top left corner of the window there are also some buttons. Clicking on any button will multiply the speed of sorting by the number displayed on the button. Note that clicking on a button multiple times will not keep multiplying the speed as when a button is cliked the speed is first set to the original sorting speed and then multiplied by the number on the button. That is to say that the maximum possible speed is times 8.

## Extensions

The program can be extended and ameliorated in many ways. Below are some which I would like to implement in future:

- Add more sorting algorithms such as merge sort, heap sort and quick sort.
- Make the insertion sort visualisation more clear by showing how the selected rectangle moves down the data set into its place rather than somply highlighting the rectangles down the data set. Ideally, the insertion sort visualisation should look something like [this](https://www.youtube.com/watch?v=8oJS1BMKE64).
- Add sounds to the sorting where the frequency of the sound depends on the height of the bars.
- At the moment, while the program is sorting it disables all other actions from taking place. While this avoids many bugs, it sometimes mean the program has to be forcibly stopped. It would be useful if all actions where allowed while sorting.

## Contact me

You can always shoot me an email at javier.fergarcia@gmail.com :).
