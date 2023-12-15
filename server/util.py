import joblib
import json
import cv2
import base64
import numpy as np

__class_number_to_name = {}
__class_name_to_number = {}
__model = None

# data = './test_images/00004.png'

final = []
def classify_images(image_base64_data, file_path=None):
    img = get_data(file_path, image_base64_data)

    img = cv2.resize(img, (30,30))
    img = np.expand_dims(img, axis=0)
    result = __model.predict(img)[0]
    result = np.argmax(result)
    final.append({
        'class': class_number_to_name(result)
    })
    # final = class_number_to_name(result)
    # print(final)
    return final



def get_cv2_image_from_base64_string(b64str):
    '''
    credit: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    :param uri:
    :return:
    '''
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def get_data(image_path, image_base64_data):
    if image_path:
        img = cv2.imread(image_path)
    else:
        img = get_cv2_image_from_base64_string(image_base64_data)
    return img



# final = []
# def classify_images(filename):
#     img = cv2.imread(filename)
#     img = cv2.resize(img, (30,30))
#     img = np.expand_dims(img, axis=0)
#     result = __model.predict(img)[0]
#     result = np.argmax(result)
#     final.append({
#         'class': class_number_to_name(result)
#     })
#     # final = class_number_to_name(result)
#     # print(final)
#     return final

def class_number_to_name(class_num):
    return __class_number_to_name[class_num+1]


def load_saved_artifacts():
    print("loading saved artifcats......start")
    global __class_number_to_name

    with open("./artifacts/labels.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {k:v for v,k in __class_name_to_number.items()}
        

    global __model
    if __model is None:
        with open("./artifacts/saved_model.pkl", "rb") as f:
            __model = joblib.load(f)
    print("loading saved artifacts......done")

def get_b64_data():
    with open("b64.txt") as f:
        return f.read()


if __name__ == '__main__':
    load_saved_artifacts()
    # print(classify_images(None, "./test_images/00004.png"))
    print(classify_images(get_b64_data(), None))