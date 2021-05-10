import pydicom
import os
import cv2


def dicom2jpg(filepath):
    ds = pydicom.dcmread(filepath)
    img_path = os.path.join('/Users/qiuyaoyang/Documents/OCT/data_fuwai/image',
                            '{}_{}'.format(ds.PatientID, ds.AcquisitionDate))
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    data = ds.pixel_array
    for i in range(data.shape[0]):
        cv2.imwrite(os.path.join(img_path, '{}.jpg'.format(i)), data[i])


if __name__ == '__main__':
    ds = pydicom.dcmread('/Users/qiuyaoyang/Documents/OCT/data_fuwai/IMG001.dcm')
    img_path = os.path.join('/Users/qiuyaoyang/Documents/OCT/data_fuwai/image',
                            '{}_{}'.format(ds.PatientID, ds.AcquisitionDate))
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    data = ds.pixel_array
    for i in range(data.shape[0]):
        cv2.imwrite(os.path.join(img_path, '{}.jpg'.format(i)), data[i])
    pass
