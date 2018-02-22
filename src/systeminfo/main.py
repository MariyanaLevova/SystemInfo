import platform

def get_info():
    return platform.platform()

def shortcut():
    print("The system is:",platform.platform())

if __name__ == '__main__':
    main()
