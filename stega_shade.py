from PIL import Image
import numpy as np
import math
from . import enc

common_characters =  {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 11: 'j', 12: 'k', 13: 'l', 14: 'm', 15: 'n', 16: 'o', 17: 'p', 18: 'q', 19: 'r', 21: 's', 22: 't', 23: 'u', 24: 'v', 25: 'w', 26: 'x', 27: 'y', 28: 'z', 29: 'A', 31: 'B', 32: 'C', 33: 'D', 34: 'E', 35: 'F', 36: 'G', 37: 'H', 38: 'I', 39: 'J', 41: 'K', 42: 'L', 43: 'M', 44: 'N', 45: 'O', 46: 'P', 47: 'Q', 48: 'R', 49: 'S', 51: 'T', 52: 'U', 53: 'V', 54: 'W', 55: 'X', 56: 'Y', 57: 'Z', 58: '0', 59: '1', 61: '2', 62: '3', 63: '4', 64: '5', 65: '6', 66: '7', 67: '8', 68: '9', 69: '!', 71: '@', 72: '#', 73: '$', 74: '%', 75: '^', 76: '&', 77: '*', 78: '(', 79: ')', 81: '-', 82: '_', 83: '=', 84: '+', 85: ';', 86: ':', 87: "'", 88: '"', 89: ',', 91: '.', 92: '<', 93: '>', 94: '/', 95: '?', 96: ' '}


reversed_dict = {value: key for key, value in common_characters.items()}



def image_to_array(image_path):
    with Image.open(image_path) as img:
        return np.array(img)

def array_to_image(array, output_path):
    img = Image.fromarray(array)
    img.save(output_path)


def encode_data(dat):
    l = []
    for e in dat:
        x =  reversed_dict.get(e, 0)
        if x < 10:
            y = "0"
            x = str(x)
        else:
            x = str(x)
            y = x[0]
            x = x[1]

        l.append(y)
        l.append(x)

    return l

def decode_data(dat):
    l = ""
    prev = ""
    for e in dat:
        if prev == "":
            prev = e
        else:
            if prev == "0":
                l += common_characters.get(int(e), "<Unknown Char>")
                prev = ""
            else:
                l += common_characters.get(int(prev + e), "<Unknown Char>")
                prev = ""
    return l


def process_image_array(image_array, data):
    # Create an output array to store the processed values
    processed_array = image_array.copy()
    
    u = 0
    
    for i in range(processed_array.shape[0]):  
        for j in range(processed_array.shape[1]):  
            for e in range(processed_array.shape[2]):
                if e  != 3:
                    x =  str(processed_array[i, j , e])
                
                    if len(x) == 3:
                        x = x[0] + x[1] + "0"
                    elif len(x) == 2:
                        x = x[0] + "0"
                    else:
                        x = 10
                    
                    x = int(x)

                    if u < len(data):
                        if u%2 == 0:
                            x += int(data[u])
                        else:
                            x -= int(data[u])
                        u += 1
                                
                    processed_array[i, j, e] = x           

    return processed_array

def simple_shade_stega(image_path, output, data):
    data =  encode_data(data + "##END##")
    img = image_to_array(image_path)
    img = process_image_array(img, data)
    array_to_image(img, output)    
            
def undo_simple_shade_stega(image_path):
    processed_array = image_to_array(image_path)
    u = 0
    data = []
    for i in range(processed_array.shape[0]):  
        for j in range(processed_array.shape[1]):  
            for e in range(processed_array.shape[2]):
                if e  != 3:
                    x = str(processed_array[i, j, e])
                    if u%2 == 0:
                        data.append(x[-1])
                    else:
                        data.append(str(10-int(x[-1]))) 
                    u += 1
                        
    dat = decode_data(data)
    return dat.rsplit("##END##", 1)[0]

def protected_shade_stega(image_path, output, data, pwd):
    simple_shade_stega(image_path, output, enc.encrypt(data, pwd))

def undo_protected_shade_stega(image_path, pwd):
    return enc.decrypt(undo_simple_shade_stega(image_path), pwd)
