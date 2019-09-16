from cmpx import print_err

def main():
    try:
        raise ValueError('Just for testing purposes')
    except ValueError as err:
        print_err(err)

if __name__ == '__main__': main()