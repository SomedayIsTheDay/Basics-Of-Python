import time
import colorama

# 1


class TrafficLight:
    __color = ['Red']

    def running(self):
        timeout = 60
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for q in self.__color:
                print(colorama.Fore.RED + q)
                self.__color.clear()
                self.__color.append('Yellow')
                time.sleep(7)
                for w in self.__color:
                    print(colorama.Fore.YELLOW + w)
                    self.__color.clear()
                    self.__color.append('Green')
                    time.sleep(2)
                    for e in self.__color:
                        print(colorama.Fore.GREEN + e)
                        self.__color.clear()
                        self.__color.append('Yellow')
                        time.sleep(5)
                        for r in self.__color:
                            print(colorama.Fore.YELLOW + r)
                            self.__color.clear()
                            self.__color.append('Red')
                            time.sleep(2)


a = TrafficLight()
a.running()


# 2
class TrafficLight:
    __color = ['Red']

    def running(self):
        timeout = 60
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            print(colorama.Back.RED)
            self.__color.clear()
            self.__color.append('Yellow')
            time.sleep(7)
            print(colorama.Back.YELLOW)
            self.__color.clear()
            self.__color.append('Green')
            time.sleep(2)
            print(colorama.Back.GREEN)
            self.__color.clear()
            self.__color.append('Yellow')
            time.sleep(5)
            print(colorama.Back.YELLOW)
            self.__color.clear()
            self.__color.append('Red')
            time.sleep(2)


a = TrafficLight()
a.running()


# 3 without attribute and method
class TrafficLight:
    timeout = 60  # how long traffic_light will light in seconds
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        print(colorama.Back.RED)
        time.sleep(7)
        print(colorama.Back.YELLOW)
        time.sleep(2)
        print(colorama.Back.GREEN)
        time.sleep(5)
        print(colorama.Back.YELLOW)
        time.sleep(2)


TrafficLight()

