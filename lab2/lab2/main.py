from todo import *


answer = str(input("You want hide message(h) or find message(f)?\n"))

if answer == "h":
    image_name = input("Enter image name with extension:\n ")
    image = cv2.imread(image_name)  # Read the input image using OpenCV-Python.
    # It is a library of Python bindings designed to solve computer vision problems.

    # details of the image
    print("The shape of the image is: ", image.shape)  # check the shape of image to calculate the number of bytes in it
    print("The original image is as shown below: ")
    resized_image = cv2.resize(image, (500, 500))  # resize the image as per your requirement
    plt.imshow(resized_image)  # display the image

    data = input("Enter data to be encoded : ")
    if len(data) == 0:
        raise ValueError('Data is empty')

    filename = input("Enter the name of new encoded image(with extension): ")
    encoded_image = hideText(image,
                             data)  # call the hideData function to hide the secret message into the selected image
    cv2.imwrite(filename, encoded_image)

elif answer == "f":
    print("im ready to find")
else:
    print("choose right mode:c")
