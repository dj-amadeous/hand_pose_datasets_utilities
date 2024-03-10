from scipy.io import loadmat
import numpy as np
import cv2

ROOT_FOLDER = '/Volumes/Evan_Samsung_HP_data/dataset/'
TEST_FOLDER = ROOT_FOLDER + 'test/'
TRAIN_FOLDER = ROOT_FOLDER + 'train/'
FILENAME = 'joint_data.mat'
JOINT_LIST = [0, 3, 6, 9, 12, 15, 18, 21, 24, 25, 27, 30, 31, 32] # temporary list of joints

def highlight_GT(index):
    '''
    this is experimental code that draws a circle around the ground truth values of a datapoint
    it illustrates and proves that the gt array is
    cam, image, joint, xyz in that order.
    it also keeps track of which joints are typically used for testing, and how to load the GT data.
    '''
    root_folder = '/Volumes/Evan_Samsung_HP_data/dataset/'
    test_folder = root_folder + 'test/'
    train_folder = root_folder + 'train/'
    jnt_filename = 'joint_data.mat'

    img = cv2.imread(test_folder + 'rgb_1_0000001.png')

    jnt_data_tst = loadmat(test_folder + jnt_filename)
    jnt_data_train = loadmat(train_folder + jnt_filename)

    joint_list = [0, 3, 6, 9, 12, 15, 18, 21, 24, 25, 27, 30, 31, 32]

    joint_test_names = jnt_data_tst["joint_names"]
    joint_test_uvd = jnt_data_tst["joint_uvd"]
    joint_test_xyz = jnt_data_tst["joint_xyz"]

    joint_train_names = jnt_data_train["joint_names"]
    joint_train_uvd = jnt_data_train["joint_uvd"]
    joint_train_xyz = jnt_data_train["joint_xyz"]
    # the dimensions of the matrix are CAMxIMGxJOINTx(xyz) 

    # so it's 3xNx24x3
    hand = np.array(joint_test_uvd[0,index, joint_list,:2], dtype=np.int16)

    for kp in hand:
        print(kp)
        cv2.circle(img, kp, radius=10, color=(0,0,255), thickness=2)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return hand

def get_hand(index, joint_xyz, joint_list):
    '''
    @index: The index into the dataset of the keypoint
    @joint_xyz: array of ground truths to pull from
    @joint_list: list of joints we want to use from the array
    @return: returns a 2d array of all the kp on a hand, dimensions [len(joint_list)]x3
    '''
    testing = False
    if testing:
        hand = np.array(joint_xyz[0, index, :, :])
    else:
        hand = np.array(joint_xyz[0, index, joint_list, :])
    return hand