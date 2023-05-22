RandArt:

RandArt is a Python application that generates and displays random art using SVG images. 
It utilizes the PyQt6 library for the graphical user interface and interacts with an external SVG image repository.

Usage:

Upon running the RandArt application, a window will appear with the following options:

    *Add Image: 
    Click this button to add a new image to the canvas. 
    The application will randomly select an image from the available SVG image repository and display it on the canvas. Each image is draggable and selectable.

    *Group Images: 
    Select multiple images using Ctrl key and click this button to group selected images together. 
    Once grouped, you can move the entire group by dragging any of the images within the group. Grouped images can be selected and manipulated as a single entity.

    *Canvas: 
    The canvas is the main area where images are displayed. 
    You can drag and drop images to reposition them. Images can be selected individually or as a group.

    *Image Properties: When you add an image to the canvas, its properties, such as size and color, will be displayed in a text box adjacent to the image.
    
Methodology:

    1. Importing Required Libraries: sys, random, requests, and various PyQt6 modules for GUI development.

    2. Application Setup: The QApplication instance is created to initialize the PyQt6 application. This sets up the application's event loop and manages the GUI components.

    3. Image Repository and Lists: The application defines a list lst that contains the names of SVG images to be randomly selected. Additional names and patterns are appended to the list based on specific criteria.

    4. Customizing the Main Window: The MainWindow class is defined, which subclasses QMainWindow to customize the application's main window. The class includes methods and properties for setting up the window geometry, creating the graphics scene and view, adding buttons, and managing the layout.

    5. Adding Image Functionality: The add_image method is implemented within the MainWindow class. It is triggered when the "Add Image" button is clicked. This method selects a random image name from the list, retrieves the SVG image data from an external repository, and creates a QPixmap and QSvgWidget from the image data. The image is then added to the QGraphicsScene, and its properties, such as size and color, are displayed in a text item adjacent to the image.

    6. Displaying Image Properties: The display_image_properties method is responsible for extracting and displaying the image properties, such as size and color. It creates a QGraphicsTextItem and sets its position based on the image's position. The method also removes the previously displayed text item before adding the new one.

    7. Overlap Checking: The check_overlap method checks for overlaps between the newly added image and any existing items on the scene. It iterates through all the items in the scene and compares their collision with the new image. If an overlap is detected, the method returns True, indicating that the image needs to be repositioned.

    8. Grouping Images: The group_images method is triggered when the "Group Images" button is clicked. It selects the currently selected images in the scene and groups them together using the QGraphicsItemGroup class. The grouped images can then be moved as a single entity.

    9. Creating the Main Window and Running the Application: An instance of the MainWindow class is created, and the application's main window is displayed using the show method. Finally, the app.exec() function is called to start the event loop and run the application.
    
Acknowledgements:

RandArt makes use of the openmoji repository (https://github.com/hfg-gmuend/openmoji) for the SVG images. 
The application fetches random SVG images from this repository to generate the artwork.

PS: View the RandArt application in full-screen mode!
