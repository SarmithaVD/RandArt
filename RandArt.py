import sys, random, requests
from PyQt6.QtCore import Qt, QByteArray, QSize
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QPixmap, QPainter, QImage, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QGraphicsScene, QGraphicsTextItem, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QGraphicsPixmapItem, QGraphicsItem, QGraphicsItemGroup

app = QApplication(sys.argv)

# List of the image names
lst = ['1F4A0', '1F518']
name1 = '1F53'
name2 = '1F7E'
name3 = '25A'
name4 = '25F'
name5 = '26A'
name6 = '2B1'
numb = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
alpha = ['A', 'B', 'C', 'D', 'E']

for i in numb:
    j = int(i)
    lst.append(name2 + i)
    if j>1 and j<=9:
        lst.append(name1 + i)

for i in alpha:
    if i<='B':
        lst.append(name1 + i)
        lst.append(name2 + i)
        lst.append(name3 + i)
        lst.append(name5 + i)
    if i>'A':
        lst.append(name4 + i)
    if i=='B' or i=='C':
        lst.append(name6 + i)

# Subclass QMainWindow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_item = None

        self.setWindowTitle("RandArt")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.button1 = QPushButton("Add Image", self)
        self.button2 = QPushButton("Group Images", self)
        self.button1.clicked.connect(self.add_image)
        self.button2.clicked.connect(self.group_images)

        view = QGraphicsView(self.scene)
        view.show()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        self.images = []

    def showMinimized(self):
        pass

    # Function to add a new image
    def add_image(self):
        image_path = "https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{}.svg" # image link
        image_name = random.choice(lst) 
        image_url = image_path.format(image_name)

        image_data = requests.get(image_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        # Creating a QSvgWidget and load the image data
        svg_widget = QSvgWidget()
        svg_widget.load(QByteArray(image_data))

        # Creating a QPixmap from the QSvgWidget
        pixmap = QPixmap(svg_widget.size())
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        svg_widget.render(painter)
        painter.end()

        # Adding the QPixmap to the QGraphicsScene
        pixmap_item = self.scene.addPixmap(pixmap)
        pixmap_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        pixmap_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        # Size of the loaded image
        image_size = pixmap_item.pixmap().size()

        # Colour of the loaded image
        image = QImage(svg_widget.size(), QImage.Format.Format_ARGB32)
        width = image.width()
        height = image.height()
        x = width // 2
        y = height // 2
        color_value = image.pixel(x, y)
        color = QColor(color_value)
        pixel_color = color.getRgb()[:3]  # Extracting RGB values
        
        # Checking for overlaps with existing items and adjusting position if necessary
        while self.check_overlap(pixmap_item):
            x = random.randint(0, self.view.width() - pixmap.width())
            y = random.randint(0, self.view.height() - pixmap.height())
            pixmap_item.setPos(x, y)

        self.scene.addItem(pixmap_item)
        self.images.append(pixmap_item)

        # Displaying colour and size
        self.display_image_properties(image_size, pixel_color, x, y)

    def display_image_properties(self, size, color, x, y):
        text_item = QGraphicsTextItem()
        size = str(size)

        # Width and Height
        width_start = size.index("(") + 1
        width_end = size.index(",")
        height_start = size.index(",") + 2
        height_end = size.index(")")

        width = int(size[width_start:width_end])
        height = int(size[height_start:height_end])

        size = f"{width}x{height}"

        text = 'Size: ' + size + '\nColor: ' + str(color)
        text_item.setPlainText(text)
        text_item.setPos(x+75, y+75)  # Position of the text item

        # Removing previously displayed text item (if any)
        if self.text_item is not None:
            self.scene.removeItem(self.text_item)

        self.text_item = text_item
        self.scene.addItem(self.text_item)

    # Function to check for overlaps
    def check_overlap(self, item):
        for existing_item in self.scene.items():
            if existing_item is item:
                continue
            if existing_item.collidesWithItem(item):
                return True
        return False

   # Function to group the images 
    def group_images(self):
        group = QGraphicsItemGroup()
        for image in self.scene.selectedItems():
            group.addToGroup(image)

        group.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.scene.addItem(group)

window = MainWindow()
window.show()

app.exec()