import os

os.chdir('c:\\pyth\\mur\\tdir')

# Hiermee kun je checken in welke directory je zit
# print(os.getcwd())

#
# for f in os.listdir():
#     print(os.path.splitext(f))

# we gaan splitsen op de - teken
# for f in os.listdir(): 
#     file_name, file_ext = (os.path.splitext(f))
#     print(file_name)


# for f in os.listdir():
#     file_name, file_ext = (os.path.splitext(f))
#     print(file_name.split('-'))


# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)

#     f_title, f_course, f_num = file_name.split('-')
#     print(f_title)
#     print(f_course)
#     print(f_num)


# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)

#     f_title, f_course, f_num = f_name.split('-')

#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))


#we moeten nu nog de spaties wegwerken
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)

#     f_title, f_course, f_num = f_name.split('-')

#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num =f_num.strip()

#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))


# we gaan nu de # teken voor de filenaam aanpakken
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)

#     f_title, f_course, f_num = f_name.split('-')

#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num =f_num.strip()[1:]

#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))


# we gaan nu zorgen dat de sortering moet kloppen bv 1 en de 10 we gaan extra 00 toevoegen
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)

#     f_title, f_course, f_num = f_name.split('-')

#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num =f_num.strip()[1:].zfill(2)

#     print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))


#  we gaan nu de course name  "Our Solar System" eruit gooien
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)

#     f_title, f_course, f_num = f_name.split('-')

#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     f_num =f_num.strip()[1:].zfill(2)

#     print('{}-{}{}'.format(f_num, f_title, f_ext))


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num =f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name)

    