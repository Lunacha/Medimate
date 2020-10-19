import io
from ImgPreprocessor import ImgPreprocessor
from google.cloud import vision
from google.cloud.vision import types

class OCRProcessor:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def OCRExecute(self, file_name=None):

        if file_name is not None:
            with io.open("./data/" + file_name, 'rb') as img_file:
                content = img_file.read()

        drug_img = types.Image(content=content)

        response = self.client.text_detection(image=drug_img)
        drug_texts = response.text_annotations

        print('Texts: ')

        for text in drug_texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                         for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))


if __name__ == '__main__':
    img_pproc = ImgPreprocessor()
    drug_image = img_pproc.ProcExecute("viekira.jpg")
    img_pproc.display()
    ocr = OCRProcessor()
    ocr.OCRExecute("tmp.jpg")
