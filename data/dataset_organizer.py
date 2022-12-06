import os



source_path = '../datasets/images_front_left_door/'
dest_path = '../datasets/images_front_left_door/B/'


file_names = os.listdir(source_path)

for file_name in file_names:
    if 'no_reflections' in file_name:
        print(file_name)
        new_file_name = file_name.replace('_no_reflections','')
        print(new_file_name)
        os.rename(source_path+file_name, dest_path+new_file_name)

