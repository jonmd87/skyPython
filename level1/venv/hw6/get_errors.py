errors_dict = dict(out='you have log out from system.',
                   noaccess='You don\'t have access for this section.',
                   unknown='Unknown error.',
                   timeout='The system is not responding',
                   robot='You act as robot',
                   )


def get_errors(*list_of_errors):
    temp_list = []
    for item in list_of_errors:
        if item in errors_dict:
            temp_list.append(errors_dict[item])

    return tuple(temp_list)


print(get_errors('out', 'robot'))
