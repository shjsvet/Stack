class StackIsEmptyError(Exception):
    def __init__(self):
        self.__massage = "stack is empty"


    def __str__(self):
        return self.__massage


class Stack:
    def __init__(self, *args):
        self.__content = []
        self.__content.extend(args)


    def push(self, el):
        self.__content.append(el)


    def pop(self):
        if len(self.__content) == 0:
            raise StackIsEmptyError()
        end = self.__content[-1]
        del self.__content[-1]
        return end


    def top(self):
        return self.__content[-1]


    def size(self):
        return len(self.__content)


    def is_empty(self):
        return len(self.__content) == 0


    def print_stack(self):
        print(self.__content)
