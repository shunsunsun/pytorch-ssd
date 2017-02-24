'''Convert VOC PASCAL 2007/2012 xml annotations to a list file.'''

import os
import xml.etree.ElementTree as ET


VOC_LABELS = (
    'aeroplane',
    'bicycle',
    'bird',
    'boat',
    'bottle',
    'bus',
    'car',
    'cat',
    'chair',
    'cow',
    'diningtable',
    'dog',
    'horse',
    'motorbike',
    'person',
    'pottedplant',
    'sheep',
    'sofa',
    'train',
    'tvmonitor',
)

xml_dir = '/mnt/hgfs/D/download/PASCAL VOC/VOC2007/Annotations/'

f = open('index.txt', 'w')
for xml_name in os.listdir(xml_dir):
    print('converting %s' % xml_name)
    image_name = xml_name[:-4]+'.jpg'
    f.write(image_name+' ')

    tree = ET.parse(os.path.join(xml_dir, xml_name))
    annos = []
    for child in tree.getroot():
        if not child.tag == 'object':
            continue

        bbox = child.find('bndbox')
        xmin = bbox.find('xmin').text
        ymin = bbox.find('ymin').text
        xmax = bbox.find('xmax').text
        ymax = bbox.find('ymax').text

        class_label = VOC_LABELS.index(child.find('name').text)
        annos.append('%s %s %s %s %s' % (xmin,ymin,xmax,ymax,class_label))

    f.write('%d %s\n' % (len(annos), ' '.join(annos)))
f.close()
