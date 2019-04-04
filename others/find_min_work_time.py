
# def find_max_work_time(processor):
#
#     print('I have', processor, 'processor')
#
#     while True:
#
#         works_input = input("input your five works: ")
#
#         works = [int(work) for work in works_input.split()]
#
#         if len(works) == 5:
#             break
#
#     works = sorted(works)
#
#     return max(works[0] + works[1], works[4])


def add_min_to_second(works):

    works = sorted(works)

    if len(works) > 1:
        new_work = works[0] + works[1]

        del works[0]
        del works[1]

        works.append(new_work)

        return works

    else:
        return works


def find_max_work_time(processor, num_works):

    while True:

        works_input = input('input your works: ')

        works = [int(work) for work in works_input.split()]

        if len(works) == num_works:
            break

    while len(works) > processor:

        works = add_min_to_second(works)

        if len(works) == processor:

            return(max(works))


if __name__ == "__main__":

    print(find_max_work_time(4, 5))


